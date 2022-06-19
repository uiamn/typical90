N = int(input())
A = list(map(int, input().split()))
cake_size = sum(A)

if cake_size % 10 != 0:
    print('No')
    exit()

target = cake_size // 10

head = 0
tail = 1
size = A[0]
A += A

while head < N:
    while size < target:
        size += A[tail]
        tail += 1

    if size == target:
        print('Yes')
        exit()

    while size > target:
        size -= A[head]
        head += 1

    if size == target:
        print('Yes')
        exit()

print('No')
