N, M = map(int, input().split())

n_proper_neightbors = [0 for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    n_proper_neightbors[max(a-1, b-1)] += 1

print(sum([1 for n in n_proper_neightbors if n == 1]))
