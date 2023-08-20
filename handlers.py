from validators import validate_phone

def display_results(idx, entry):
    """
    Выводит информацию о записи в удобном формате.

    Args:
        idx (int): Номер записи.
        entry (dict): Словарь с данными записи.

    Returns:
        None
    """
    print(f"{idx}. {entry['last_name']} {entry['first_name']} {entry['middle_name']}")
    print(f"   Организация: {entry['organization']}")
    print(f"   Рабочий телефон: {entry['work_phone']}")
    print(f"   Личный телефон: {entry['personal_phone']}\n")

def create_entry():
    """
    Создает новую запись в телефонном справочнике.

    Returns:
        dict: Словарь с данными новой записи.
    """
    entry = {
        "last_name": input("Введите фамилию: "),
        "first_name": input("Введите имя: "),
        "middle_name": input("Введите отчество: "),
        "organization": input("Введите название организации: "),
        "work_phone": validate_phone("рабочий", input("Введите рабочий телефон: ")),
        "personal_phone": validate_phone("личный", input("Введите личный телефон: "))
    }

    return entry




