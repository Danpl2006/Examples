"""Стратегия 'разделяй и властвуй' состоит из двух шагов:
1) Сначала определяется базовый случай. Это должен быть простейший случай из всех возможных
2) Задача делится или сокращается до тех пор, пока не будет сведена к базовому случаю.
Ссылка на алгоритм Евклида(https://ru.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm)
Быстрая сортировка - сначала выбирается опорный элемент, далее находим элементы меньшие опорного и элементы большие опорного,
разделить массив на два подмассива, рекурсивно применить быструю сортировку к двум подмассивам
O(n) - O(n^2) в худшем случае, O(n log n) - в среднем"""

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return  quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([9, 43,434, 2412, 14, 63, 76]))




