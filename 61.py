import collections

Q = int(input())
deque = collections.deque()

for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        deque.appendleft(x)
    elif t == 2:
        deque.append(x)
    else:
        print(deque[x-1])
