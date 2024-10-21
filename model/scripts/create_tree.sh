#!/bin/bash

# Fonksiyon: Belirtilen dizini oluşturur
create_directory() {
    if [ ! -d "$1" ]; then
        mkdir -p "$1"
        echo "Created directory: $1"
    fi
}

# Proje kök dizini
project_root="watch-data"

# Temel klasörleri oluştur
create_directory "$project_root"
create_directory "$project_root/app"
create_directory "$project_root/camera"
create_directory "$project_root/config"
create_directory "$project_root/database"
create_directory "$project_root/doc"
create_directory "$project_root/image_processing"
create_directory "$project_root/interfaces"
create_directory "$project_root/logs"
create_directory "$project_root/middleware"
create_directory "$project_root/models"
create_directory "$project_root/routes"
create_directory "$project_root/scripts"
create_directory "$project_root/services"
create_directory "$project_root/static"
create_directory "$project_root/templates"
create_directory "$project_root/tests"
create_directory "$project_root/tools"
create_directory "$project_root/utils"

# doc klasörü içindeki dosyaları oluştur
touch "$project_root/doc/__init__.py"
touch "$project_root/doc/config.example.json"
touch "$project_root/doc/general.todo"
touch "$project_root/doc/Readme.md"
touch "$project_root/doc/requirements.txt"
touch "$project_root/doc/Structure.md"

# app klasörü içindeki dosyaları oluştur
touch "$project_root/app/__init__.py"
touch "$project_root/app/main.py"

# camera klasörü içindeki dosyaları oluştur
create_directory "$project_root/camera/camera_data"
create_directory "$project_root/camera/camera_data/camera_templates"
touch "$project_root/camera/__init__.py"
touch "$project_root/camera/camera_manager.py"
touch "$project_root/camera/camera_processor.py"
touch "$project_root/camera/camera_data/__init__.py"
touch "$project_root/camera/camera_data/camera.py"
touch "$project_root/camera/camera_data/camera_templates/__init__.py"

# config klasörü içindeki dosyaları oluştur
create_directory "$project_root/config/config_templates"
touch "$project_root/config/__init__.py"
touch "$project_root/config/config.json"
touch "$project_root/config/config_manager.py"
touch "$project_root/config/config_templates/__init__.py"

# database klasörü içindeki dosyaları oluştur
create_directory "$project_root/database/migrations"
touch "$project_root/database/__init__.py"
touch "$project_root/database/db_connector.py"
touch "$project_root/database/models.py"
touch "$project_root/database/migrations/__init__.py"

# image_processing klasörü içindeki dosyaları oluştur
touch "$project_root/image_processing/__init__.py"
touch "$project_root/image_processing/counter.py"
touch "$project_root/image_processing/face_blur.py"
touch "$project_root/image_processing/utils.py"

# interfaces klasörü içindeki dosyaları oluştur
touch "$project_root/interfaces/__init__.py"
touch "$project_root/interfaces/web_interface.py"

# logs klasörü içindeki dosyaları oluştur
touch "$project_root/logs/__init__.py"
touch "$project_root/logs/app.log"

# middleware klasörü içindeki dosyaları oluştur
touch "$project_root/middleware/__init__.py"
touch "$project_root/middleware/authentication.py"

# models klasörü içindeki dosyaları oluştur
touch "$project_root/models/__init__.py"
touch "$project_root/models/camera_data.py"
touch "$project_root/models/user_data.py"

# routes klasörü içindeki dosyaları oluştur
touch "$project_root/routes/__init__.py"
touch "$project_root/routes/api_routes.py"

# scripts klasörü içindeki dosyaları oluştur
touch "$project_root/scripts/__init__.py"

# services klasörü içindeki dosyaları oluştur
touch "$project_root/services/__init__.py"
touch "$project_root/services/data_logger.py"
touch "$project_root/services/image_processor_service.py"
touch "$project_root/services/webcam_service.py"

# static ve templates klasörlerini oluştur (web uygulaması için)
create_directory "$project_root/static"
create_directory "$project_root/templates"

# tests klasörü içindeki dosyaları oluştur
create_directory "$project_root/tests/__pycache__"
touch "$project_root/tests/__init__.py"
touch "$project_root/tests/test_camera.py"
touch "$project_root/tests/test_config.py"
touch "$project_root/tests/test_database.py"
touch "$project_root/tests/test_image_processing.py"
touch "$project_root/tests/test_services.py"
touch "$project_root/tests/test_web_interface.py"

# tools klasörü içindeki dosyaları oluştur
touch "$project_root/tools/__init__.py"

# utils klasörü içindeki dosyaları oluştur
touch "$project_root/utils/__init__.py"
touch "$project_root/utils/common_utils.py"

echo "Project structure created successfully."
