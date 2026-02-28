"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

TABLE_SIZE = 10007 # візьмемо велике просте число так буде менше колізій. 10007 має бути оптимально для наших тест кейсів.
#Загалом якщо виходити за межі тест кейсу, ми можемо рехешувати нашу таблицю у вдвічі більшу кожен раз коли вона починає переповнюватися, але в нашому випадку в цьому нема потреби
table = []

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global table
    table = [None] * TABLE_SIZE


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    idx = get_index(author)

    # Якщо комірка порожня або делейтнута, створюємо новий запис
    if table[idx] is None or table[idx] == "DELETED":
        table[idx] = [author, [title]]
    else:
        # Якщо автор вже є, перевіряємо, чи немає ще такої книги, і додаємо
        if title not in table[idx][1]:
            table[idx][1].append(title)


def find(author, title) ->bool:
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    idx = get_index(author)

    # Якщо за індексом є реальні дані і автор той самий
    if table[idx] is not None and table[idx] != "DELETED" and table[idx][0] == author:
        return title in table[idx][1]

    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    idx = get_index(author)

    # Якщо автор знайдений
    if table[idx] is not None and table[idx] != "DELETED" and table[idx][0] == author:
        # Якщо така книга дійсно є у його списку
        if title in table[idx][1]:
            table[idx][1].remove(title)

            # Якщо після видалення книг більше не залишилося, видаляємо автора
            if len(table[idx][1]) == 0:
                table[idx] = "DELETED"


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    idx = get_index(author)

    # Якщо автор знайдений, повертаємо відсортований список
    if table[idx] is not None and table[idx] != "DELETED" and table[idx][0] == author:
        return sorted(table[idx][1])

    # інакше, повертаємо порожній список
    return []

########################

def get_index(author): #Шукаємо індекс автора або перший вільний
    idx = my_hash(author) % TABLE_SIZE # Хешом ж можна коримстуватися? його з нуля не треба писати?
    first_deleted = -1

    while table[idx] is not None:
        if table[idx] == "DELETED":
            if first_deleted == -1:
                first_deleted = idx # Запам'ятовуємо перше видалене місце
        elif table[idx][0] == author:
            return idx # Знайшли автора (вже є)
        idx = (idx + 1) % TABLE_SIZE # Йдемо далі

    # Якщо автора не знайдено, повертаємо місце для запису
    return first_deleted if first_deleted != -1 else idx


def my_hash(string):
    hash_value = 0
    p = 31  #має вистачити

    for char in string:
        hash_value = (hash_value * p + ord(char))
    return hash_value