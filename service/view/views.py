from flask import request, jsonify, send_file, request
from app import app

import cv2
import pandas as pd
import psycopg2
import io
import os
import threading
import json

from services.camera.video_face_blur import VideoPersonBlur
from utils.export.create_pdf import data_preprocessing, create_rapor_pdf
from config import aws_config, database_config

from utils.aws.s3 import upload_to_s3
from utils.database.get_data import (
    get_data,
    get_data_as_dataframe,
    get_camera_as_dataframe,
    get_data_as_dataframe_from_camera,
    get_branch_by_id
    
    )
from utils import get_current_customer_data, get_current_gender_data, get_hourly_customer_counts, get_hourly_gender_counts

import datetime

request_lock = threading.Lock()
model_path = "services/camera/model/yolov8m.pt"

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', '*')
  response.headers.add('Access-Control-Allow-Methods', '*')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

def get_df(branch_id,between):
    
    data = get_data_as_dataframe(branch_id=branch_id, between=between)

    data_json = data.T.to_dict()

    return data, data_json


#DATA OPERATION ==========================================
@app.route('/api/data/current_customer/all', methods=["POST"])
def get_current_customer_all():

    request_data = request.get_json()
    branch_id=request_data["branch_id"]
    #camera_id=request_data["camera_id"]
    camera_id = 6
    between=request_data["between"]
    
    data = get_data_as_dataframe_from_camera(branch_id,between,camera_id)
      

    #data, data_json = get_df(branch_id,between)
    value_counts = data['event_type'].value_counts()
    current_customer = value_counts.get('enter', 0) #- value_counts.get('exit', 0)

    return jsonify({
        "status": True,
        "message":{
            "current_customer":  int(current_customer)
        }
        })
    
@app.route('/api/data/current_customer', methods=["POST"])
def get_current_customer():

    request_data = request.get_json()
    branch_id=request_data["branch_id"]
    camera_id=request_data["camera_id"]
    between=request_data["between"]
    
    data = get_data_as_dataframe_from_camera(branch_id,between,camera_id)
    
    value_counts = data['event_type'].value_counts()
    current_customer = value_counts.get('enter', 0) #- value_counts.get('exit', 0)

    return jsonify({
        "status": True,
        "message":{
            "current_customer":  int(current_customer)
        }
        })

@app.route('/api/data/current_gender/all', methods=["POST"])
def get_current_gender_all():

    request_data = request.get_json()
    branch_id=request_data["branch_id"]
    between=request_data["between"]
    
    camera_id = 6


    # data, data_json = get_df(branch_id,between)

    data = get_data_as_dataframe_from_camera(branch_id,between,camera_id)

    male_data = data[data["gender"] == "male"]
    male_couts = male_data['event_type'].value_counts()


    female_data = data[data["gender"] == "female"]
    female_couts = female_data['event_type'].value_counts()

    print("="*80)
    print("Male")
    print(male_couts)
    print("Female")
    print(female_couts)
    print("="*80)


    current_male = male_couts.get('enter', 0) #- male_couts.get('exit', 0)
    current_female = female_couts.get('enter', 0) #- female_couts.get('exit', 0)
    return jsonify({
        "status": True,
        "message":{
            "current_male": int(current_male) ,
            "current_female": int(current_female),
            
        }
        })
    
@app.route('/api/data/current_gender', methods=["POST"])
def get_current_gender():

    request_data = request.get_json()
    branch_id=request_data["branch_id"]
    camera_id=request_data["camera_id"]
    between=request_data["between"]
    
    data = get_data_as_dataframe_from_camera(branch_id,between,camera_id)
   
    male_data = data[data["gender"] == "male"]
    male_couts = male_data['event_type'].value_counts()


    female_data = data[data["gender"] == "female"]
    female_couts = female_data['event_type'].value_counts()

    print("="*80)
    print("Male")
    print(male_couts)
    print("Female")
    print(female_couts)
    print("="*80)


    current_male = male_couts.get('enter', 0) #- male_couts.get('exit', 0)
    current_female = female_couts.get('enter', 0) #- female_couts.get('exit', 0)
    return jsonify({
        "status": True,
        "message":{
            "current_male": int(current_male) ,
            "current_female": int(current_female),
            
        }
        })

