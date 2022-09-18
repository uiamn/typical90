import itertools

def set_partitions(iterable, k=None):
    L = list(iterable)
    n = len(L)
    if k is not None:
        if k < 1:
            raise ValueError(
                "Can't partition in a negative or zero number of groups"
            )
        elif k > n:
            return

    def set_partitions_helper(L, k):
        n = len(L)
        if k == 1:
            yield [L]
        elif n == k:
            yield [[s] for s in L]
        else:
            e, *M = L
            for p in set_partitions_helper(M, k - 1):
                yield [[e], *p]
            for p in set_partitions_helper(M, k):
                for i in range(len(p)):
                    yield p[:i] + [[e] + p[i]] + p[i + 1 :]

    if k is None:
        for k in range(1, n + 1):
            yield from set_partitions_helper(L, k)
    else:
        yield from set_partitions_helper(L, k)


N, K = map(int, input().split())
points = []

for _ in range(N):
    points.append(tuple(map(int, input().split())))

# dist[i][j] = 点 i+1 と点 j+1 の距離の平方．
distsq = [[None for __ in range(N)] for _ in range(N)]

for i in range(N-1):
    for j in range(1, N):
        d = (points[j][0] - points[i][0]) ** 2 + (points[j][1] - points[i][1]) ** 2
        distsq[i][j] = d
        distsq[j][i] = d

result = (2* (10**9)) ** 2
for partition in set_partitions(list(range(N)), K):
    tmp = 0  # この分割における同一グループ内での 2 点間距離の最大値
    for part in partition:
        if len(part) == 1:
            continue

        for c in itertools.combinations(part, 2):
            if distsq[c[0]][c[1]] > tmp:
                tmp = distsq[c[0]][c[1]]

    result = min(result, tmp)

print(result)
