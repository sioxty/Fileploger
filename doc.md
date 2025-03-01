# plagin.py Documentation

**Version:** 1.1.0
**Last Updated:** 2023-10-27
**Author:** Sioxty

**Description:** `plagin.py` is a Python module providing file management functionalities. It allows for moving and deleting files based on their extensions. The module uses the `logging` module for recording actions and handles potential errors gracefully.  It includes improved error handling and file renaming to prevent overwrites.

## Table of Contents

- [1. Introduction](#1-introduction)
- [2. Classes](#2-classes)
    - [2.1 `TypeFile`](#21-typefile)
    - [2.2 `FileManager`](#22-filemanager)
- [3. Usage](#3-usage)
- [4. Logging](#4-logging)
- [5. Error Handling](#5-error-handling)


## 1. Introduction

This plugin simplifies file operations, categorizing files by extension and enabling bulk moves and deletions. It is designed to be integrated into other applications.  It reads file extension configurations from a JSON file (`settings/ext.json`) for flexibility.


## 2. Classes

### 2.1 `TypeFile`

This class manages file extension configurations loaded from a JSON file (`settings/ext.json`). It's used internally by `FileManager` to determine which files match specified file types.

*   **Constructor (`__init__(self, config_file="settings/ext.json")`)**
    *   `config_file` (str, optional): The path to the JSON configuration file. Defaults to "settings/ext.json". The JSON file should contain a dictionary where keys represent file types (e.g., "document", "image") and values are lists of file extensions (e.g., `["txt", "pdf"]`).  If the file is not found or is invalid JSON, a default empty dictionary is used.

*   **Methods:**
    *   `get_extensions(self, file_type)`: Returns a list of file extensions associated with the given `file_type` from the configuration file. Returns an empty list if the `file_type` is not found or if there's an error reading the configuration file.


### 2.2 `FileManager`

This class provides the core functionality: moving and deleting files.

*   **Constructor (`__init__(self, src_dir: str)`)**
    *   `src_dir` (str): The source directory containing the files to be managed.

*   **Methods:**
    *   `move(self, dest_dir: str, extensions: list)`: Moves files with specified extensions from the source directory to the destination directory. It handles cases where files already exist in the destination by appending a number to the filename (e.g., `myfile.txt` becomes `myfile (1).txt`). Creates the destination directory if it doesn't exist.  Returns the number of files successfully moved.
        *   `dest_dir` (str): The destination directory.
        *   `extensions` (list): A list of file extensions (e.g., `['.txt', '.pdf']`).
    *   `delete(self, extensions: list)`: Deletes files with the specified extensions from the source directory.
        *   `extensions` (list): A list of file extensions to delete.
    *   `__sort_extension(self, extensions: list) -> list`: (Private helper method) Filters files in the source directory based on provided extensions. Returns a list of file names matching the extensions. Performs case-insensitive matching.
    *   `__get_unique_filename(self, dest_dir, filename)`: (Private helper method) Generates a unique filename if a file with the same name already exists in the destination directory.  This prevents overwrites.


## 3. Usage

```python
import plagin
import logging

# Configure logging (optional, but recommended)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a FileManager object
file_manager = plagin.FileManager("path/to/your/source/directory")

# Move .txt files to a new directory
moved_count = file_manager.move("path/to/your/destination/directory", ['.txt'])
print(f"Moved {moved_count} files.")

# Delete .tmp files
file_manager.delete(['.tmp'])

