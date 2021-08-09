import math

A, B, C = list(map(int, input().split()))

l = math.gcd(math.gcd(A, B), C)

print(f'{A//l + B//l + C//l - 3}')
