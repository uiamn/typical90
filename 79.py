H, W = map(int, input().split())
A = []
diff = []

for _ in range(H):
    A.append(list(map(int, input().split())))

for row in A:
    b_row = list(map(int, input().split()))
    diff.append([a-b for a, b in zip(row, b_row)])

count = 0
for i in range(H-1):
    for j in range(W-1):
        diff_ij = diff[i][j]
        count += abs(diff_ij)
        diff[i+1][j] -= diff_ij
        diff[i][j+1] -= diff_ij
        diff[i+1][j+1] -= diff_ij
        diff[i][j] = 0

    if diff[i][W-1] != 0:
        print('No')
        exit()

for j in range(W):
    if diff[H-1][j] != 0:
        print('No')
        exit()

print('Yes')
print(count)
