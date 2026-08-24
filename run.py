# Importations externes
import tkinter as tk

# Importation interne
from app.API import API

# Point d'entrée du logiciel
if __name__ == "__main__":
    interface = tk.Tk()
    app = API(interface)
    interface.mainloop()
