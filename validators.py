import re

def validate_phone(phone_type, phone):
    """
    Проверяет и возвращает валидный телефонный номер.

    Args:
        phone_type (str): Тип телефонного номера ("рабочий" или "личный").
        phone (str): Введенный пользователем телефонный номер.

    Returns:
        str: Валидный телефонный номер или пустая строка, если введен некорректный номер.
    """
    if re.match(r'^\+7\d{10}$', phone) or phone == '':
        return phone
    else:
        print(f"Некорректный формат номера телефона. Введите номер снова.")
        return validate_phone(phone_type, input(f"Введите {phone_type} номер телефона: "))
