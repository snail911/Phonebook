from data import save_data
from handlers import display_results, create_entry


class Menu:
    """
       Класс, представляющий меню телефонного справочника.

       Attributes:
           data (list): Список данных с записями в справочнике.
           menu_options (dict): Словарь с опциями меню и соответствующими методами.

       Methods:
           display_entries: Выводит записи на экран.
           add_entry: Добавляет новую запись в справочник.
           edit_entry: Редактирует существующую запись.
           search_entries: Выполняет поиск записей по заданному тексту.
           run: Запускает цикл меню.
       """
    def __init__(self, data):
        self.data = data
        self.menu_options = {
            "1": self.display_entries,
            "2": self.add_entry,
            "3": self.edit_entry,
            "4": self.search_entries,
            "5": exit
        }

    def display_entries(self):

        page = int(input("Введите номер страницы: "))
        page_size = 5
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        entries_to_display = self.data[start_idx:end_idx]

        if entries_to_display:
            print("\nЗаписи на странице:")
            for idx, entry in enumerate(entries_to_display, start=start_idx + 1):
                display_results(idx, entry)
        else:
            print("На этой странице нет записей.")

    def add_entry(self):
        """
                Добавляет новую запись в справочник.
        """
        entry = create_entry()
        self.data.append(entry)
        save_data(self.data)

    def edit_entry(self):
        """
                Редактирует существующую запись в справочнике.
        """
        input_fields = ["last_name", "first_name", "middle_name", "organization", "work_phone", "personal_phone"]
        update_functions = {field: lambda current, new: new if new != "" else current for field in input_fields}

        index = int(input("Введите номер записи для редактирования: ")) - 1
        if 0 <= index < len(self.data):
            current_entry = self.data[index]
            new_entry = create_entry()

            for field in update_functions:
                current_entry[field] = update_functions[field](current_entry[field], new_entry[field])

            self.data[index] = current_entry
            save_data(self.data)
            print("Запись успешно отредактирована.")
        else:
            print("Неверный номер записи.")

    def search_entries(self):
        """
                Выполняет поиск записей по заданному тексту.
        """
        search_term = input("Введите текст для поиска: ")
        results = [
            entry for entry in self.data if any(
                search_term.lower() in value.lower() for value in entry.values()
            )
        ]
        if results:
            print("\nРезультаты поиска:")
            for idx, entry in enumerate(results, start=1):
                display_results(idx, entry)

        else:
            print("Ничего не найдено.")

    def run(self):
        """
                Запускает цикл меню и обработку действий пользователя.
        """
        while True:
            print("\nМеню:")
            print("1. Вывод записей")
            print("2. Добавление записи")
            print("3. Редактирование записи")
            print("4. Поиск записей")
            print("5. Выход")

            choice = input("Выберите действие: ")

            selected_action = self.menu_options.get(choice)
            if selected_action:
                selected_action()
            else:
                print("Неверный выбор. Пожалуйста, выберите корректное действие.")
