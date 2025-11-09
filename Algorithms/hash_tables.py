"""Хэш-функция - связывает строки с числами(индексами). Функция знает размер массива и
возвращает только действительные индексы. В хэш таблице существуют коллизии - когда под значение выделяется один и тот же элемент
массива и образуется связный список
скорость структуры данных O(1) то есть за постоянное время - будь то 1 элемент или миллиард выборка данных займет одинаковое время"""

book = dict()
book['apple'] = 0.67
book['milk'] = 1.4
book['avocado'] = 0.57
print(book['avocado'])

voted = {}
def  check_vote(name):
    if voted.get(name):
        print("kick them out")
    else:
        voted[name] = True
        print("let them vote")

print(check_vote('tom'))
print(check_vote('tom'))
print(check_vote('Red'))
print(check_vote('red'))


cache = {}
def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = None
        cache[url] = data
        return data
print(get_page('https://google.com'))
print(get_page('https://google.com'))