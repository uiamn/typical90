_, L = list(map(int, input().split()))
K = int(input())
A = list(map(int, input().split()))

head = 0
tail = 10**9

while 1:
    pivot = (head+tail) // 2
    try:
        last_kireme = 0
        last_kireme_idx = 0
        for _ in range(K):
            i = last_kireme_idx
            while A[i] - last_kireme < pivot:
                i += 1

            last_kireme = A[i]
            last_kireme_idx = i

        if L - last_kireme < pivot:
            tail = pivot
        else:
            head = pivot

    except:
        tail = pivot

    if tail - head < 2:
        print(head)
        exit()


