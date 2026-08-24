# Imporataions externes
import sqlite3, os
from tkinter import ttk

class DB():
    """Classe secondaire pour gérer la SQL Database."""
    def __init__(self):
        """Fonction d'initialisation de la classe pour créer la SQL Database"""
        db_path = os.path.join(os.path.dirname(__file__), "database", "gacha_games.db")
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS GachaGames (
            CharacterId INTEGER PRIMARY KEY,
            CharacterName TEXT,
            Game TEXT,
            CharacterImage TEXT,
            DATE TEXT DEFAULT CURRENT_DATE
        );""")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS GachaClub (
            CharacterId INTEGER PRIMARY KEY,
            CharacterName TEXT,
            CharacterImage TEXT,
            DATE TEXT DEFAULT CURRENT_DATE
        );""")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS GachaPlus (
            CharacterId INTEGER PRIMARY KEY,
            CharacterName TEXT,
            CharacterImage TEXT,
            DATE TEXT DEFAULT CURRENT_DATE
        );""")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS GachaLife2 (
            CharacterId INTEGER PRIMARY KEY,
            CharacterName TEXT,
            CharacterImage TEXT,
            DATE TEXT DEFAULT CURRENT_DATE
        );""")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS GachaNebula16 (
            CharacterId INTEGER PRIMARY KEY,
            CharacterName TEXT,
            CharacterImage TEXT,
            DATE TEXT DEFAULT CURRENT_DATE
        )""")

        self.conn.commit()
    
    def load_data(self, tree: ttk.Treeview, table: str):
        """
        Fonction permettant de remplir le tableau 
        avec les données de la table SQL.
        Args:
            tree: tableau à remplir.
            table: nom de la table SQL.
        """
        for item in tree.get_children():
            tree.delete(item)
        self.cursor.execute(f"SELECT * FROM {table}")
        rows = self.cursor.fetchall()
        for row in rows:
            tree.insert("", "end", values=row)

    def update_db1(self, tableauGG: ttk.Treeview):
        """
        Fonction permettant de mettre à jour la table 
        SQL GachaGames de la SQL Database avec les lignes 
        du ttk.Treview tableauGG.
        Args:
            tableauGG:
        """
        self.cursor.execute("DELETE FROM GachaGames")
        for item in tableauGG.get_children():
            values = tableauGG.item(item, "values")
            if len(values) == 5:
                self.cursor.execute("""
                INSERT OR REPLACE INTO GachaGames (CharacterId, CharacterName, Game, CharacterImage, DATE)
                VALUES (?, ?, ?, ?, ?)
                """, values)
            elif len(values) == 4:
                self.cursor.execute("""
                INSERT OR REPLACE INTO GachaGames (CharacterId, CharacterName, Game, CharacterImage)
                VALUES (?, ?, ?, ?)
                """, values)
        self.conn.commit()

    def update_db2(self, tableauGC: ttk.Treeview):
        """
        Fonction permettant de mettre à jour la table 
        SQL GachaClub de la SQL Database avec les lignes 
        du ttk.Treview tableauGC.
        Args:
            tableauGC:
        """
        self.cursor.execute("DELETE FROM GachaClub")
        for item in tableauGC.get_children():
            values = tableauGC.item(item, "values")
            if len(values) == 4:
                self.cursor.execute("""
                INSERT OR REPLACE INTO GachaClub (CharacterId, CharacterName, CharacterImage, DATE)
                VALUES (?, ?, ?, ?)
                """, values)
            elif len(values) == 3:
                self.cursor.execute("""
                INSERT OR REPLACE INTO GachaClub (CharacterId, CharacterName, CharacterImage)
                VALUES (?, ?, ?)
                """, values)
            self.conn.commit()

    def update_db3(self, tableauGP: ttk.Treeview):
        """
        Fonction permettant de mettre à jour la table 
        SQL GachaPlus de la SQL Database avec les lignes 
        du ttk.Treview tableauGP.
        Args:
            tableauGP:
        """        
        self.cursor.execute("DELETE FROM GachaPlus")
        for item in tableauGP.get_children():
            values = tableauGP.item(item, "values")
            if len(values) == 4:
                self.cursor.execute("""
                INSERT OR REPLACE INTO GachaPlus (CharacterId, CharacterName, CharacterImage, Date)
                VALUES (?, ?, ?, ?)
                """, values)
            elif len(values) == 3:
                self.cursor.execute("""
                INSERT OR REPLACE INTO GachaPlus (CharacterId, CharacterName, CharacterImage)
                VALUES (?, ?, ?)
                """, values)
        self.conn.commit()

    def update_db4(self, tableauGL2: ttk.Treeview):
        """
        Fonction permettant de mettre à jour la table 
        SQL GachaLife2 de la SQL Database avec les lignes 
        du ttk.Treview tableauGL2.
        Args:
            tableauGL2:
        """
        self.cursor.execute("DELETE FROM GachaLife2")
        for item in tableauGL2.get_children():
            values = tableauGL2.item(item, "values")
            if len(values) == 4:
                self.cursor.execute("""
                INSERT OR REPLACE INTO Gachalife2 (CharacterId, CharacterName, CharacterImage, DATE)
                VALUES (?, ?, ?, ?)
                """, values)
            elif len(values) == 5:
                self.cursor.execute("""
                INSERT OR REPLACE INTO Gachalife2 (CharacterId, CharacterName, CharacterImage)
                VALUES (?, ?, ?)
                """, values)        
            self.conn.commit()

    def update_db5(self, tableauGN16: ttk.Treeview):
        """
        Fonction permettant de mettre à jour la table 
        SQL GachaNebula16 de la SQL Database avec les lignes 
        du ttk.Treview tableauGN16.
        Args:
            tableauGN16
        """
        self.cursor.execute("DELETE FROM GachaNebula16")
        for item in tableauGN16.get_children():
            values = tableauGN16.item(item, "values")
            if len(values) == 4:
                self.cursor.execute("""
                INSERT OR REPLACE INTO GachaNebula16 (CharacterId, CharacterName, CharacterImage, DATE)
                VALUES (?, ?, ?, ?)
                """, values)
            elif len(values) == 3:
                self.cursor.execute("""
                INSERT OR REPLACE INTO GachaNebula16 (CharacterId, CharacterName, CharacterImage)
                VALUES (?, ?, ?)
                """, values)
        self.conn.commit()

    def update_db(self, tableauGG: ttk.Treeview, tableauGC: ttk.Treeview, 
                  tableauGP: ttk.Treeview, tableauGL2: ttk.Treeview, 
                  tableauGN16: ttk.Treeview):
        """
        Fonction conteneur permettant de mettre à jour les tables 
        SQL GachaGames, GachaClub, GachaPlus, GachaLife2, GachaNebula16 
        de la SQL Database avec les ttk.Treview tableauGG, tableauGC, 
        tableauGP, tableauGL2, tableauGN16.
        Args:
            tableauGG: 
            tableauGC: 
            tableauGP: 
            tableauGL2: 
            tableauGN16:
        """
        self.update_db1(tableauGG)
        self.update_db2(tableauGC)
        self.update_db3(tableauGP)
        self.update_db4(tableauGL2)
        self.update_db5(tableauGN16)

