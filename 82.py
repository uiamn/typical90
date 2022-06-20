L, R = map(int, input().split())
MOD = 10**9 + 7

sum_p_to_q = lambda p, q: (((p+q)*(q-p+1))//2)

l_digit = len(str(L))
r_digit = len(str(R))

# 桁数が同じなら L から R までの和にその桁数をかけて終了
if l_digit == r_digit:
    print((l_digit * sum_p_to_q(L, R)) % MOD)
    exit()

"""
先に 10**(n-1) から 10**n - 1 まで操作を行ったときに黒板に追加される文字数を求めておく．これらの数はすべて n 桁の数であり， p から q まで操作を行ったときに書かれる"整数"の個数は (p+q)(q-p+1)/2 なので，
"""

chars = []
for n in range(19):
    chars.append(n * sum_p_to_q(10**(n-1), 10**n - 1))

"""
L の桁数を Ld, R の桁数を Rd とすると，答へは
    chars[Ld+1] + ... + chars[Rd-1]
に
    (L から 10**(Ld)-1 までの和)*Ld + (10**(Rd-1) から R までの和)
を加えたもの
"""

answer = l_digit*sum_p_to_q(L, 10**l_digit-1) + r_digit*sum_p_to_q(10**(r_digit-1), R)
answer %= MOD

for i in range(l_digit+1, r_digit):
    answer += chars[i]
    answer %= MOD

print(answer)