@app.route('/api/data/hourly_gender/all', methods=["POST"])
def get_current_hourly_gender_all():

    request_data = request.get_json()
    branch_id=request_data["branch_id"]
    day=request_data["day"]
    working_hours=request_data["working_hours"]
    
    day_time = datetime.datetime.strptime(day, '%Y-%m-%d').date()
    day_time= datetime.datetime.combine(day_time, datetime.datetime.min.time())
    
    between = {
        "start_date": day_time,
        "end_date": day_time + datetime.timedelta(hours=23)
        }
  
    data, data_json = get_df(branch_id,between)
   

    data["detection_time"] = pd.to_datetime(data["detection_time"])
    data["hourly"] = data["detection_time"].dt.hour
   

    male_data = data[(data["gender"] == "male") & (data["event_type"] == "enter")]
    female_data = data[(data["gender"] == "female") & (data["event_type"] == "enter")]

    female_couts = female_data['hourly'].value_counts()
    male_couts = male_data['hourly'].value_counts()

    male_dict = male_couts.to_dict()
    female_dict = female_couts.to_dict()

    hourly_dict_female = {f"{hour:02d}:00": 0 for hour in range(working_hours[0],working_hours[1])}
    hourly_dict_male = {f"{hour:02d}:00": 0 for hour in range(working_hours[0],working_hours[1])}
  
    hourly_list = [f"{hour:02d}:00" for hour in range(working_hours[0],working_hours[1])]

    for i in male_dict:
        hourly_dict_male[f"{i:02d}:00"] = male_dict[i]
    for i in female_dict:
        hourly_dict_female[f"{i:02d}:00"] = female_dict[i]

    males = list()
    for i in hourly_list:
        males.append({"time_label": i, "count": hourly_dict_male[i]})
    females = list()
    for i in hourly_list:
        females.append({"hour": i, "count": hourly_dict_female[i]})





    print("="*70)
    print(males)
    return jsonify({
        "status": True,
        "message":{
            "male": males,
            "female": females
        }
        })
    
    
@app.route('/api/data/hourly_gender', methods=["POST"])
def get_current_hourly_gender():

    request_data = request.get_json()
    branch_id=request_data["branch_id"]
    camera_id=request_data["camera_id"]
    
    day=request_data["day"]
    working_hours=request_data["working_hours"]
    
    day_time = datetime.datetime.strptime(day, '%Y-%m-%d').date()
    day_time= datetime.datetime.combine(day_time, datetime.datetime.min.time())
    
    between = {
        "start_date": day_time,
        "end_date": day_time + datetime.timedelta(hours=23)
        }
  
    data = get_data_as_dataframe_from_camera(branch_id,between,camera_id)
   

    data["detection_time"] = pd.to_datetime(data["detection_time"])
    data["hourly"] = data["detection_time"].dt.hour
   

    male_data = data[(data["gender"] == "male") & (data["event_type"] == "enter")]
    female_data = data[(data["gender"] == "female") & (data["event_type"] == "enter")]

    female_couts = female_data['hourly'].value_counts()
    male_couts = male_data['hourly'].value_counts()

    male_dict = male_couts.to_dict()
    female_dict = female_couts.to_dict()

    hourly_dict_female = {f"{hour:02d}:00": 0 for hour in range(working_hours[0],working_hours[1])}
    hourly_dict_male = {f"{hour:02d}:00": 0 for hour in range(working_hours[0],working_hours[1])}

  
    hourly_list = [f"{hour:02d}:00" for hour in range(working_hours[0],working_hours[1])]

    for i in male_dict:
        hourly_dict_male[f"{i:02d}:00"] = male_dict[i]
    for i in female_dict:
        hourly_dict_female[f"{i:02d}:00"] = female_dict[i]

    males = list()
    for i in hourly_list:
        males.append({"time_label": i, "count": hourly_dict_male[i]})
    females = list()
    for i in hourly_list:
        females.append({"time_label": i, "count": hourly_dict_female[i]})





    print("="*70)
    print(males)
    return jsonify({
        "status": True,
        "message":{
            "male": males,
            "female": females
        }
        })
    
