import collections


N, Q = map(int, input().split())
A = map(int, input().split())

deque = collections.deque(A)

for _ in range(Q):
    T, x, y = map(int, input().split())
    if T == 1:
        deque[x-1], deque[y-1] = deque[y-1], deque[x-1]
    elif T == 2:
        deque.rotate()
    else:
        print(deque[x-1])
