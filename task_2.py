list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2 = list_1.copy()
for i in list_2:
    if i.isdigit():
        ind = list_2.index(i)
        list_2[ind] = i.zfill(2)
        list_2[ind] = '"' + list_2[ind] + '"'
    elif i[0] == '+' or i[0] == '-':
        ind = list_2.index(i)
        list_2[ind] = i.zfill(3)
        list_2[ind] = '"' + list_2[ind] + '"'
print(' '.join(list_2))