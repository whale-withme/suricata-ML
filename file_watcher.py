from watchdog.observers import Observer  
from watchdog.events import FileSystemEventHandler
import time  
  
class MyHandler(FileSystemEventHandler):  
    def on_modified(self, event):  
        if event.is_directory:  
            return None  
  
        elif event.src_path.endswith("/var/log/suricata/eve.json"):  
            print(f'hey hey hey, {event.src_path} has been modified!')  
  
if __name__ == "__main__":  
    path = "."  # 当前目录，你可以改为任何你想要监控的目录  
    event_handler = MyHandler()  
    observer = Observer()  
    observer.schedule(event_handler, path, recursive=True)  
    observer.start()  
  
    try:  
        while True:  
            time.sleep(1)  
    except KeyboardInterrupt:  
        observer.stop()  
    observer.join()