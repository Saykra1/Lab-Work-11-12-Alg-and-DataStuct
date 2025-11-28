def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))     # Вывод: "olleh"
print(reverse_string("Python"))    # Вывод: "nohtyP"
print(reverse_string("Аa"))         # Вывод: "Аa"
