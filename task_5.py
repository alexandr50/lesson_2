list_1 = [1.2, 23.57, 76.7, 9.0, 77.5, 24.8, 22.2, 0.7, 10.0, 47.77]
print(id(list_1))
for i in list_1:
    rub = int(i)
    cent = int(i * 100 % 100)
    print(f'{rub} руб {cent:02d} коп', end=', ')
print(id(list_1))
list_1.sort()
print(id(list_1))
print(list_1)
list_1 = list(reversed(list_1))
print(id(list_1))
print(list_1)
for i in range(5):
    print(list_1[i])
