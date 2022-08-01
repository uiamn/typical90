import sys
sys.setrecursionlimit(100000)

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 木構造を作り直す
tree = [[] for _ in range(N+1)]
tree[1] = graph[1]
is_visited = [False for _ in range(N+1)]

nodes = [1]

while nodes != []:
    node = nodes.pop()
    is_visited[node] = True

    children = [n for n in graph[node] if is_visited[n] == False]

    nodes += children
    tree[node] = children


# ノード 1 を頂点としたときに，各ノードの持つ子孫ノードの個数を求める．
n_children = [None for _ in range(N+1)]
is_visited = [False for _ in range(N+1)]
nodes = [1]

def calc_children(node):
    if n_children[node] is not None:
        return n_children[node]
    elif tree[node] == []:
        n_children[node] = 0
        return 0
    else:
        ans = sum([calc_children(c) for c in tree[node]]) + len(tree[node])
        n_children[node] = ans
        return ans

calc_children(1)

ans = 0
for i in range(1, N+1):
    n_child = n_children[i]
    ans += (N-(n_child+1)) * (n_child+1)

print(ans)
