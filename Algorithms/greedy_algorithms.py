"""Жадные алгоритмы - приближенные и по возможности оптимальные.
Идет оптимизация локальная, что приводит к локализации глобальной
Объединение множеств означает слияние элементов обоих множеств. Под операцией пересечения
множеств понимается поиск элементов, входящих в оба множества. Под разностью множеств
понимается исключение из одного множества элементов, присутствующих в другом множестве."""

states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

stations = {}
final_stations = set()
stations["kone"] = {"id", "nv", "ut"}
stations["ktwo"] = {"wa", "id", "mt"}
stations["kthree"] = {"or", "nv", "ca"}
stations["kfour"] = {"nv", "ut"}
stations["kfive"] = {"ca", "az"}

while states_needed:
    best_station = None
    states_covered = set()

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)


print(final_stations)


