MOD = 10**9 + 7

N = int(input())
answer = 1

for _ in range(N):
    A = sum(map(int, input().split()))
    answer *= A
    answer %= MOD

print(answer)
