N = int(input())
S = input()
mod = 10**9+7
atcoder = 'atcoder'

dp = [[1] + [0 for _ in range(7)] for __ in range(N)]
dp[0][0] = 1

for i, c in enumerate(S):
    for j in range(1, 8):
        if c == atcoder[j-1]:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])