@app.route('/api/data/hourly_customer/all', methods=["POST"])
def get_current_hourly_customer_all():

    request_data = request.get_json()
    branch_id=request_data["branch_id"]
    day=request_data["day"]
    working_hours=request_data["working_hours"]
    
    day_time = datetime.datetime.strptime(day, '%Y-%m-%d').date()
    between = {
        "start_date": day_time,
        "end_date": day_time + datetime.timedelta(hours=24)
        }

    data, data_json = get_df(branch_id,between)
   

    data["detection_time"] = pd.to_datetime(data["detection_time"])
    data["hourly"] = data["detection_time"].dt.hour
   

    enter_data = data[data["event_type"] == "enter"]

    enter_counts = enter_data['hourly'].value_counts()

    enter_dict = enter_counts.to_dict()

    hourly_dict = {f"{hour:02d}:00": 0 for hour in range(working_hours[0],working_hours[1])}



    for i in enter_dict:
        hourly_dict[f"{i:02d}:00"] = enter_dict[i]
   

    hourly_list = [f"{hour:02d}:00" for hour in range(working_hours[0],working_hours[1])]


    hourly_customer = list()
    for i in hourly_list:
        hourly_customer.append({"time_label": i, "count": hourly_dict[i]})
   

    return jsonify({
        "status": True,
        "message":{
           "hourly_customer": hourly_customer
        }
        })
    
@app.route('/api/data/hourly_customer', methods=["POST"])
def get_current_hourly_customer():

    request_data = request.get_json()
    branch_id=request_data["branch_id"]
    camera_id=request_data["camera_id"]
    
    day=request_data["day"]
    working_hours=request_data["working_hours"]
    
    day_time = datetime.datetime.strptime(day, '%Y-%m-%d').date()
    between = {
        "start_date": day_time,
        "end_date": day_time + datetime.timedelta(hours=24)
        }

    data = get_data_as_dataframe_from_camera(branch_id,between, camera_id)
   

    data["detection_time"] = pd.to_datetime(data["detection_time"])
    data["hourly"] = data["detection_time"].dt.hour
   

    enter_data = data[data["event_type"] == "enter"]

    enter_counts = enter_data['hourly'].value_counts()

    enter_dict = enter_counts.to_dict()

    hourly_dict = {f"{hour:02d}:00": 0 for hour in range(working_hours[0],working_hours[1])}



    for i in enter_dict:
        hourly_dict[f"{i:02d}:00"] = enter_dict[i]
   

    hourly_list = [f"{hour:02d}:00" for hour in range(working_hours[0],working_hours[1])]


    hourly_customer = list()
    for i in hourly_list:
        hourly_customer.append({"time_label": i, "count": hourly_dict[i]})
   

    return jsonify({
        "status": True,
        "message":{
           "hourly_customer": hourly_customer
        }
        })
# ========================================================


# CAMERA OPERATION =======================================
@app.route("/api/camera/blur/", methods=["POST"])
def camera_blur():
     with request_lock:
        video_blur = VideoPersonBlur(model_path)
        data = request.get_json()
        protocol = data.get("protocol")
        host = data.get("host")
        port = data.get("port")
        user = data.get("user")
        password = data.get("password")
        path = data.get("path")
        channel = data.get("channel")
        
        
        video_url = f"""{protocol.lower()}://{host}:{port}/user={user}&password={password}&channel={channel}&stream=0.sdp?"""
        video_url = f"""{protocol.lower()}://{user}:{password}{host}:{port}/{path}/{channel}"""
        print("="*60)
        print(video_url)
        print("="*60)

        blurred_image = video_blur.get_blur_image(video_url)
        _, img_encoded = cv2.imencode(".jpg", blurred_image)
        bytes_io = io.BytesIO(img_encoded.tobytes())

        bytes_io.seek(0)

        return send_file(
            bytes_io, mimetype="image/jpeg", as_attachment=True, download_name="result.jpg"
        )
    
