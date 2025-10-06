from bird import *
chick = Bird('Cheep, cheep!')
chick.age = '1 week'

print('\nChick says:', chick.talk())
print('\nChick age:', chick.age)

chick.age = '2 week'
print('\nChick age:', chick.age)

setattr(chick, 'age', '4 weeks')
print("\n Chick attr")
for attrib in dir(chick):
    if attrib[0] != '_':
        print(attrib, ':', getattr(chick, attrib))
delattr(chick, 'age')
print("chick agew attr", hasattr(chick, 'age'))