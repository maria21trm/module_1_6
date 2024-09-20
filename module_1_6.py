my_dict = {'Maria':2003,'Alena': 2004}
print(my_dict)
print(my_dict.get('Maria'))
print(my_dict.get('Sveta'))
my_dict.update({'Alina': 1999, 'Natali': 2000})
a=my_dict.pop('Alena')
print(a)
print(my_dict)

my_set = {1,1,3,5,5,'string'}
print(my_set)
my_set.add(2)
my_set.add(4)
my_set.discard(3)
print(my_set)

