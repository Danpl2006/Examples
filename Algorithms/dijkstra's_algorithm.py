"""Алгоритм Дейкстры - работает отличным от алгоритма поиска в ширину способом.
Алгоритм BFS ищет кратчайшие путь по количеству ребер, а алгоритм Дейкстры по весу ребер.
Работает только с направленными ациклическими графами DAG.
Алгоритм не может использоваться для ребер с отрицательным весом.
Состоит из 4 шагов:
1) Найти узел с наименьшей стоимостью
2) Обновить стоимости соседей этого узла
3) Повторять пока это не будет сделано для всех узлов графа
4) Вычислить итоговый путь
Цикл в графе - можно начать с некоторого узла и перемещаясь по графу вернуться в тот же узел"""

processed = []

graph2 = {
    'start': {'a': 6, 'b': 2},
    'a': {'fin': 1},
    'b': {'a': 3, 'fin': 5},
    'fin': {}
}

infinity = float('inf')

costs = {
    'a': 6,
    'b': 2,
    'fin': infinity
}

parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}

def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # Перебрать все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # Если это узел с наименьшей стоимостью из уже виденный и он не был обработан
            lowest_cost = cost  # Он назначается новым узлом с наименьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node

# Основной алгоритм
node = find_lowest_cost_node(costs, processed)  # Передаем processed

while node is not None:
    cost = costs[node]
    neighbors = graph2[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    node = find_lowest_cost_node(costs, processed)  # Снова передаем

print("Итоговые стоимости:", costs)
print("Родители:", parents)
print("Кратчайший путь до fin стоит: ", costs['fin'])

