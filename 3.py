import sys

N = int(input())

road = {}
for _ in range(N-1):
    a, b = list(map(int, input().split()))

    if a in road:
        road[a].append(b)
    else:
        road[a] = [b]

    if b in road:
        road[b].append(a)
    else:
        road[b] = [a]

def deepest(begin: int):
    visited = {i: False for i in range(1, N+1)}

    visited[begin] = True

    next_node = road[begin]
    d = 0
    while 1:
        tmp = []
        for n in next_node:
            if visited[n]:
                continue
            visited[n] = True
            tmp += road[n]

        if len(tmp) == 0:
            break

        d+=1
        next_node = tmp

    return next_node[0], d

a, _ = deepest(1)
_, d = deepest(a)

print(d+2)
