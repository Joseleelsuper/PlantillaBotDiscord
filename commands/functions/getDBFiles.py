import os
from pathlib import Path

def getCommands():
    # Obtener la ruta absoluta del directorio de trabajo actual
    app_path = os.getcwd()
    # Unir esta ruta con la ruta al archivo que quieres abrir
    file_path = os.path.join(app_path, "db/util/commands.json")

    return file_path

def getDotenv():
    # Obtener la ruta absoluta del directorio raíz del proyecto
    project_dir = Path(__file__).resolve().parents[2]
    # Unir esta ruta con la ruta al archivo que quieres abrir
    file_path = project_dir / ".env"
    return str(file_path)