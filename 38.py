def gcd(a, b):
    return gcd(b, a % b) if a % b else b

def lcm(a, b):
    return a*b // gcd(a, b)


A, B = map(int, input().split())
l = lcm(A, B)
print(l if l <= 10 ** 18 else 'Large')
