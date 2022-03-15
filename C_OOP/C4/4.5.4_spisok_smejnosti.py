G = {
    "Адмиралтейская": {
        "Садовая": 4},
    "Садовая": {
        "Сенная площадь": 4,
        "Спасская": 3,
        "Адмиралтейская": 4,
        "Звенигородская": 5},
    "Сенная площадь": {
        "Садовая": 4,
        "Спасская": 4},
    "Спасская": {
        "Садовая": 3,
        "Сенная площадь": 4,
        "Достоевская": 6},
    "Звенигородская": {
        "Пушкинская": 3,
        "Садовая": 5},
    "Пушкинская": {
        "Звенигородская": 3,
        "Владимирская": 4},
    "Владимирская": {
        "Достоевская": 3,
        "Пушкинская": 4},
    "Достоевская": {
        "Владимирская": 3,
        "Спасская": 6}
}

D = {k : 100 for k in G.keys()}  # расстояния
start_k = 'Адмиралтейская'  # стартовая вершина
D[start_k] = 0  # расстояние от нее до самой себя равно нулю
U = {k : False for k in G.keys()}  # флаги просмотра вершин
P = {k : None for k in G.keys()}  # предки

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])

    for v in G[min_k].keys():  # проходимся по всем смежным вершинам
         if D[v] > D[min_k] + G[min_k][v]:  # если расстояние от текущей вершины меньше
            D[v] = D[min_k] + G[min_k][v]  # то фиксируем его
            P[v] = min_k  # и записываем как предок
    U[min_k] = True  # просмотренную вершину помечаем

pointer = 'Владимирская'  # куда должны прийти
while pointer is not None:  # перемещаемся, пока не придем в стартовую точку
    print(pointer)
    pointer = P[pointer]
# import math

# print(round(10_000**2 / (10_000*math.log2(10_000))))