import sys
import os

# Damit Python  das Hauptverzeichnis findet
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from system_status import check_system

def test_system_status_exists():
    """Prüft, ob die Funktion check_system fehlerfrei importiert werden kann."""
    assert callable(check_system), "check_system muss eine ausführbare Funktion sein."

def test_check_system_runs():
    """Führt die Systemprüfung im Test-Modus aus (ohne Log-Datei zu schreiben)."""
    try:
        check_system(log_to_file=False)
    except Exception as e:
        assert False, f"check_system ist mit einem Fehler fehlgeschlagen: {e}"
