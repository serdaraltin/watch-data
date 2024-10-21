from ..services import app, process_dict
from ..services.process import *
from flask import request, jsonify, send_file, request
from multiprocessing import Process
import io
import cv2
from datetime import datetime
from image_processing import VideoPersonBlur
import logging
from services.logging.logger import custom_logger
import os
from ...config.config_manager import config, preset

MODEL_PATH = os.path.join(
    preset.folder.model, (config.setting.model.name + "." + config.setting.model.type)
)


# Video işleme için process başlatır
@app.route("/api/process-video/", methods=["POST"])
def person_count_process():
    try:
        data = request.get_json()

        video_path = data.get("video_path")
        point_data = data.get("point_data")
        user_data = data.get("user_data")

        processID = user_data["processID"]
        userId = user_data["userId"]
        branchID = user_data["branchID"]

        if processID not in process_dict:
            process = Process(
                target=run_process, args=(video_path, point_data, user_data)
            )
            process.start()

            process_dict[processID] = {
                "process": process,
                "userId": userId,
                "branchID": branchID,
                "processID": processID,
                "created_data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }

            logging.info(f"Video processing started with data:\n{data}")
            custom_logger.info(f"Video processing started with data:\n{data}")

            return (
                jsonify({"status": "Processing video", "process_id": processID}),
                202,
            )
        else:
            logging.warning(f"Action has a name with data:\n{data}")
            custom_logger.warning(f"Action has a name with data:\n{data}")

            return jsonify({"status": "Action has a name"}), 404
    except Exception as e:
        logging.error(
            f"Error starting video processing\npost_data: {data}\n{e}", exc_info=True
        )
        custom_logger.error(
            f"Error starting video processing\npost_data: {data}\n{e}", exc_info=True
        )

        return jsonify({"error": str(e)}), 500


# Mevcut process'leri listeler
@app.route("/api/get-process-list/", methods=["GET"])
def get_process_list():
    try:
        process_list = [
            {
                "process_id": value["processID"],
                "user_id": value["userId"],
                "created_data": value["created_data"],
            }
            for key, value in process_dict.items()
        ]
        logging.info("Process list successfully retrieved")
        custom_logger.info("Process list successfully retrieved")

        return jsonify({"processes": process_list}), 200

    except Exception as e:
        logging.error(
            f"An error occurred while retrieving the process list\n{e}", exc_info=True
        )
        custom_logger.error(
            f"An error occurred while retrieving the process list\n{e}", exc_info=True
        )

        return jsonify({"error": str(e)}), 500


@app.route("/api/delete-process/<processID>", methods=["DELETE"])
def delete_process(processID):
    try:
        processID = int(processID)
        # Süreç sözlüğünde processID kontrol edilir
        if processID in process_dict:
            # Süreci sonlandır (bu kısım sürecinize bağlı olarak değişebilir)
            process = process_dict[processID]["process"]
            if process.is_alive():
                process.terminate()

            # Süreci sözlükten kaldır
            del process_dict[processID]

            logging.info(f"Process deleted, processID: {processID}")
            custom_logger.info(f"Process deleted, processID: {processID}")

            return jsonify({"status": "Process deleted", "process_id": processID}), 200
        else:
            logging.warning(f"Process not found processID: {processID}")
            custom_logger.warning(f"Process not found data: {processID}")

            return jsonify({"status": "Process not found"}), 404

    except Exception as e:
        logging.error(
            f"An error occurred while deleting the process.\nprocessID: {processID}\nprocess_dict:{process_dict}\n{e}",
            exc_info=True,
        )
        custom_logger.error(
            f"An error occurred while deleting the process.\nprocessID: {processID}\nprocess_dict:{process_dict}\n{e}",
            exc_info=True,
        )

        return jsonify({"error": str(e)}), 500

