N, K = map(int, input().split())
a = list(map(int, input().split()))

head = 0
p = 0
answer = 0
num_kind = 0
nums = set([])
counter = {}  # 何が何個入ってるか

while p < N:
    if a[p] in nums:
        if a[p] in counter:
            counter[a[p]] += 1
        else:
            counter[a[p]] = 1
    else:
        num_kind += 1
        nums.add(a[p])
        counter[a[p]] = 1
        if num_kind > K:
            answer = max(answer, p - head)
            # どれかの文字が head ~ p までに 1 回も現れなくなるまで， head を移動する
            while 1:
                num = a[head]
                count = counter[num]
                counter[num] -= 1
                head += 1

                if count == 1:
                    nums.discard(num)
                    break

    p += 1

print(max(answer, N - head))
