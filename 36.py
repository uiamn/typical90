N, Q = map(int, input().split())

xpy = []  # 各点の x 座標と y 座標の和
xmy = []  # 各店の x 座標から y 座標を引いたもの

xpymax = 0
xpymin = 10**10
xmymax = 0
xmymin = 10**10

for _ in range(N):
    x, y = map(int, input().split())
    xpy.append(x+y)
    xmy.append(x-y)
    xpymax = max(x+y, xpymax)
    xpymin = min(x+y, xpymin)
    xmymax = max(x-y, xmymax)
    xmymin = min(x-y, xmymin)

for _ in range(Q):
    q = int(input()) - 1
    print(max(xpy[q] - xpymin, xmy[q] - xmymin, -xmy[q]+xmymax, -xpy[q]+xpymax))
