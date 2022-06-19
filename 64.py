N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 隣り合ふ標高の差を保存しておく
"""
    不便さ = 隣り合ふ区間の標高差の絶対値の和 なので標高差だけ知ってゐればよい．
    区間 i から j の標高が V 変化する地殻変動による標高差の変化は，
        区間 i-1 と i は E_{i-1} - E_i => E_{i-1} - E_i - V，
        区間 j と j+1 は E_j - E_{j+1} => E_j + V - E_{j+1}，
        それ以外は変動なし．
"""
diff = [0] + [A[i] - A[i+1] for i in range(N-1)] + [0]

inconvinience = 0
for i in range(N):
    inconvinience += abs(diff[i])

for _ in range(Q):
    L, R, V = map(int, input().split())
    if L != 1:
        inconvinience += abs(diff[L-1] - V) - abs(diff[L-1])
        diff[L-1] = diff[L-1] - V
    if R != N:
        inconvinience += abs(diff[R] + V) - abs(diff[R])
        diff[R] = diff[R] + V


    print(inconvinience)

