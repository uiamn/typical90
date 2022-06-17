import sys
sys.setrecursionlimit(50000)

MOD = 10**9 + 7

N, L = map(int, input().split())

cache = [None for _ in range(N+1)]

def n_ways(N: int, L: int) -> int:
    if N < L:
        return 1

    if cache[N] is not None:
        return cache[N]

    n = (n_ways(N-L, L) + n_ways(N-1, L)) % MOD
    cache[N] = n
    return n

print(n_ways(N, L))
