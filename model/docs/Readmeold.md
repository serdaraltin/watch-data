
# Configuration System Usage
Explain how users can effectively use your project. Provide detailed examples or a quick start guide.

## e.g. Access the database path

```python
  from config import preset
  database_path = preset.folder.database
  print(f"Database path: {database_path}")
```

## Configuration
Describe the configuration options and how users can customize the settings.

## Preset Configuration
Explain how users can customize the Preset class.

## Config Configuration
Explain how users can customize the Config class.



# Kafka yı başlatmak için 

Gereksinimler
```
sudo apt install default-jre
sudo apt install default-jdk
```

```bash
cd kafka_topic/kafka_2.12-3.6.0

```
1. **Zookeeper'ı Başlatın: Kafka dizinindeki bin klasörüne gidin ve aşağıdaki komutu çalıştırın (Windows için .bat, Linux/Mac için .sh uzantısını kullanın):** (Gerekli)
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties

```


2. **Yeni bir Terminal Penceresinde Kafka Server'ını Başlatın: Zookeeper çalışırken, yeni bir terminal penceresi açın ve Kafka server'ını başlatmak için aşağıdaki komutu çalıştırın:** (Gerekli)

```bash
bin/kafka-server-start.sh config/server.properties

```
3. **Kafka Topic Oluşturma Kafka üzerinde iletişim kurmak için bir topic (konu) oluşturmanız gerekecek:**

**Topic Oluşturun: Kafka topic'lerini oluşturmak için aşağıdaki komutu kullanabilirsiniz:** (Opsiyonel)


```bash
bin/kafka-topics.sh --create --topic your_topic_name --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1


```


topic silme
```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic your_topic_name


```


# API çalıştırma

```
cd ..
cd ..

pip install -r requirements.txt

```
API çalıştırma

```
python3 app.py

```


# URL Config
```
watch-data-model/
├── api/
│   ├──config.py

# Sadece tek bir url var. veri tabanına veri yazdırmak için.
```




# Process başlatma (POST)
```
http://100.90.105.68:5000/api/process-video
```
```json
{
    "video_path": "data/9_2.mp4",
    "point_data":{
            "points":  [[472, 352], [698, 352]],
            "threshold_time": 5,
            "enter_direction": [0, 1]
              
        }
    ,
    "user_data": {
      "userId": 1,
      "branchID": 1,
      "processID": 1
    }
}

```

# Process listeleme (GET)

```
http://100.90.105.68:5000/api/get-process-list
```

# Process silme (DELETE)

```
http://100.90.105.68:5000/api/delete-process/1

```


