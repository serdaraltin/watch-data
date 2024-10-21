import os
import json

# os.environ["VARIABLE"]="value"

FRESH_CONFIG = {
    "setting": {
        "debug": {"mode": False, "camera_view": False},
        "device": "gpu",
        "network": {
            "host": "localhost",
            "port": 5000,
            "cors": ["*"],
            "backend": {"host": "localhost", "port": 3000},
        },
        "model": {
            
                "name": "yolov8n",
                "type": "pt"
            },
        "processing": {
            "source": [],
            "repeated_time": 300,
            "topic_reload_time": {"hour": 0, "minute": 0},
            "gc_clean_time": 60,
            "threshold_time_default": 5,
        },
    }
}


class Preset(object):
    preset = {
        "response_types": {"info": 0, "error": 1, "warning": 2},
        "folder": {
            "config": "config/json",
            "log": "logs",
            "model": "model_path",
            "database": "database",
        },
        "file": {
            "config": "config.json",
            "sqlite": "data.sqlite"
        },
        "setting": {},
    }

    def __init__(self) -> None:
        self.file = self.File(self.preset["file"])
        self.folder = self.File(self.preset["folder"])

    def __repr__(self) -> str:
        return repr(self.preset)

    class File(object):
        def __init__(self, value):
            self.__dict__ = value

        def __repr__(self):
            return repr(self.__dict__)

    class Folder(object):
        def __init__(self, value):
            self.__dict__ = value

        def __repr__(self):
            return repr(self.__dict__)


preset = Preset()


class Config(object):
    CONFIG_PATH = os.path.join(preset.folder.config, preset.file.config)

    def dump(self, fresh_data):
        with open(self.CONFIG_PATH, "w") as outfile:
            outfile.write(json.dumps(self.__dict__, indent=4))
            outfile.close()

    def load(self):
        # Dosyanın var olup olmadığını kontrol et
        if not os.path.exists(self.CONFIG_PATH):
            self.dump(fresh_data=True)
            return FRESH_CONFIG

        # Dosyayı aç ve içeriğini kontrol et
        with open(self.CONFIG_PATH, "r") as openfile:
            content = openfile.read()
            if content == "":
                self.dump(fresh_data=True)
                return FRESH_CONFIG

        # JSON içeriğini yükle ve döndür
        with open(self.CONFIG_PATH, "r") as openfile:
            return json.load(openfile)

    def __init__(self):
        self.__dict__ = self.load()
        self.setting = self.Setting(self.__dict__["setting"])

    def __repr__(self):
        return repr(self.__dict__)

    class Setting(object):
        def __init__(self, value):
            self.__dict__ = value
            self.network = self.Network(self.__dict__["network"])
            self.model = self.Model(self.__dict__["model"])
            self.processing = self.Processing(self.__dict__["processing"])
            self.module = self.Module(self.__dict__["module"])
            self.schedule = self.Schedule(self.__dict__["schedule"])

        def __repr__(self):
            return repr(self.__dict__)
        class Module(object):
            def __init__(self, value):
                self.__dict__ = value
        class Network(object):
            def __init__(self, value):
                self.__dict__ = value
                self.backend = self.Backend(self.__dict__["backend"])
                self.database = self.Database(self.__dict__["database"])

            def __repr__(self):
                return repr(self.__dict__)

            class Backend(object):
                def __init__(self, value):
                    self.__dict__ = value

                def __repr__(self):
                    return repr(self.__dict__)

            class Database(object):
                def __init__(self, value):
                    self.__dict__ = value

                def __repr__(self):
                    return repr(self.__dict__)

        class Model(object):
            def __init__(self, value):
                self.__dict__ = value

            def __repr__(self):
                return repr(self.__dict__)

        class Processing(object):
            def __init__(self, value):
                self.__dict__ = value

            def __repr__(self):
                return repr(self.__dict__)
            
        class Schedule(object):
            def __init__(self, value):
                self.__dict__ = value

            def __repr__(self):
                return repr(self.__dict__)

config = Config()
