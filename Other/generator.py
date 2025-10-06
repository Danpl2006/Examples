# Пример Генератора
def fib_gener():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b
fib = fib_gener()
for i in fib:
    if i > 100:
        break
    else:
        print("Generated:", i)



