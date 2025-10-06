"""Сортировка выбором - проходим по массиву слева направо, находим
минимальный элемент и меняем его местами
с первым (текущим) элементом. Увеличиваем границу отсортированной
части массива на один элемент и повторяем процесс
для оставшейся части.
Сложность: O(n^2) """

def find_Smallest(arr):
    smallest = arr[0] # Хранение наименьшего значения
    smallest_index = 0 # Хранение наименьшего индекса значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_Smallest(arr) # Находит наименьший элемент в массиве и добавляет в новый
        new_arr.append(arr.pop(smallest))
    return new_arr

print(selection_sort([5, 3, 6, 2, 10]))
