def solve_sub(graph, x, N, P):
    # X = x としたとき， P スヌーク以下， P+1 スヌーク以下で移動できる街の組の個数を返す
    d = [[v if v != -1 else x for v in row] for row in graph]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    cnt = 0
    for i in range(N-1):
        for j in range(i, N):
            if i != j and d[i][j] <= P:
                cnt += 1

    return cnt


def solve(graph, N, P, K):
    # P スヌーク以下で到達可能であるような組が K
    head = 0
    tail = P+2

    while tail - head > 1:
        pivot = (head + tail) // 2

        a = solve_sub(graph, pivot, N, P)

        if a >= K:
            head = pivot
        else:
            tail = pivot

    return head

N, P, K = map(int, input().split())

fee = []

for _ in range(N):
    fee.append(list(map(int, input().split())))

a = solve(fee, N, P, K)
b = solve(fee, N, P, K+1)

if b == P+1:
    print(0)
elif a == P+1:
    print('Infinity')
else:
    print(a-b)
