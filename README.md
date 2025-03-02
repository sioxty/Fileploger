# FilePloger: A Python File Management Plugin

**Version:** 1.1.0

**Author:** Sioxty

**Description:**

FilePloger is a simple yet powerful Python plugin designed for efficient file management. It allows you to move and delete files based on their extensions, simplifying bulk file operations and improving workflow.  FilePloger uses configuration files for flexibility and includes robust logging and error handling.


## Features:

* **Move Files:** Moves files with specified extensions from a source directory to a destination directory.  Handles existing files in the destination by appending numbers to filenames to prevent overwriting. Creates destination directory if it doesn't exist.
* **Delete Files:** Deletes files with specified extensions from a source directory.
* **Configuration File:** Uses a JSON configuration file (`setting/ext.json` by default) to define file types and their associated extensions, making it highly customizable.
* **Logging:** Uses Python's `logging` module to provide detailed information about operations performed, including errors and warnings.
* **Error Handling:** Includes comprehensive error handling for file-related issues, ensuring graceful operation even when encountering unexpected problems.
* **Case-Insensitive Matching:** File extension matching is case-insensitive.


## Installation:

1.  **Clone the repository:** `git clone https://github.com/sioxty/Fileploger/tree/main`
2.  **Navigate to the directory:** `cd FilePloger`
3. **[Install winwows amd64](installer/Output/Fileploger.exe)**

## Usage:

FilePloger is designed to be used as a plugin within other applications.  However, you can also use it directly from the command line (or within a Python script).

**Example (Python Script):**

```python
import plagin
import logging

# Configure logging (optional, but recommended)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a FileManager object
file_manager = plagin.FileManager("path/to/your/source/directory")

# Move .txt files to a new directory
moved_files = file_manager.move("path/to/your/destination/directory", ['.txt'])
print(f"Moved files: {moved_files}")

# Delete .tmp files
file_manager.delete(['.tmp'])
```

[Documentation](doc.md)