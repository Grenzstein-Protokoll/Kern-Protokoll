import sys
import platform

def check_system():
    print("--- Grenzstein-Protokoll: System-Status ---")
    print(f"Python-Version: {sys.version.split()[0]}")
    print(f"Betriebssystem: {platform.system()} {platform.release()}")
    print("Status: Systemkern intakt und einsatzbereit.")

if __name__ == "__main__":
    check_system()
  
