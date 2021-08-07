N = int(input())

ichikumi = [0]
ichikumi_wa = 0
nikumi = [0]
nikumi_wa = 0

for _ in range(N):
    c, p = list(map(int, input().split()))
    if c == 1:
        ichikumi_wa += p
    else:
        nikumi_wa += p

    ichikumi.append(ichikumi_wa)
    nikumi.append(nikumi_wa)

Q = int(input())

for _ in range(Q):
    l, r = list(map(int, input().split()))

    print(f'{ichikumi[r] - ichikumi[l-1]} {nikumi[r] - nikumi[l-1]}')
