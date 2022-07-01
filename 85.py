def divisors(n: int):
    res = []
    for i in range(1, n+1):
        if i ** 2 > n:
            break
        if n % i != 0:
            continue

        res.append(i)
        if n // i != i:
            res.append(n // i)

    return res

K = int(input())
res = 0

for a in range(1, K+1):
    if a**3 > K:
        break

    if K % a != 0:
        continue

    divs = divisors(K // a)

    if len(divs) % 2 == 0:
        n_inappropriate = len(list(filter(lambda x: x < a, divs))) * 2
        res += (len(divs) - n_inappropriate) // 2
    else:
        n_inappropriate = len(list(filter(lambda x: x < a, divs))) * 2
        res += (max(len(divs) - n_inappropriate, 0) + 1) // 2


print(res)
