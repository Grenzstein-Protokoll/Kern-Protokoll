from willkommen import zeige_begruessung
from system_status import check_system

def main():
    print("=== GRENZSTEIN-PROTOKOLL: START ==-\n")
    
    # 1. Begrüßung ausführen
    zeige_begruessung()
    
    print("\n--- Systemprüfung wird gestartet ---")
    
    # 2. Systemstatus prüfen und Log-Datei schreiben
    check_system(log_to_file=True)
    
    print("=== GRENZSTEIN-PROTOKOLL: ABGESCHLOSSEN ===")

if __name__ == "__main__":
    main()
