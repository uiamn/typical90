N = int(input())
S = input()

index = 0
c = S[index]

a = []

while index < N:
    last_index = index
    while index < N and c == S[index]:
        index += 1

    if index < N:
        c = S[index]

    a.append(index - last_index)

b = [c*(c-1)//2 for c in a]
print((N*(N-1) // 2) - sum(b))

