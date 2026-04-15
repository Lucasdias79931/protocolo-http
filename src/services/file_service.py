import os
from werkzeug.utils import secure_filename
from uuid import uuid4
from dotenv import load_dotenv

load_dotenv()
UPLOAD_FOLDER = os.getenv('UPLOAD')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


class FileService:

    @staticmethod
    def save_file(file):
        filename = secure_filename(file.filename)

        id_file  = str(uuid4())
        base_dir = os.path.join(UPLOAD_FOLDER, id_file)

        os.makedirs(base_dir, exist_ok=True)
        path = os.path.join(base_dir, filename)
        file.save(path)

        return filename, id_file

    @staticmethod
    def get_file_path(filename, image_id):

        path = os.path.join(UPLOAD_FOLDER,image_id ,filename)

        if not os.path.exists(path):
            return None

        return path
    


    @staticmethod
    def list_images():

        all_id = os.listdir(UPLOAD_FOLDER)
        all_images = []

        if not all_id:
            return []

        for folder in all_id:
            folder_path = os.path.join(UPLOAD_FOLDER, folder)

            if not os.path.isdir(folder_path):
                continue

            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)

                if os.path.isfile(file_path):
                    all_images.append({
                        "id": folder,
                        "filename": filename,
                        "path": file_path
                    })

        return all_images
