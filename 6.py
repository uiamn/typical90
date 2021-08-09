N, K = list(map(int, input().split()))
S = input()

result = ''
result_len = 0
head = 0
dk = K

while result_len < K:
    r = N-head-dk
    c = S[head]
    best_i = 0
    for i in range(1, r+1):
        if c > S[head+i]:
            c = S[head+i]
            best_i = i

    result += c
    head += best_i+1
    result_len += 1
    dk -= 1

print(result)
