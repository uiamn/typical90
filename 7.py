N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A.sort()

def nibutan(sorted_A, b):
    head = 0
    tail = len(sorted_A) - 1

    while tail - head > 1:
        pivot = (head+tail) // 2
        if sorted_A[pivot] >= b:
            tail = pivot
        else:
            head = pivot

    return head, tail

for _ in range(Q):
    B = int(input())
    h, t = nibutan(A, B)
    print(min(abs(B-A[h]), abs(A[t]-B)))


