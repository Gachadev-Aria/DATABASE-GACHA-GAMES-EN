# Importations externes
import tkinter as tk
import sys
from pathlib import Path

# Importation interne
from app.API import API

sys.path.append(str(Path(__file__).parent))

# Point d'entrée du logiciel
if __name__ == "__main__":
    interface = tk.Tk()
    app = API(interface)
    interface.mainloop()