import sys
import os

# Damit Python das Hauptverzeichnis findet
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from system_status import check_system

def test_system_status_exists():
    """Prüft, ob die Funktion check_system fehlerfrei importiert werden kann und existiert."""
    assert callable(check_system), "check_system muss eine ausführbare Funktion sein."
  
