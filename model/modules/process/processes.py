from modules.detect.person.person import PersonCounter
from modules.detect.density.density import DensityTable
import threading
from app import processes_list, processes_dict
from multiprocessing import Process
from services.logging.logger import custom_logger


def person_counter_process(camera_id):
    try:
        counter = PersonCounter(camera_id=camera_id)
        counter.start()

        custom_logger.info("'person_counter_process' runnig")
    except Exception as e:
        custom_logger.error("'person_counter_process' error \n{e}", exc_info=True)


def start_async_person_counter_process(camera_id):
    try:
        p = Process(target=person_counter_process, args=(camera_id,))
        p.start()
        processes_dict[camera_id] = p
        custom_logger.info(f"'start_async_person_counter_process' started for camera_id={camera_id}")
    except Exception as e:
        custom_logger.error(f"'start_async_person_counter_process' error for camera_id={camera_id} \n{e}", exc_info=True)

def stop_async_person_counter_process(camera_id):
    try:
        if camera_id in processes_dict:
            processes_dict[camera_id].terminate() 
            processes_dict[camera_id].join()
            custom_logger.info(f"'stop_async_person_counter_process' stopped for camera_id={camera_id}")
        else:
            custom_logger.warning(f"'stop_async_person_counter_process': No process found for camera_id={camera_id}")
    except Exception as e:
        custom_logger.error(f"'stop_async_person_counter_process' error for camera_id={camera_id} \n{e}", exc_info=True)



def delete_async_person_counter_process(camera_id):
    try:
        if camera_id in processes_dict:
            processes_dict[camera_id].terminate()
            processes_dict[camera_id].join()
            del processes_dict[camera_id]
            custom_logger.info(f"'delete_async_person_counter_process' deleted for camera_id={camera_id}")
        else:
            custom_logger.warning(f"'delete_async_person_counter_process': No process found for camera_id={camera_id}")
    except Exception as e:
        custom_logger.error(f"'delete_async_person_counter_process' error for camera_id={camera_id} \n{e}", exc_info=True)

#####################################################################################################################################

def density_table_process(camera_id):
    try:
        counter = DensityTable(camera_id=camera_id)
        counter.start()

        custom_logger.info("'density_table_process' runnig")
    except Exception as e:
        custom_logger.error("'density_table_process' error \n{e}", exc_info=True)

def start_async_density_table_process(camera_id):
    try:
        t = Process(target=density_table_process, args=(camera_id,))
        t.start()
        processes_dict[camera_id] = t
        custom_logger.info(f"'start_async_person_counter_process' started for camera_id={camera_id}")
    except Exception as e:
        custom_logger.error(f"'start_async_person_counter_process' error for camera_id={camera_id} \n{e}", exc_info=True)

def stop_async_person_counter_process(camera_id):
    try:
        if camera_id in processes_dict:
            processes_dict[camera_id].terminate() 
            processes_dict[camera_id].join()
            custom_logger.info(f"'stop_async_person_counter_process' stopped for camera_id={camera_id}")
        else:
            custom_logger.warning(f"'stop_async_person_counter_process': No process found for camera_id={camera_id}")
    except Exception as e:
        custom_logger.error(f"'stop_async_person_counter_process' error for camera_id={camera_id} \n{e}", exc_info=True)



def delete_async_person_counter_process(camera_id):
    try:
        if camera_id in processes_dict:
            processes_dict[camera_id].terminate()
            processes_dict[camera_id].join()
            del processes_dict[camera_id]
            custom_logger.info(f"'delete_async_person_counter_process' deleted for camera_id={camera_id}")
        else:
            custom_logger.warning(f"'delete_async_person_counter_process': No process found for camera_id={camera_id}")
    except Exception as e:
        custom_logger.error(f"'delete_async_person_counter_process' error for camera_id={camera_id} \n{e}", exc_info=True)