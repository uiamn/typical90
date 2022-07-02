H, W = map(int, input().split())

P = []

for _ in range(H):
    P.append(list(map(int, input().split())))

result = 0

"""
行数が最大 8 なので，どの行を採用するか全探索
    各列を見ていき，採用する行についてすべて同じ数字を持ってゐたら，その数字のカウントを 1 上げる
    最も大きいカウント * 行数 で結果を更新
"""

for b in range(1, 1 << H):
    row_ids = []
    for i in range(H):
        if (b >> i) & 1:
            row_ids.append(i)

    num_ctr = {0: 0}
    for j in range(W):
        common_v = P[row_ids[0]][j]
        for r in row_ids[1:]:
            if P[r][j] != common_v:
                break
        else:
            if common_v in num_ctr:
                num_ctr[common_v] += 1
            else:
                num_ctr[common_v] = 1

    result = max(max(num_ctr.values()) * len(row_ids), result)

print(result)
