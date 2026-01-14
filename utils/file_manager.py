import os

UPLOAD_FOLDER = "uploads"
HISTORY_FILE = "history.txt"

# Stelle sicher, dass Upload-Ordner existiert
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def save_code_to_file(code, filename="script.py"):
    with open(filename, "w") as f:
        f.write(code)
    return filename

def save_upload(file):
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return filepath

def save_history(code):
    with open(HISTORY_FILE, "a") as f:
        f.write(code + "\n" + "-"*40 + "\n")

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return f.read()
    return ""
