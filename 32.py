import itertools

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

bad = [[] for _ in range(N)]
M = int(input())
for _ in range(M):
    X, Y = map(int, input().split())
    bad[X-1].append(Y-1)
    bad[Y-1].append(X-1)

answer = 10**8
calc_time = lambda order: sum([A[runner][i] for i, runner in enumerate(order)])
is_bad_order = lambda order: any(order[i] in bad[order[i+1]] for i in range(N-1))

for p in itertools.permutations(range(N), N):
    if is_bad_order(p):
        continue

    answer = min(calc_time(p), answer)

if answer == 10**8:
    print(-1)
else:
    print(answer)
