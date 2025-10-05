from pathlib import Path

def write_file(file_name, file_content):
   
    file_path = Path(f"{file_name}.txt")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(file_content)


def append_file(file_name, append_content):
    file_path = Path(f"{file_name}.txt")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(append_content)


def read_file(file_name):
    file_path = Path(f"{file_name}.txt")
    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} does not exist.")
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content
