from bird import *

zola = Bird("BOOBOBOB")

print('\nАТРИБУТЫ:')

for attrib in dir(zola):
    if attrib[0] == '-':
        print(attrib)

print("\nClass dict")

for item in Bird.__dict__:
    print(item, ':', Bird.__dict__[item])

print("\nDict element")

for item in zola.__dict__:
    print(item, ":", zola.__dict__[item])

