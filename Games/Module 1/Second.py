a = 5  # просто переменные
b = 4

print(a == b)  # сравнение, выведет False
print(a != b)  # True, a не равно b

print(a > b)  # True, а больше b
print(a >= b)  # True, a больше или равно b
# аналолгично работают < и <=

print(a == 5 and b == 4)  # True, должны выполниться сразу оба условия
print(a != 5 or b == 4)  # True, должно выполниться хотя бы 1 условие (тут выполняется второе)

print(115 == 1.15 * 100)  # прикол
