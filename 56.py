N, S = map(int, input().split())

"""
    dp[i][j] 1 から i 日目までに丁度 j 円にできる福袋の組がある => その組
    ない => None
"""

dp = [[None for __ in range(S+1)] for _ in range(N+1)]
dp[0][0] = ''

for i in range(1, N+1):
    a, b = map(int, input().split())

    for j in range(S+1):
        if j-a >= 0 and dp[i-1][j-a] is not None:
            dp[i][j] = dp[i-1][j-a] + 'A'
        elif j-b >= 0 and dp[i-1][j-b] is not None:
            dp[i][j] = dp[i-1][j-b] + 'B'
        else:
            dp[i][j] = None

if dp[N][S] is None:
    print('Impossible')
else:
    print(''.join(dp[N][S]))
