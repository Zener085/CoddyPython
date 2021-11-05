aa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # список
aa = list(i for i in range(1, 11))  # такой же список

print(aa[:9])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(aa[1:])  # [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(aa[2:8])  # [3, 4, 5, 6, 7, 8]
print(aa[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(aa[1:8:2])  # [2, 4, 6, 8]

# СТРОКИ - ЭТО СПИСКИ ДЛЯ КОМПЬЮТЕРА, С НИМИ МОЖНО РАБОТАТЬ ТАКЖЕ

aaa = {1: 0, 2: 'a', 5: 'g', 'a': 4}  # словарь
print(aaa['a'])

a = {1, 2, 3, 4, 5}  # по английски кортеж
a = set(i for i in range(1, 6))
# кортеж хранит только уникальные значения, элементы не повторяются
# список может быть [1, 2, 3, 3, 3], а такой же кортеж {1, 2, 3}
# также с кортежом почти ничего нельзя сделать

aaaa = (1, 2, 3, 4, 5, 6)  # множество
aaaa = tuple(i for i in range(1, 7))
# Множество может иметь дупликаты, но как и кортеж, не может изменяться

bb = aa  # делаем копию списка
bb[0] += 1  # увеличиваем первывй элемент на 1
print(aa, bb)  # первый элемент увеличился у обоих списоков на 1, хотя увеличивали только у одного
# см. что такое поинтер (индусы на Ютубе в помощь)

# И снова обычный список
a = list(i for i in range(1, 19))
a.append(5)  # добавляем в конец списка значение 5
a.pop(0)  # удаляем первый элемент списка
a.remove(5)  # удаляем первую попавшуюся значение 5 (если их не будет в списке, будет ошибка)
a.count(5)  # считает кол-во элементов со значением 5
a.index(5)  # выведет номер элемента со значением 5
a.sort()  # сортирует список
a.reverse()  # аналог a[::-1]
a.clear()  # удаляет все элементы из списка
print(len(a))  # выводит кол-во элементов в списке
print(sum(a))  # выводит сумму всех элементов в списке
print(max(a))  # или min(a) - выводит максимальное/минимальное значение из списка
# некоторые команды работают также со словарями, кортежами и множествами, это можно протестировать
