import os
import shutil
import logging
import json

logger = logging.getLogger("FileManager")

class TypeFile:
    def __init__(self, config_file="settings/ext.json"):
        try:
            with open(config_file, "r") as f:
                self.extensions = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Error loading extension configuration: {e}")
            self.extensions = {}  # Default to empty if error

    def get_extensions(self, file_type:str)->list:
        return self.extensions.get(file_type, [])


class FileManager:
    def __init__(self, src_dir: str):
        self.src_dir = src_dir

    def move(self, dest_dir: str, extensions)->int:
        try:
            files = self.__sort_extension(extensions)
            if not files:
                logger.info(f"No files found with specified extensions in {self.src_dir}")
                return 0  # Повертаємо 0, якщо немає файлів
                
            os.makedirs(dest_dir, exist_ok=True)  # Створюємо директорію, якщо її немає

            moved_files = []
            for file in files:
                src_path = os.path.join(self.src_dir, file)
                
                # Перевіряємо, чи існує вихідний файл
                if not os.path.exists(src_path):
                    logger.warning(f"File not found: {src_path}")
                    continue  # Пропускаємо файл

                dest_path = os.path.join(dest_dir, file)

                # Якщо файл вже є в `dest_dir`, генеруємо унікальне ім'я
                if os.path.exists(dest_path):
                    dest_path = self.__get_unique_filename(dest_dir, file)
                    logger.info(f"File renamed {dest_path}")

                # Переміщуємо файл
                shutil.move(src_path, dest_path)
                moved_files.append(dest_path)

            logger.info(f"Moved {len(moved_files)} files to {dest_dir}")
            return len(moved_files)  # Повертаємо кількість переміщених файлів
        
        except (FileNotFoundError, shutil.Error) as e:  
            logger.error(f"Error moving files: {e}", exc_info=True)
            raise  # Повторно кидаємо виняток після логування


    def delete(self, extensions: list)->int:
        try:
            files = self.__sort_extension(extensions)
            if files:
                for file in files:
                    os.remove(os.path.join(self.src_dir, file))
                logger.info(f"Deleted {len(files)} files")
                return len(files)  # Повертаємо кількість видалених файлів
            else:
                logger.info(f"No files found with specified extensions in {self.src_dir}")
                return 0  # Повертаємо 0, якщо немає файлів
        except (FileNotFoundError, OSError) as e:  # Catch specific exceptions
            logger.error(f"Error deleting files: {e}")
            raise  # Re-raise after logging

    def __sort_extension(self, extensions: list) -> list:
        files = os.listdir(self.src_dir)
        result = []
        for file in files:
            for ext in extensions:
                if file.lower().endswith(ext.lower()):  # Case-insensitive matching
                    result.append(file)
                    break  # Avoid adding the same file multiple times
        return result
    
    def __get_unique_filename(self, dest_dir: str, filename:str) -> str:
        base, ext = os.path.splitext(filename)
        i = 1
        while True:
            dest_path = os.path.join(dest_dir, f"{base}{f' ({i}){ext}' if i > 1 else ext}")
            if not os.path.exists(dest_path):
                return dest_path
            i += 1