@app.route('/api/camera/add', methods=["POST"])
def camera_add():
    try:
        request_data = request.get_json()

        conn = psycopg2.connect(
            host=database_config.host,
            port=database_config.port,
            dbname=database_config.database,
            user=database_config.user,
            password=database_config.password,
        )

        cur = conn.cursor()

        sql = """
            INSERT INTO "Camera" (
                branch_id,
                channel,
                "createdAt",
                host,
                install_date,
                label,
                model,
                password,
                path,
                port,
                protocol,
                resolution,
                status,
                type,
                "user"
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id;
        """

        values = (
            request_data["branch_id"],
            request_data["channel"],
            request_data["createdAt"],
            request_data["host"],
            request_data["install_date"],
            request_data["label"],
            request_data["model"],
            request_data["password"],
            request_data["path"],
            request_data["port"],
            request_data["protocol"],
            request_data["resolution"],
            request_data["status"],
            request_data["type"],
            request_data["user"],
        )

        cur.execute(sql, values)
        new_id = cur.fetchone()[0]  # Yeni eklenen kaydın ID'sini al

        conn.commit()

        cur.close()
        conn.close()

        return jsonify({"status": True, "message": {"camera_id": new_id}})

    except Exception as e:
        # Hata mesajını string olarak dönüştür
        return jsonify({"status": False, "message": str(e)})

@app.route('/api/camera/update', methods=["POST"])
def camera_update():
    pass

@app.route('/api/camera/delete', methods=["POST"])
def camera_delete():
    pass

@app.route('/api/camera/list', methods=["POST"])
def camera_list():
    request_data = request.get_json()
    branch_id=request_data["branch_id"]
    
    data = get_camera_as_dataframe(branch_id=branch_id)

    data_json = data.T.to_dict()

    camera_list = [data_json[i] for i in data_json]
   
    return jsonify({
        "status": True,
        "message":{
            "cameras":  camera_list
        }
        })
# ========================================================


# EXPORT OPERATION =======================================
@app.route("/api/export/csv", methods=["POST"])
def export_csv():


    if not request.json:
        return jsonify({"error": "No JSON data provided"}), 400

    data = request.json
    branch_id=data["branch_id"]
    between=data["between"]
    

    if "branch_id" not in data or "between" not in data:
        return jsonify({"error": "Missing branch_id or date range"}), 400
    try:
        start_date = between["start_date"]
        end_date = between["end_date"]

        start_date_dt = datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S.%f+00")
        start_date_dt = start_date_dt.strftime("%Y-%m-%d")

        end_date_dt = datetime.datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S.%f+00")
        end_date_dt = end_date_dt.strftime("%Y-%m-%d")

        branch_name = get_branch_by_id(branch_id)

        file_name = f"{branch_name['name']}_{start_date_dt}B{end_date_dt}".replace(' ','_')

        file_path =  f"""reports/csv/{file_name}.csv"""

        rows_exported, row_length, s3_url = get_data(
            branch_id=data["branch_id"],
            between=data["between"],
            object_name=file_path
        )

        if rows_exported == 0:
            result = {
                "branch_id": data["branch_id"],
                "modules": data.get("modules", []),
                "between": data["between"],
                "status": "no data found",
            }
            return jsonify(result), 404
        else:
            result = {
                "branch_id": data["branch_id"],
                "modules": data.get("modules", []),
                "between": data["between"],
                "status": "success",
                "file_size": rows_exported,
                "row_length": row_length,
                "url": s3_url,
            }
            return jsonify(result), 200
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500
    except KeyError as e:
        return jsonify({"error": f"Missing key in 'between': {str(e)}"}), 400
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred"}), 500
  
