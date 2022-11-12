def mex(l):
    for i in range(51*51):
        if i not in l:
            return i

cache = {(0, 0): 0, (0, 1): 0}
def grundy(w, b):
    a = cache.get((w, b))

    if a is not None:
        return a
    else:
        candidate = set([])
        if w == 0:
            for i in range(1, b//2 + 1):
                candidate.add(grundy(w, b-i))
        elif b == 0 or b == 1:
            candidate.add(grundy(w-1, b+w))
        else:
            candidate.add(grundy(w-1, b+w))
            for i in range(1, b // 2 + 1):
                candidate.add(grundy(w, b-i))

        g = mex(candidate)
        cache[(w, b)] = g
        return g

N = int(input())
W = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans ^= grundy(W[i], B[i])

if ans == 0:
    print('Second')
else:
    print('First')
