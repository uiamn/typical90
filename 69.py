N, K = map(int, input().split())

if N == 1:
    print(K)
    exit()

if N == 2:
    print(K*(K-1))
    exit()

if K == 1 or K == 2:
    print(0)
    exit()

MOD = 10**9 + 7
print((K*(K-1)*(pow(K-2, N-2, MOD))) % MOD)
