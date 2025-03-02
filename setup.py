from cx_Freeze import setup, Executable

options = {
    "build_exe": {
        "include_files": ["icon.ico", "settings/"],  # Додай сюди всі необхідні файли та папки
    }
}

setup(
    name="File Manager",
    version="1.0",
    description="Простий файловий менеджер",
    options=options,
    executables=[Executable("app.py", base="Win32GUI", icon="icon.ico")]
)
