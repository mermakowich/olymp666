MOD = 998244353

# Чтение входных данных
n, m = map(int, input().split())
parents = list(map(int, input().split()))

# Построение дерева
from collections import defaultdict
graph = defaultdict(list)
for i in range(n - 1):
    graph[parents[i] - 1].append(i + 1)
    graph[i + 1].append(parents[i] - 1)

# Чтение скуфов
queries = []
for _ in range(m):
    u, v = map(int, input().split())
    queries.append((u - 1, v - 1))

# Функция для нахождения четности пути между двумя вершинами
def dfs(v, parent, parity, parities):
    parities[v] = parity
    for neighbor in graph[v]:
        if neighbor != parent:
            dfs(neighbor, v, 1 - parity, parities)

# Четность всех вершин относительно корня
parities = [-1] * n
dfs(0, -1, 0, parities)

# Проверка всех запросов
conditions = []
for u, v in queries:
    if parities[u] == parities[v]:
        conditions.append(0)  # Четный путь
    else:
        conditions.append(1)  # Нечетный путь

# Подсчет способов назначения длин дорог
result = 1
for cond in conditions:
    if cond == 1:
        result = (result * 2) % MOD

print(result)
