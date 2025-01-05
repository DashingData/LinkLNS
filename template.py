import os  # OS module ko import karte hain directory aur file operations ke liye.
from pathlib import Path  # Pathlib ka use karte hain file/directory path ko handle karne ke liye.
import logging  # Logging module ka use debug aur info messages ke liye hota hai.

# Logging configure karte hain. Yeh hume timestamp ke saath info aur error messages dega.
logging.basicConfig(
    level=logging.INFO,  # INFO level ka matlab hai ki har important message log hoga.
    format='[%(asctime)s : %(levelname)s]: %(message)s'  # Format specify karta hai ki log kaise dikhengi.
)

# User se project name input lene ke liye ek loop
while True:  # Infinite loop jab tak user sahi input na de
    project_name = input("Project Name: ").strip()  # Input lene ke baad strip() extra spaces ko hata deta hai
    if project_name:  # Agar project_name empty nahi hai toh loop se bahar nikalte hain.
        break
logging.info(f"Creating project: {project_name}")  # User ko project create karne ki information dikhate hain.

# File aur folder structure define karte hain jo project ke liye chahiye.
pack_tree = [
    ".github/workflows/.gitkeep",  # Git folder empty na dikhe isliye ek dummy file.
    f"src/{project_name}/__init__.py",  # Project ka main module initialize karne ke liye empty init file.
    "tests/__init__.py",  # Tests folder ke liye init file.
    "tests/unit/__init__.py",  # Unit tests folder ke liye init file.
    "tests/integration/__init__.py",  # Integration tests folder ke liye init file.
    "init_setup.sh",  # Project setup ke liye shell script.
    "requirements.txt",  # Dependencies ke liye file.
    "requirements_dev.txt",  # Development dependencies ke liye file.
    "setup.py",  # Package setup file.
    "setup.cfg",  # Package configuration file.
    "tox.ini",  # Testing automation ke liye configuration file.
    "pyproject.toml",  # Modern Python project configuration file.
]

# Loop karke har file path par kaam karte hain
for filepath in pack_tree:  
    filepath = Path(filepath)  # Path object banate hain jo file/directory ka path represent karta hai.
    filedir = filepath.parent  # Parent method folder ka path deta hai.
    filename = filepath.name  # File name ko extract karte hain.

    # Folder ko create karte hain agar woh already exist nahi karta
    if filedir and not filedir.exists():  # Agar folder ka path hai aur exist nahi karta.
        os.makedirs(filedir, exist_ok=True)  # Folder ko recursively create karte hain.
        logging.info(f"Created directory at: {filedir}")  # Logging karte hain ki folder create ho gaya.

    # File ko create karte hain agar file exist nahi karti ya empty hai
    if not filepath.exists() or filepath.stat().st_size == 0:  # Agar file nahi hai ya size 0 hai.
        with open(filepath, 'w') as f:  # File ko write mode me open karte hain (empty file banata hai).
            pass  # File content nahi likhna, toh pass karte hain.
        logging.info(f"Created new file: {filename} at path: {filepath}")  # File creation ka message log karte hain.
    else:
        logging.info(f"File already exists at path: {filepath}")  # Agar file already hai toh log karte hain.
