# Примеры функций
def func_1(x): return x ** 2
def func_2(x): return x ** 4
def func_3(x): return x ** 6

callback = [func_1, func_2, func_3]

print("\nName func")
for i in callback: print("Res:", i(5))

callback = \
[lambda x: x ** 2, lambda x: x ** 4, lambda x: x ** 6]

print("\nName anonymous func")
for i in callback: print("Res:", i(5))