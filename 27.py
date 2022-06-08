data = {}

N = int(input())

for i in range(1, N+1):
    s = input()
    if s in data:
        continue
    else:
        data[s] = 1
        print(i)
