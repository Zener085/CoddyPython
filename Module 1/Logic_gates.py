# 2 занятие - сравниваем значения друг с другом

a = 5  # просто переменные
b = 4

print(a == b)  # сравнение, выведет False, потому что 'a' не равно 'b'
print(a != b)  # уже True, потому что 'a' не равно 'b'

print(a > b)  # True, а больше b
print(a >= b)  # True, a больше или равно b
# аналогично работают '<' и '<=', в данном примере они оба выведут False ('a' не меньше или равно 'b')

# Иногда нужно сравнивать сразу несколько условий, для этого мы используем 'and' и 'or'
print(a == 5 and b == 4)  # True, должны выполниться сразу оба условия
print(a != 5 or b == 4)  # True, должно выполниться хотя бы 1 условие (тут выполняется второе)

# Чтобы взять полное отрицание, можно также использовать 'not'
print(not a)  # False, так как bool(a) - True, а not переворачивает ответ

# В Python иногда есть небольшие проблемы с данными. Вот 1 пример
print(115 == 1.15 * 100)  # False, чтобы понять почему - надо понимать, что такое мантисса и как она работает в Python

# В Python можно сравнивать что угодно
# в основном сравнение используют, чтобы проверить одинаковые значения 2-х переменных
print("привет" == "ПРИВЕТ")  # False, так как строки не совпадают
