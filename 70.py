N = int(input())
X = []
Y = []

for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()
ans_x = X[N // 2]
ans_y = Y[N // 2]

answer = 0
for x in X:
    answer += abs(x - ans_x)

for y in Y:
    answer += abs(y - ans_y)

print(answer)
