# from services import app
# import threading
# import multiprocessing
# from config.config_manager import config
# import os
# from pynput import keyboard
# import signal

# def run_app():
#     app.run(debug=False, host=config.setting.network.host, port=config.setting.network.port)

# def on_release(key):
#     if key == keyboard.KeyCode.from_char('q'):
#         print("Q pressed, terminating Kafka and Flask...")
#         os.kill(os.getpid(), signal.SIGKILL)  # Ana süreci sonlandır

# def on_press(key):
#     if key == keyboard.Key.esc:
#         return False  # Dinlemeyi sonlandırmak için


# if __name__ == "__main__":
#     try:
#         multiprocessing.set_start_method("spawn")
#     except Exception as e:
#         print("SPAWN Error ", e)

#      # Klavye dinleyicisini başlat
#     listener = keyboard.Listener(on_press=on_press, on_release=on_release)
#     listener.start()


#     # Flask uygulamasını ayrı bir thread üzerinde çalıştır
#     app_thread = threading.Thread(target=run_app)
#     app_thread.start()


