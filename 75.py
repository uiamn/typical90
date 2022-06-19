def factorize(n):
    factors = {}
    tmp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i

            factors[i] = cnt

    if tmp != 1:
        factors[tmp] = 1

    if len(factors) == 0:
        factors[n] = 1

    return factors

N = int(input())
factors = factorize(N)
s = sum(factors.values())

if s == 1:
    ans = 0
elif s == 2:
    ans = 1
else:
    # s が 2 のべきなら答へは 1 少なくなる
    if (s & (s-1)) == 0:
        ans = 0
    else:
        ans = 1

    while s >= 2:
        ans += 1
        s //= 2

print(ans)
