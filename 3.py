def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

print(gcd(48, 18))  # Вывод: 6
print(gcd(17, 5))   # Вывод: 1
print(gcd(-60, 48)) # Вывод: 12