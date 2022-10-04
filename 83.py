N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

Q = int(input())

color = {i: 1 for i in range(1, N+1)}

for _ in range(Q):
    x, y = map(int, input().split())

    print(color[x])

    color[x] = y
    for n in graph[x]:
        color[n] = y
