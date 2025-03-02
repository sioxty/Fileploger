from cx_Freeze import setup, Executable

#init presets 
with open('settings/presets.json', 'r', encoding='utf-8') as file:
    pass

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
