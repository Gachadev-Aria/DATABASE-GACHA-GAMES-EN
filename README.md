# Database Gacha Games FR

## Description: 
Un logiciel permettant de sauvegarder les OC des jeux pour en garder une trace:
- Gache Club
- Gacha Plus
- Gacha Life 2
- Gacha Nebula v1.6

Le projet a commencé le 22/08/2026 et il se basait sur un projet existant de mon ordinateur.

---

## 📸 Aperçu
![Capture d'écran](app/assets/Capture_d'écran_DATABASE.png)

---

## 🚀 Fonctionnalités
- ✅ Ajout d'OC de différentes applications
- ✅ Affichage de l'OC
- ✅ Possibilité de copier le code stocké
- ✅ Personnalisation (couleur et police)

---

## 📌 **À propos du projet**
- **Backend** : Python
- **Frontend** : Python Tkinter
- **Database**: SQL et JSON

---

## 🤖 Utilisation de l'IA

Ce projet a été développé avec l'aide d'outils d'intelligence artificielle (Mistral AI).

**La contribution de l'IA** inclut :
- la création de la class FontChooserDialog avec quelques modifications personnelles
- une partie de mon apprentissage sur SQL
- la résolution d'erreurs non comprises
- des fonctionnalités spécifiques 

## Utilisation

Prérequis:
- python
- tkinter
- color-contrast
- colour
- pathlib
- pyperclip
- pyinstaller

### Solution 1:
1. Cloner le dépôt :
     ```bash
     git clone https://github.com/Gachadev-Aria/Database-Gacha-Games-FR.git
Ou:
     Télécharger le [fichier ZIP.](https://github.com/Gachadev-Aria/Database-Gacha-Games-FR/archive/refs/heads/main.zip)
  
2. Dans la console de votre ordi:
    ```bash
    cd Database-Gacha-Games-FR
    python -mvenv venv
    python run.py
Ou 
     Ouvrir run.py avec un logiciel de code et l'executer (Exemple: VS Code)
3. Puis commencez !

### Solution 2, Créer un fichier exe
1. Cloner le dépôt ou télécharger le fichier ZIP.
2. Dans la console de votre ordi:
   ```bash
   cd Database-Gacha-Games-FR
   python -m PyInstaller --onefile --windowed --add-data "app/fichier_code;app/fichier_code" --add-data "app/parametres;app/parametres" --add-data "app/static;app/static"  --add-data "app/database;app/database" run.py
3. Ouvrer /dist/run
4. Puis commencer !



---
## 📧 Contact

Vous pouvez me contacter par mail: aria.and.idriss@gmail.com
