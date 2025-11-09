"""Поиск в ширину позволяет найти кратчайшее расстояние между
двумя объектами. Очередь работает по принципу первый пришел, первый вышел.
O(V * E) V - количество вершин, E - количество ребер"""

from collections import deque

def person_is_seller(name):
    """Проверяет, является ли человек продавцом манго"""
    return name[-1] == 'm'  # Например, если имя заканчивается на 'm'


def search_mango_seller(graph, start):
    search_queue = deque()  # Создание новой очереди
    search_queue += graph[start]  # Добавляем всех друзей начального человека
    searched = set()  # Множество для отслеживания уже проверенных людей

    while search_queue:
        person = search_queue.popleft()

        # Пропускаем, если уже проверяли этого человека
        if person in searched:
            continue

        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            # Добавляем всех друзей этого человека в очередь
            search_queue += graph[person]
            searched.add(person)  # Помечаем как проверенного

    print("No mango seller found")
    return False

# Пример графа из книги
graph = {
    'you': ['alice', 'bob', 'claire'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': []
}

# Запуск поиска
search_mango_seller(graph, 'you')