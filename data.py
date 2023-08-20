import json

DATA_FILE = "phonebook_data.json"

def load_data():
    """
    Загружает данные из файла phonebook_data.json.

    Returns:
        list: Список данных из файла. Если файл не найден, возвращает пустой список.
    """
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    """
    Сохраняет данные в файл phonebook_data.json.

    Args:
        data (list): Список данных для сохранения.

    Returns:
        None
    """
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
