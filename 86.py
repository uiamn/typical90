N, Q = map(int, input().split())
bitwidth = 60
MOD = 1000000007

X = [[] for _ in range(bitwidth + 1)]
Y = [[False for _ in range(bitwidth + 1)] for __ in range(N+1)]

bit = lambda x, i: (x >> (i-1)) & 1

for i in range(Q):
    x, y, z, w = map(int, input().split())

    for j in range(1, bitwidth + 1):
        if bit(w, j) == 0:
            Y[x][j] = 1
            Y[y][j] = 1
            Y[z][j] = 1
        else:
            X[j].append([x, y, z])

ans = 1

for j in range(1, bitwidth + 1):
    cnt = 0
    for assign in range(2**N):
        for i in range(1, N+1):
            if bit(assign, i) and Y[i][j]:
                # 0 に assign されなければならないものが 1 になってゐるので除外
                break
        else:
            # assign が X[j] を充足するか？
            for clause in X[j]:
                if bit(assign, clause[0]) or bit(assign, clause[1]) or bit(assign, clause[2]):
                    pass
                else:
                    # assign は clause を充足しない
                    break
            else:
                # 全ての節が充足してゐた
                cnt += 1

    ans *= cnt
    ans %= MOD

print(ans)
