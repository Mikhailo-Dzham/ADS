import sys


def solve():
    # Зчитуємо весь вхідний текст
    input_data = sys.stdin.read()

    # 1. Знаходимо перше число N (розмір словника)
    n_str = ""
    idx = 0

    # Пропускаємо будь-які пробіли на самому початку, поки не знайдемо першу цифру
    while idx < len(input_data) and not input_data[idx].isdigit():
        idx += 1

    # Збираємо цифри, щоб отримати число N
    while idx < len(input_data) and input_data[idx].isdigit():
        n_str += input_data[idx]
        idx += 1

    if not n_str:
        return
    n = int(n_str)

    # парсер слів
    words = []
    current_word = []

    # Продовжуємо читати текст з того місця, де закінчилося число N
    for i in range(idx, len(input_data)):
        char = input_data[i]

        # Чекаєм, чи це латинська літера
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            current_word.append(char.lower())  # Одразу переводимо в нижній регістр
        else:
            # Якщо символ - не літера, але ми вже назбирали якісь літери
            if current_word:
                words.append("".join(current_word))  # Склеюємо літери у слово
                current_word = []  # Очищаємо масив для наступного слова

    if current_word:
        words.append("".join(current_word))

    # Розділяємо знайдені слова на словник і твір
    dict_words = words[:n]
    text_words = words[n:]

    # Ініціалізація хеш-таблиці
    TABLE_SIZE = 20011
    table = [[] for _ in range(TABLE_SIZE)]

    def my_hash(string):
        h = 0
        for char in string:
            h = (h * 31 + ord(char)) % TABLE_SIZE
        return h

    # Заповнюємо словник
    for w in dict_words:
        idx = my_hash(w)
        found = False
        for item in table[idx]:
            if item[0] == w:
                found = True
                break

        if not found:
            table[idx].append([w, False])

    # Перевіряємо слова з тексту
    unknown_found = False
    for w in text_words:
        idx = my_hash(w)
        found = False

        for item in table[idx]:
            if item[0] == w:
                item[1] = True  # Відмічаємо, що слово використане
                found = True
                break

        if not found:
            unknown_found = True
            break

    # Виводимо результат
    if unknown_found:
        print("Some words from the text are unknown.")
    else:
        all_used = True
        for chain in table:
            for item in chain:
                if item[1] == False:  # Якщо знайшли невикористане слово
                    all_used = False
                    break
            if not all_used:
                break

        if all_used:
            print("Everything is going to be OK.")
        else:
            print("The usage of the vocabulary is not perfect.")


if __name__ == '__main__':
    solve()