"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

TABLE_SIZE = 10007
table = []


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global table
    # Створюємо масив, де кожна комірка -- це порожній список (chain)
    table = [[] for _ in range(TABLE_SIZE)]


def addBook(author, title):
    """ Додає книгу до бібліотеки. """
    idx = hash(author) % TABLE_SIZE

    # Шукаємо автора у ланцюжку за обчисленим індексом
    for item in table[idx]:
        if item[0] == author:
            # Автор знайдений. Перевіряємо, чи немає ще такої книги
            if title not in item[1]:
                item[1].append(title)
            return  # Завершуємо роботу функції

    # Якщо цикл завершився і автора не знайдено, додаємо нового автора в ланцюг
    table[idx].append([author, [title]])


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці. """
    idx = hash(author) % TABLE_SIZE

    # Шукаємо автора в ланцюжку
    for item in table[idx]:
        if item[0] == author:
            return title in item[1]

    # Якщо автора взагалі немає в ланцюжку
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки. """
    idx = hash(author) % TABLE_SIZE

    # Шукаємо автора в ланцюжку.
    # через enumerate берем індекс за яким делейтимо книгу
    for i, item in enumerate(table[idx]):
        if item[0] == author:
            # Якщо книга є у списку автора
            if title in item[1]:
                item[1].remove(title)

                # Якщо після видалення у автора не залишилося книг, видаляємо запис про автора з ланцюжка
                if len(item[1]) == 0:
                    table[idx].pop(i)
            return  # Завершуємо роботу, бо автора знайдено і оброблено


def findByAuthor(author):
    """ Повертає список книг заданого автора. """
    idx = hash(author) % TABLE_SIZE

    for item in table[idx]:
        if item[0] == author:
            return sorted(item[1])

    return [] #якщо автора немає