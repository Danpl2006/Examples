""" Бинарный поиск — это алгоритм поиска элемента в отсортированном списке.
    Он работает следующим образом:
    Находит середину списка и сравнивает этот элемент с искомым значением.
    Если значение равно среднему элементу — поиск завершён.
    Если значение меньше — алгоритм повторяет поиск в левой половине списка.
    Если значение больше — алгоритм ищет в правой половине.
    Сложность: O(log n)"""

def binary_searh(list, item):
    low = 0  # Нижняя граница
    high = len(list) - 1 # Высшая граница
    while low <= high: # Цикл сравнения середины элемента
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

spisok = [i for i in range(1, 10000)]

spisok_names = ["Ваня", "Dany", "Mickle", "Mica", "Geralt", "Маша"]
spisok_names.sort()

print(binary_searh(spisok, 5535))
