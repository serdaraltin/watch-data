import os
import json


base_folder_path = os.path.join("config", "jsons")
# base_folder_path = "jsons"

aws_file_path = "aws.json"
database_file_path = "database.json"

FRESH_CONFIG = {

}

class AWSConfig(object):
    CONFIG_PATH = os.path.join(base_folder_path, aws_file_path)

    def dump(self, fresh_data):
        with open(self.CONFIG_PATH, "w") as outfile:
            outfile.write(json.dumps(self.__dict__, indent=4))
            outfile.close()

    def load(self):
        # # Dosyanın var olup olmadığını kontrol et
        # if not os.path.exists(self.CONFIG_PATH):
        #     self.dump(fresh_data=True)
        #     return FRESH_CONFIG

        # # Dosyayı aç ve içeriğini kontrol et
        # with open(self.CONFIG_PATH, "r") as openfile:
        #     content = openfile.read()
        #     if content == "":
        #         self.dump(fresh_data=True)
        #         return FRESH_CONFIG

        # JSON içeriğini yükle ve döndür
        with open(self.CONFIG_PATH, "r") as openfile:
            return json.load(openfile)

    def __init__(self):
        self.__dict__ = self.load()

    def __repr__(self):
        return repr(self.__dict__)
    


class DatabaseConfig(object):
    CONFIG_PATH = os.path.join(base_folder_path, database_file_path)

    def dump(self, fresh_data):
        with open(self.CONFIG_PATH, "w") as outfile:
            outfile.write(json.dumps(self.__dict__, indent=4))
            outfile.close()

    def load(self):
        # # Dosyanın var olup olmadığını kontrol et
        # if not os.path.exists(self.CONFIG_PATH):
        #     self.dump(fresh_data=True)
        #     return FRESH_CONFIG

        # # Dosyayı aç ve içeriğini kontrol et
        # with open(self.CONFIG_PATH, "r") as openfile:
        #     content = openfile.read()
        #     if content == "":
        #         self.dump(fresh_data=True)
        #         return FRESH_CONFIG

        # JSON içeriğini yükle ve döndür
        with open(self.CONFIG_PATH, "r") as openfile:
            return json.load(openfile)

    def __init__(self):
        self.__dict__ = self.load()

    def __repr__(self):
        return repr(self.__dict__)
    



    

aws_config = AWSConfig()
database_config = DatabaseConfig()