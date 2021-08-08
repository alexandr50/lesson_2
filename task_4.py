list_1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in list_1:
    i = i.split()
    name = (i[-1]).capitalize()
    print('Привет,' + name + '!')
list_2 = []

for j in list_1:
    j = j.split()
    j = j[-1:]
    j = ' '.join(j)
    j = j.capitalize()
    list_2.append(j)
print(list_2)