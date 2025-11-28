def get_permutations(s):
    # Базовый случай: если строка пустая или из одного символа
    if len(s) <= 1:
        return [s]

    permutations = []

    for i in range(len(s)):
        # Берем текущий символ
        current_char = s[i]
        # Оставшаяся часть строки без текущего символа
        remaining_chars = s[:i] + s[i + 1:]

        # Рекурсивно получаем перестановки для оставшейся части
        for perm in get_permutations(remaining_chars):
            # Добавляем текущий символ в начало каждой перестановки
            permutations.append(current_char + perm)

    return permutations

# Пример с строкой "abc"
result = get_permutations("abc")
print(result)  # Вывод: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
print(f"Количество перестановок: {len(result)}")

# Пример с строкой "ab"
result2 = get_permutations("ab")
print(result2)  # Вывод: ['ab', 'ba']

# Пример с одним символом
result3 = get_permutations("a")
print(result3)  # Вывод: ['a']