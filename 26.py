N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

node = 1
distances = [None for _ in range(N+1)]
is_visited = [False for _ in range(N+1)]
next_nodes = [node]
dist = 0

odd_node = []
even_node = []

while next_nodes:
    tmp = []
    for n in next_nodes:
        if not is_visited[n]:
            is_visited[n] = True
            tmp += graph[n]
            if dist % 2:
                odd_node.append(str(n))
            else:
                even_node.append(str(n))

    next_nodes = tmp
    dist += 1

if len(odd_node) >= N // 2:
    print(' '.join(odd_node[:N//2]))
else:
    print(' '.join(even_node[:N//2]))
