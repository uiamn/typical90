import sys
sys.setrecursionlimit(100000)

K = int(input())

if K % 9 != 0:
    print(0)
    exit(0)

MOD = 10**9 + 7
memo = [None for _ in range(100000)]

for i in range(9):
    memo[i+1] = 2 ** i

def f(n: int) -> int:
    # n の順序付きの分割であって，各項の最大値が 9 であるものの個数を返す
    if memo[n] is not None:
        return memo[n]
    else:
        res = 0
        for i in range(1, 10):
            res += f(n-i)

        memo[n] = res % MOD
        return res % MOD

print(f(K))
