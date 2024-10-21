import os
from ultralytics import YOLO
import socket
import requests
import time
import psycopg2
from config import preset, config
# info: 0, warning: 2, error: 1

# - izin kontrolleri
# - path kontrolu

class Checker:
    def __init__(self):
        self.file_system = self.File_System()
        self.image_processing = self.Image_Processing(self)
        self.camera = self.Camera()
        self.localization = self.Localization()
        self.network = self.Network()
        self.database = self.Database()

    def __repr__(self) -> str:
        return "Cheker()"

    class File_System:
        
        # Belirlenen dosyanin varilgini kontrol edip, `create` parametresine gore olusturur.
        def check_file(self, file_path: str, create: bool = False) -> dict:
            try:
                if os.path.isfile(file_path):
                    return {"type": 0, "message": f"File already exists: {file_path}"}

                else:
                    if create:
                        with open(file_path, "w") as file:
                            return {"type": 0, "message": f"File created: {file_path}"}
                    else:
                        return {
                            "type": 0,
                            "message": f"File not found and not created: {file_path}",
                        }

            except PermissionError:
                return {"type": 1, "message": f"Permission denied: {file_path}"}
            except Exception as e:
                return {"type": 1, "message": f"File in file operation: {e}"}

        # Belirlenen klasorun varligini kontrol eder, `create` parametresine gore olusturur.
        def check_folder(self, folder_path: str, create: bool = False) -> dict:
            try:
                if os.path.isdir(folder_path):
                    return {"type": 0, "message": f"Folder already exists: {folder_path}"}
                else:
                    if create:
                        os.makedirs(folder_path)
                        return {"type": 0, "message": f"Folder created: {folder_path}"}
                    else:
                        return {
                            "type": 0,
                            "message": f"Folder not found and not created: {folder_path}",
                        }
            except PermissionError:
                return {"type": 1, "message": f"Permission denied: {folder_path}"}

            except Exception as e:
                return {"type": 1, "message": f"Error in folder operation: {e}"}

        #
        def check_permissions(self, path: str) -> dict:
            try:
                permissions = {
                    "r": os.access(path, os.R_OK),
                    "w": os.access(path, os.W_OK),
                    "rw": os.access(path, os.R_OK) and os.access(path, os.W_OK)
                }
                return {"type": 0, "message": f"Permissions for '{path}'", "value":permissions}

            except Exception as e:
                return {"type": 1, "message": f"Error checking permissions for {path}: {e}"}

    #modelin varlık kontrolü, indirilmesi
    class Image_Processing:
        def __init__(self, parent):
            self.parent = parent
  
        def check_image_model(self) -> dict:
            folder_path = preset.folder.model
            file_name = config.setting.model.name
            file_type = config.setting.model.type

            model_path = os.path.join(folder_path, f"{file_name}.{file_type}")
            if file_type == "pt":
                if os.path.isdir(folder_path):
                    if os.path.isfile(model_path):
                        return {"type": 0, "message": f"File already exists: {model_path}"}
                    else:
                        YOLO(model_path)
                        return {"type": 0, "message": f"File created: {model_path}"}
                else:
                    os.makedirs(folder_path)
                    YOLO(model_path)
                    return {"type": 0, "message": f"File created: {model_path}"}
                
            elif file_type == "onnx":
                if os.path.isdir(folder_path):
                    if os.path.isfile(model_path):
                        return {"type": 0, "message": f"File already exists: {model_path}"}
                    else:
                        model = YOLO(os.path.join(folder_path, f"{file_name}.pt"))
                        model.export(format='onnx')
                        return {"type": 0, "message": f"File created: {model_path}"}
                else:
                    os.makedirs(folder_path)
                    model = YOLO(os.path.join(folder_path, f"{file_name}.pt"))
                    model.export(format='onnx')
                    return {"type": 0, "message": f"File created: {model_path}"}

    #port, database, cors
    class Network:
        # Belirli bir portun kullanılabilirliğini kontrol eder
        def check_port_availability(self, host: str, port: int) -> dict:
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.bind((host, port))
                    return {"type": 0, "message": f"Port {port} is available."}
                except socket.error as e:
                    return {"type": 1, "message": f"Port {port} is not available: {e}"}
                
        # Bir API'nin erişilebilirliğini kontrol eder.
        def check_api_accessibility(self, url: str) -> dict:
            
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    return {"type": 0, "message": f"API {url} is accessible."}
                else:
                    return {"type": 2, "message": f"API {url} is not accessible. Status Code: {response.status_code}"}
            except requests.RequestException as e:
                return {"type": 1, "message": f"Error accessing API {url}: {e}"}
    
    #ip, protokol
    class Camera:
        def check_ip_validity(self, ip: str) -> dict:
            """ Verilen IP adresinin geçerli olup olmadığını kontrolü """
            try:
                socket.inet_aton(ip)
                return {"type": 0, "message": f"Valid IP address: {ip}"}
            except socket.error:
                return {"type": 1, "message": f"Invalid IP address: {ip}"}
    
    #timezone
    class Localization:
        def check_system_timezone(self) -> dict:
            """ Sistemin zaman dilimini kontrolü """
            timezone = time.tzname
            return {"type": 0, "message": f"System timezone: {timezone}"}
    

    class Database:
        def __init__(self):

            self.host = config.setting.network.database.host
            self.database = config.setting.network.database.database
            self.user = config.setting.network.database.user
            self.password = config.setting.network.database.password



        # Veritabani baglantisini kontrol eder.
        def check_connection(self) -> dict:
         
            try:
                connection = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
                connection.close()
                return {"type": 0, "message": "Database connection successful."}
            except psycopg2.OperationalError as e:
                return {"type": 1, "message": f"Database connection failed: {e}"}
            except Exception as e:
                return {"type": 1, "message": f"Error in database operation: {e}"}
            
            
checker = Checker()