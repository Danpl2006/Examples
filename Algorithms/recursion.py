"""Рекурсия - вызов функцией самой себя. Применение рекурсии не ускоряет работу программы, но она может ускорить
работу программиста"""

def countdown(lst):
    if not lst: # Базовый случай
        return 0
    return 1 + countdown(lst[1:]) # Рекурсивный случай

sp = [1, 4, 5, 7]
result = countdown(sp)
print(result)

"""Стек - структура данных, где новые элементы добавляются в начало списка и этот же элемент при извлечении читается первым.
Когда вызывается функция из другой функции, то вызывающая функция приостанавливается в частично завершенном состоянии"""

def greet(nick):
    print('hello' + nick + "!")
    greet2(nick)
    print('get ready to say bye..')
    bye()

def greet2(nick):
    print('How are you' + nick + '/')

def bye():
    print('Bye')

name = 'Jane'
print(greet(name))

