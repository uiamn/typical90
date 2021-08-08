N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = [abs(A[i]-B[i]) for i in range(N)]
s = sum(diff)
po = s - K

if po > 0 or po % 2 != 0:
    print('No')
else:
    print('Yes')
