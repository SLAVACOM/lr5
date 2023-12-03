import csv

import heapq as hq
from pandas import *
import pandas as pd

pd.set_option('display.expand_frame_repr', False)

graph = []
start = end = 0

def read_graph():
    with open('Книга1.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        next(spamreader)
        for row in spamreader:
            rw = row[0].split(";")[1:]
            data = []
            for j in range(len(rw)):
                if rw[j] == "":
                    rw[j] = "inf"

            for i in range(len(rw)):
                data.append(float(rw[i]) )
            graph.append(data)
    print(DataFrame(graph))

def dijkstra(G, start):
    n = len(G)

    Q = [(0, start)]

    d = [float("inf") for _ in range(n)]
    d[start] = 0
    while len(Q) != 0:
        (cost, u) = hq.heappop(Q)
        for v in range(n):
            if d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                Q.append((d[v], v))
    return d

def get_path(end):
    global d, start_pos
    n = len(graph)

    path = [end]
    while end != start_pos:
        for i in range(n):
            if d[i] == d[end] - graph[end][i]:
                path.append(i)
                end = i
    return path[::-1]

read_graph()


start_pos = end_pos = -1

while start_pos == -1:
    start_pos = int(input(f"Введите начальный пункт (число от 0 до {len(graph)-1} включительно): "))
    if ( (start_pos >= len(graph)) or (start_pos < 0)):
        start_pos = -1
        print("ОШИБКА!!!\nВы ввели неправильный начальный пункт")

while end_pos == -1:
    end_pos = int(input(f"Введите конечный пункт (число от 0 до {len(graph) - 1} включительно): "))
    if ((end_pos >= len(graph)) or (start_pos < 0)):
        end_pos = -1
        print("ОШИБКА!!!\nВы ввели неправильный конечный пункт")

d = dijkstra(graph,start_pos)

print(f"Минимальная протяженность дороги от пунтка №{start_pos} до пунта №{end_pos} составляет {d[end_pos]}")
print("Его путь:",*get_path(end_pos))

