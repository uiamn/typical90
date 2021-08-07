N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

fubensa = 0

for a, b in zip(A, B):
    fubensa += abs(a-b)

print(fubensa)
