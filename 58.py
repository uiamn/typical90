"""
以下の表は，最初に表示されてゐる数字 (最後に到達する数字, ボタンを押した回数) を表す．
    1 (10, 4741)
    2 (10, 4740)
    3 (20, 4606)
    4 (10, 4739)
    5 (10, 4736)
    6 (20, 4605)
    7 (10, 4737)
    8 (10, 4738)
    9 (44, 4743)
    10 (10, 4735)
    11 (10, 4734)
    12 (20, 4604)
    13 (10, 4733)
    14 (10, 4736)
    15 (20, 4603)
    16 (10, 4737)
    17 (10, 4732)
    18 (44, 4742)
    19 (10, 4735)
    20 (10, 4734)
    21 (20, 4602)
    22 (10, 4733)
    23 (10, 4736)
    24 (20, 4601)
    25 (10, 4731)
    26 (10, 4732)
    27 (44, 4741)
    28 (10, 4735)
    29 (10, 4734)
    30 (20, 4600)
    31 (10, 4733)
    32 (10, 4730)
    33 (20, 4599)
    34 (10, 4731)
    35 (10, 4732)
    36 (44, 4740)
    37 (10, 4729)
    38 (10, 4734)
    39 (20, 4598)
    40 (10, 4733)
    41 (10, 4730)
    42 (20, 4599)
    43 (10, 4731)
    44 (10, 4732)
これより，最初にどんな数字が表示されてゐても，約 2 万回程度ボタンを押せば 10 になることがわかる．
（途中で 0 になるケースを除く）
"""

def push_button(n: int) -> int:
    y = sum(map(int, str(n)))
    return (n + y) % (10**5)

N, K = map(int, input().split())
ctr = 0

for _ in range(K):
    old = N
    N = push_button(N)
    ctr += 1

    if N == 0:
        print(0)
        exit(0)

    if N == 10:
        break
else:
    # K 回押し終はった場合
    print(N)
    exit(0)

# 今 ctr 回ボタンを押した状態で 10 が表示されてゐる
# 10 が表示された状態で 4735 回ボタンを押すと再び 10 が表示される
rem = (K-ctr) % 4735

for _ in range(rem):
    N = push_button(N)

print(N)
