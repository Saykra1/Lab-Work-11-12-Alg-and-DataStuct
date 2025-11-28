def find_max(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        # Рекурсивно находим максимум в оставшейся части массива
        max_rest = find_max(arr[1:])
        # Сравниваем первый элемент с максимумом оставшейся части
        return arr[0] if arr[0] > max_rest else max_rest

print(find_max([3, 1, 4, 1, 5, 9, 2]))  # Вывод: 9
print(find_max([-5, -2, -10]))          # Вывод: -2
print(find_max([42]))                   # Вывод: 42
print(find_max([]))                     # Вывод: None


