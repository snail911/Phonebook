from menu import Menu
from data import load_data

def main():
    """
    Главная функция для запуска телефонного справочника.

    Returns:
        None
    """
    data = load_data()  # Загрузка данных из файла
    menu = Menu(data)   # Создание объекта Menu с передачей данных
    menu.run()          # Запуск главного цикла меню

if __name__ == "__main__":
    main()
