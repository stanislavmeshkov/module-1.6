my_dict = {'Pavel' : 1980, 'Stas' : 1988, 'Alesha' : 1987}
print(my_dict)
print(my_dict['Stas'])
my_dict['Sacha'] = 1981
print(my_dict['Sacha'])
my_dict.update({'Kiril' : 1982, 'Dima' : 1988})
print(my_dict)
p = my_dict.pop('Pavel')
print(my_dict)
print(p)

my_set = {9, 8, 7, 6, 6, 7, 8, 9, 'Miki', False}
print(my_set)
my_set.update({1, 'Met'})
print(my_set.discard(False))
print(my_set)