@app.route('/api/export/pdf', methods=["POST"])
def export_pdf():

    request_data = request.get_json()
    branch_id=request_data["branch_id"]
    between=request_data["between"]

    start_date = between["start_date"]
    end_date = between["end_date"]

    start_date_dt = datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S.%f+00")
    start_date_dt = start_date_dt.strftime("%Y-%m-%d")

    end_date_dt = datetime.datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S.%f+00")
    end_date_dt = end_date_dt.strftime("%Y-%m-%d")

    branch_name = get_branch_by_id(branch_id)

    file_name = f"{branch_name['name']}_{start_date_dt}B{end_date_dt}".replace(' ','_')

    file_path =  f"""reports/pdf/{file_name}.pdf"""

    df_data = get_data_as_dataframe(
        branch_id=branch_id,
        between=between
    )

    df_data = data_preprocessing(df_data)
    branch_name = get_branch_by_id(branch_id)
    pdf_byte_stream = create_rapor_pdf(df_data, branch_name["name"])

    pdf_bytes = pdf_byte_stream.getvalue()

    try:
        presigned_url = upload_to_s3(file_path, pdf_bytes)
        return jsonify({'message': 'PDF uploaded successfully.', 'url': presigned_url})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
#! ========================================================
#! ========================================================
#! ========================================================
    

@app.route('/api/data/get_data_by_branch_id', methods=["POST"])
def get_data_by_branch_id():

    try:

        request_data = request.get_json()
        branch_id=request_data["branch_id"]
        day=request_data["day"]
        working_hours=request_data["working_hours"]

        day_time = datetime.datetime.strptime(day, '%Y-%m-%d').date()
        day_time= datetime.datetime.combine(day_time, datetime.datetime.min.time())

        between = {
                "start_date": day_time,
                "end_date": day_time + datetime.timedelta(hours=23)
                }


        data, data_json = get_df(branch_id,between)
        if not len(data):
            return jsonify({"status": False, "message": "Data not found"})
        
        data = data[data["event_type"] == "enter"]


        camera_ids = list(set(data["camera_id"]))

        cameras = list()

        for id_ in camera_ids:

            current_data = data[data["camera_id"] == id_]
            data_gender = get_current_gender_data(current_data)
            cameras.append(
                {
                "id": str(id_),
                "current_customer": get_current_customer_data(current_data),
                "current_female": data_gender["current_female"],
                "current_male": data_gender["current_male"],
                "hourly_customer": get_hourly_customer_counts(current_data, working_hours),
                "hourly_gender": get_hourly_gender_counts(current_data, working_hours)
            }
            )

        data_gender = get_current_gender_data(data)

        json_data = {
            "cameras": cameras,
            "total": {

                "current_customer": get_current_customer_data(data),
                "current_female": data_gender["current_female"],
                "current_male": data_gender["current_male"],
                "hourly_customer": get_hourly_customer_counts(data, working_hours),
                "hourly_gender": get_hourly_gender_counts(data, working_hours)

            }
        }


        return jsonify({
            "status": True,
            "message":{
                "data": json_data
            }
        })
    
    except Exception as e:
        return jsonify({"status": False, "message": str(e)})



@app.route('/api/data/get_between_data_by_branch_id', methods=["POST"])
def get_between_data_by_branch_id():

    try:
        request_data = request.get_json()
        branch_id=request_data["branch_id"]
        between = request_data["between"]

        data, data_json = get_df(branch_id, between)

        if not len(data):
            return jsonify({"status": False, "message": "Data not found"})


        data = data[data["event_type"] == "enter"]
        data.loc[:, "detection_time"] = pd.to_datetime(data["detection_time"])
        data['date'] = data['detection_time'].dt.strftime('%Y-%m-%d')

        dates = list(set(data["date"]))


        data_list = list()
        for date in dates:
            current_data = data[data["date"] == date]
            current_gender = get_current_gender_data(current_data)
            data_list.append({
                "date": date,
                "total_male": current_gender["current_male"],
                "total_female": current_gender["current_female"],
                "total_customer": get_current_customer_data(current_data)
            })
        


        return jsonify({
            "status": True,
            "message":{
                "data": data_list
            }
        })
 
    except Exception as e:
        return jsonify({"status": False, "message": str(e)})


    
























