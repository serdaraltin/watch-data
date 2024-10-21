import logging
# from config.config import preset
import os

class LevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno == self.level

def get_custom_logger():
    # Özel bir logger oluştur
    custom_logger = logging.getLogger("custom")
    custom_logger.setLevel(logging.DEBUG)
    # LOG_PATH = preset.folder.log
    # LOG_PATH = "preset.folder.log"
    LOG_PATH = "logs"
    # Tüm log seviyelerini tutacak ana log dosyası
    main_handler = logging.FileHandler(os.path.join(LOG_PATH, 'main.log'))
    main_formatter = logging.Formatter('[%(asctime)s] [%(levelname)s]: %(message)s')
    main_handler.setFormatter(main_formatter)
    custom_logger.addHandler(main_handler)

    # Her log seviyesi için ayrı dosyalar oluştur
    log_levels = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    for level_name, level in log_levels.items():
        file_handler = logging.FileHandler(f'logs/{level_name}.log')
        file_handler.setLevel(level)
        file_handler.setFormatter(main_formatter)
        file_handler.addFilter(LevelFilter(level))
        custom_logger.addHandler(file_handler)

    return custom_logger



custom_logger = get_custom_logger()

