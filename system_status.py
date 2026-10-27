import sys
import platform
from datetime import datetime

def check_system(log_to_file=False):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status_info = (
        f"[{timestamp}] Grenzstein-Protokoll: System-Status\n"
        f"Python-Version: {sys.version.split()[0]}\n"
        f"Betriebssystem: {platform.system()} {platform.release()}\n"
        f"Status: Systemkern intakt und einsatzbereit.\n"
        f"----------------------------------------\n"
    )
    
    print(status_info)
    
    if log_to_file:
        with open("system.log", "a", encoding="utf-8") as f:
            f.write(status_info)
        print("Status erfolgreich in 'system.log' geschrieben.")

if __name__ == "__main__":
    check_system(log_to_file=True)
