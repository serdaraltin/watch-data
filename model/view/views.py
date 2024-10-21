from app import app, processes_list, processes_dict
from flask import request, jsonify, Response, send_file, request
from database.connector.connector_postgre import CameraDatabase
from modules.process.processes import (
    start_async_person_counter_process,
    stop_async_person_counter_process,
    delete_async_person_counter_process,
)
from database.connector.connector_postgre import PersonDatabase, CameraDatabase
import cv2
import time
import json
import torch
from config import config
from services.logging.logger import custom_logger


def check_camera_id(camera_id):

    if camera_id in config.setting.processing.source:
        return True
    else:
        return False

# rtsp://95.70.182.136:554/user=itsumi&password=yu09ke17&channel=1&stream=0.sdp?
# rtsp://45.139.203.25:554/user=minoapera&password=Minoa2024.
def get_stream_url(camera_info): 
    protocol = camera_info['protocol'].lower()

    if "host" in camera_info and "port" in camera_info:
        host_or_domain = f"{camera_info['host']}:{camera_info['port']}"
    else:
        host_or_domain = camera_info["domain_name"]

    credentials = ""
    if not camera_info.get("stream_path"):
        keys = ["user", "password", "channel"]
        for key in keys:
            credentials += f"{key}={camera_info[key]}&"
        
        credentials = credentials[:-1]
    else:
        credentials = camera_info.get("stream_path")

    result = f"{protocol}://{host_or_domain}/{credentials}"

    return result


def check_camera_stream(camera_info):
    stream_url = get_stream_url(camera_info=camera_info)

    cap = cv2.VideoCapture(stream_url)

    if not cap.isOpened():
        cap.release()
        custom_logger.error("Camera stream could not be opened.", exc_info=True)

        return {"error": "Camera stream could not be opened."}

    start_time = time.time()
    while True:
        ret, frame = cap.read()
        if ret:
            # cv2.imshow("Camera Stream", frame)
            cv2.waitKey(1)
            if time.time() - start_time > 5:
                cv2.destroyAllWindows()
                cap.release()
                return {
                    "message": "Camera connection and stream are successful.",
                    "status": True,
                }
        else:
            cv2.destroyAllWindows()
            cap.release()
            custom_logger.error("Camera stream failed.", exc_info=True)

            return {"error": "Camera stream failed."}


def replace_source_in_config(file_path, camera_id, new_source):
    with open(file_path, "r") as file:
        config = json.load(file)

    # config["setting"]["processing"]["source"][camera_id] = new_source

    source =  config["setting"]["processing"]["source"]

    source[str(camera_id)] = new_source     
    config["setting"]["processing"]["source"] = source

    with open(file_path, "w") as file:
        json.dump(config, file, indent=4)



def get_camera_size(cam_url, points):

    # Video akışını başlat
    cap = cv2.VideoCapture(cam_url)
    print("ok")
    # Video akışı başarılı bir şekilde açıldı mı kontrol et
    if not cap.isOpened():
        return "Video akışı başlatılamadı"
    # Video boyutunu al

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # Akışı serbest bırak
    cap.release()
    
    # Normalleştirilmiş koordinatları gerçek piksel değerlerine çevir
    real_points = []
    count = 0
    for point in points:
        if count == 2:
            break
        real_x = int(point['x'] * width)
        real_y = int(point['y'] * height)
        real_points.append({'x': real_x, 'y': real_y})
        count += 1
    # Gerçek piksel koordinatlarını ve video boyutunu döndür
    return (int(width), int(height)), real_points





@app.route("/api/camera/add", methods=["POST"])
def camera_add():
    try:
        request_data = request.get_json()
        camera_id = request_data.get("camera_id")
        # points = request_data.get("points")
        # threshold_time = request_data.get("threshold_time")
        # enter_direction = request_data.get("enter_direction")
        points = list()
        camera_database = CameraDatabase()
        camera_json = camera_database.get_camera_by_id(camera_id)
        video_path = get_stream_url(camera_json)
        print("="*50)
        print(video_path)
        print("="*50)
       
        additional_json = json.loads(camera_json["additional"])

        print(additional_json["points"])
        print(type(additional_json["points"]))
        

        video_path = "rtsp://minoapera:Minoa2024.@45.139.203.25:554/Streaming/Channels/101"
        # video_path = "rtsp://13.48.185.247:8554/live-stream"

        cam_size, cam_points  = get_camera_size(cam_url=video_path, points=additional_json["points"])

        points.append([cam_points[0]["x"], cam_points[0]["y"]])
        points.append([cam_points[1]["x"], cam_points[1]["y"]])
        print("="*50)
        print(points)
        print("="*50)

        source_data = {
            "video_path": video_path,
            "point_data": {
                "points": points,
                # "threshold_time": threshold_time,
                "threshold_time": 5,
                # "enter_direction": enter_direction,
                "enter_direction": [0, 1],
            },
            "camera_id": camera_id,
        }


        file_path = "config/json/config.json"
        replace_source_in_config(file_path=file_path, camera_id=camera_id, new_source=source_data)
        
        # torch.cuda.empty_cache()

        print("Process Starting")
        start_async_person_counter_process(camera_id=str(camera_id))
        print("Process Started")

        custom_logger.info(f"Camera added. Source data: {source_data}\n\n")

        return jsonify({"status": True})

    except Exception as e:
        print(e)
        custom_logger.error("Camera add error\n{e}", exc_info=True)
        return jsonify({"error": str(e)}), 500


