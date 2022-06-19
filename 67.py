N, K = input().split()
K = int(K)

def to_9ary_num(v: int) -> str:
    if v // 9:
        return to_9ary_num(v // 9) + str(v % 9)
    return str(v % 9)


def operation(s: str) -> int:
    n_digit = len(s)
    dec = 0
    for d in range(n_digit):
        dec += int(s[d]) * (8 ** (n_digit-d-1))

    a = to_9ary_num(dec)
    return a.replace('8', '5')

for _ in range(K):
    N = operation(N)

print(N)
