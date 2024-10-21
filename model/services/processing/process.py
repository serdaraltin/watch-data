from image_processing.counter import PersonCount
from services import config,preset
from os import path


MODEL_PATH= path.join(preset.folder.model, (config.setting.model.name+"."+config.setting.model.type))


def run_process(video_path:str, point_data:dict, user_data: dict):

    
    line_start = point_data["points"][0]
    line_end = point_data["points"][1]
    threshold_time = point_data["threshold_time"]
    enter_direction = point_data["enter_direction"]

    person_count = PersonCount(line_start, line_end, threshold_time, MODEL_PATH, enter_direction, user_data)
    person_count.show_camera = True
    person_count.run(video_path)