@app.route("/api/camera/update", methods=["POST"])
def camera_update():
    try:

        request_data = request.get_json()
        camera_id = request_data.get("camera_id")
        points = request_data.get("points")
        threshold_time = request_data.get("threshold_time")
        enter_direction = request_data.get("enter_direction")

        camera_database = CameraDatabase()
        camera_json = camera_database.get_camera_by_id(camera_id)
        video_path = get_stream_url(camera_json)

        source_data = {
            "video_path": video_path,
            "point_data": {
                "points": points,
                "threshold_time": threshold_time,
                "enter_direction": enter_direction,
            },
            "camera_id": camera_id,
        }

        file_path = "config/json/config.json"
        replace_source_in_config(file_path=file_path, camera_id=camera_id, new_source=source_data)

        torch.cuda.empty_cache()

        print("Process Starting")
        start_async_person_counter_process(camera_id=str(camera_id))
        print("Process Started")
        custom_logger.info(f"Camera updated. Source data: {source_data}\n\n")
        return jsonify({"status": True})

    except Exception as e:
        custom_logger.error("Camera update error\n{e}", exc_info=True)

        return jsonify({"error": str(e)}), 500


@app.route("/api/camera/delete", methods=["POST"])
def camera_delete():
    try:
        request_data = request.get_json()
        camera_id = request_data.get("camera_id")

        delete_async_person_counter_process(camera_id=camera_id)
        custom_logger.info(f"Camera deleted. Camera id: {camera_id}\n\n")

        return jsonify({"status": True, "message": f"{camera_id} process deleted"})

    except Exception as e:
        custom_logger.error("Camera delete error\n{e}", exc_info=True)

        return jsonify({"error": str(e)}), 500


@app.route("/api/camera/get", methods=["POST"])
def camera_get():
    try:
        request_data = request.get_json()
        camera_id = request_data.get("camera_id")

        camera_database = CameraDatabase()
        camera_json = camera_database.get_camera_by_id(camera_id)
        custom_logger.info("Camera information received. Camera id: {camera_id}\n\n")

        return jsonify(camera_json)

    except Exception as e:

        custom_logger.error("Error receiving camera information\n{e}", exc_info=True)

        return jsonify({"error": str(e)}), 500


@app.route("/api/camera/list", methods=["POST"])
def camera_list():
    try:
        result_list = list()
        for i in processes_dict:
            result_list.append(i)


        custom_logger.info(f"Camera listed. List: {result_list}\n\n")

        return jsonify({"camera_list": result_list})
    except Exception as e:
        custom_logger.error("An error was encountered while listing the camera\n{e}", exc_info=True)

        return jsonify({"error": str(e)}), 500


@app.route("/api/camera/test", methods=["POST"])
def get_camera():
    request_data = request.get_json()
    camera_id = request_data.get("camera_id")

    camera_database = CameraDatabase()
    camera_json = camera_database.get_camera_by_id(camera_id)
    print(camera_json)
    result = check_camera_stream(camera_json)
    custom_logger.info(f"Camera tested. Camera id: {camera_id}\n\n")

    return jsonify({"message": result})


@app.route("/api/camera/start", methods=["POST"])
def camera_start():
    try:

        request_data = request.get_json()
        camera_id = str(request_data.get("camera_id"))
        torch.cuda.empty_cache()

        print("Process Starting")
        start_async_person_counter_process(camera_id=camera_id)
        print("Process Started")


        custom_logger.info(f"Camera started. Camera id: {camera_id}\n\n")

        # config.setting.processing.source[str(camera_id)]["camera_id"]}    
        return jsonify(
            {"status": True, "camera_id":config.setting.processing.source[str(camera_id)]["camera_id"]}   
        )

    except Exception as e:

        custom_logger.error("Error initializing the camera\n{e}", exc_info=True)
        return jsonify({"error": str(e)}), 500

@app.route("/api/camera/start/multi", methods=["POST"])
def camera_start_multi():
    try:

        request_data = request.get_json()
        camera_list = request_data.get("camera_list")
        print("camera_list:", camera_list)
        torch.cuda.empty_cache()

        for camera_id in camera_list:
            print("="*80)
            print("Render is starting...")
            print("Camera Id: ", camera_id)
            print("Stream Path: ", config.setting.processing.source[str(camera_id)]["video_path"])
            start_async_person_counter_process(camera_id=str(camera_id))
            print("Render is started...")
            print("="*80)
             
        custom_logger.info(f"Camera started multi. Camera list: {camera_list}\n\n")

        return jsonify(
            {"status": True, "message": "started all camera"}   
        )

    except Exception as e:
        custom_logger.error("Error initializing multi the camera\n{e}", exc_info=True)

        return jsonify({"error": str(e)}), 500

@app.route("/api/camera/stop", methods=["POST"])
def camera_stop():
    try:
        request_data = request.get_json()
        camera_id = str(request_data.get("camera_id"))

        print(processes_dict)
        stop_async_person_counter_process(camera_id)
        print(processes_dict)
        custom_logger.info(f"Camera stopped. Camera id: {camera_id}\n\n")

        return jsonify({"status": True})
    except Exception as e:
        custom_logger.error("Error encountered when stopping the camera\n{e}", exc_info=True)

        return jsonify({"error": str(e)}), 500


@app.route("/api/camera/restart", methods=["POST"])
def camera_restart():
    try:
        request_data = request.get_json()
        camera_id = request_data.get("camera_id")

        torch.cuda.empty_cache()

        stop_async_person_counter_process(camera_id)
        start_async_person_counter_process(camera_id=camera_id)
        custom_logger.info(f"Camera restarted. Camera id: {camera_id}\n\n")


        return jsonify({"status": True, "message": f"{camera_id} process restarted"})

    except Exception as e:

        custom_logger.error("Error encountered while restarting the camera\n{e}", exc_info=True)

        return jsonify({"error": str(e)}), 500
