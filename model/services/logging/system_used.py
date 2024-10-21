import psutil
import GPUtil
import threading
import datetime
#unused
def log_system_usage(interval=600):  # 10 dakika = 600 saniye
    print("--- System Used Started -------------")
    while True:
        # CPU ve Bellek kullanımını al
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent

        # GPU kullanımını al (Eğer mevcutsa)
        gpus = GPUtil.getGPUs()
        gpu_usage = [gpu.load * 100 for gpu in gpus] if gpus else "No GPU"

        # Şu anki zamanı al
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Kullanım bilgilerini bir dosyaya yaz (Örneğin: system_usage_log.txt)
        with open("system_usage_log.txt", "a") as file:
            file.write(f"{current_time}, CPU: {cpu_usage}%, Memory: {memory_usage}%, GPU: {gpu_usage}\n")

        # Belirlenen aralıkta bekle
        threading.Timer(interval, log_system_usage).start()


