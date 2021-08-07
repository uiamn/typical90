H, W = list(map(int, input().split()))
mat = [list(map(int, input().split())) for _ in range(H)]

row_sum = [sum(r) for r in mat]
col_sum = [sum([mat[j][i] for j in range(H)]) for i in range(W)]

for i in range(H):
    print(' '.join([str(row_sum[i]+col_sum[j]-mat[i][j]) for j in range(W)]))
