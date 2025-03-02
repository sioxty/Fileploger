# plagin.py Documentation

**Version:** 1.2.0
**Last Updated:** 2025-03-02
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

The `TypeFile` class manages file extension configurations loaded from a JSON file (`settings/ext.json`). It is used to retrieve file extensions based on file types.

#### Constructor (`__init__(self, config_file="settings/ext.json")`)
- **Arguments:**
  - `config_file` (str, optional): The path to the JSON configuration file. Defaults to `"settings/ext.json"`. The JSON file should contain a dictionary where keys represent file types (e.g., `"images"`, `"documents"`) and values are lists of file extensions (e.g., `[".jpg", ".png"]`).
  - If the file is not found or is invalid JSON, the class defaults to an empty dictionary (`{}`).

#### Methods:
- **`get_extensions(self, file_type)`**
  - **Arguments:**
    - `file_type` (str): The type of file (e.g., `"images"`, `"documents"`, `"music"`).
  - **Returns**:
    - A list of file extensions (list) associated with the specified `file_type`. If the `file_type` is not found or there's an error, it returns an empty list.

#### Example Usage:

```python
# Initialize the TypeFile object
file_types = TypeFile("settings/ext.json")

# Get extensions for images
image_extensions = file_types.get_extensions("images")
print(image_extensions)  # Output: [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

# Get extensions for documents
document_extensions = file_types.get_extensions("documents")
print(document_extensions)  # Output: [".pdf", ".docx", ".doc", ".txt", ".rtf"]

# Get extensions for an unknown type
unknown_extensions = file_types.get_extensions("unknown")
print(unknown_extensions)  # Output: []
```

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

type_file = plagin.TypeFile()

# Create a FileManager object
file_manager = plagin.FileManager("path/to/your/source/directory")

# Move .txt files to a new directory
moved_count = file_manager.move("path/to/your/destination/directory", type_file.get_extensions("documents"))
print(f"Moved {moved_count} files.")

# Delete .tmp files
file_manager.delete(['.tmp'])

