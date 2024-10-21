from flask import Flask
from flask_cors import CORS
from .garbage_collection import  run_gc_collect
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from config.config import config, preset
import os

app = Flask(__name__)
cors = CORS(app)



# LOG
logging.basicConfig(
    filename= os.path.join(preset.folder.log, "log.log"),
    level=logging.DEBUG,
    format="[%(asctime)s] [%(levelname)s]: %(message)s",
)


#APScheduler'ı başlat
scheduler = BackgroundScheduler()

scheduler.add_job(
    run_gc_collect, "interval", minutes=config.setting.processing.gc_clean_time
)
# scheduler.add_job(manage_kafka_topic, 'interval',  minutes=1)
scheduler.start()

process_dict = dict()
process_list = list()


# from .system_used import log_system_usage
# log_system_usage()

from flask.views import *
