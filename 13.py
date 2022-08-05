import heapq
from typing import List

# 優先度付き Dijkstra
class ToNode:
    def __init__(self, to: int, cost: int) -> None:
        self.to = to
        self.cost = cost

def dijkstra(n_nodes: int, adj: List[ToNode], begin: int, INF: int = 2**64-1):
    class Node:
        def __init__(self, index, min_cost) -> None:
            self.index = index
            self.min_cost = min_cost

        def __lt__(self, other) -> bool:
            return self.min_cost < other.min_cost

    q = []
    begin_node = Node(begin, 0)
    heapq.heappush(q, begin_node)
    min_cost = [INF for _ in range(n_nodes+1)]

    while len(q) != 0:
        node = heapq.heappop(q)

        if min_cost[node.index] != INF:
            continue

        min_cost[node.index] = node.min_cost
        for to_node in adj[node.index]:
            new_node = Node(to_node.to, node.min_cost + to_node.cost)
            heapq.heappush(q, new_node)

    return min_cost


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())

    adj[a].append(ToNode(b, c))
    adj[b].append(ToNode(a, c))

cost_from_1 = dijkstra(N, adj, 1)
cost_from_N = dijkstra(N, adj, N)

for i in range(1, N+1):
    print(cost_from_1[i] + cost_from_N[i])
