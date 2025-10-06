# from moduls import dog
# for i in dir(dog):
#     print(i)

snack = '{} and {}'.format('Burger', "Fries")
print('\nReplaced:', snack)

snack = '{1} and {0}'.format('Burgers', "Fries")
print("Replaced: ", snack)

snack = '%s and %s' % ('Milk', "Cookies")
print('\nSub: ', snack)