a_mod46_nums = [0 for _ in range(46)]
b_mod46_nums = [0 for _ in range(46)]
c_mod46_nums = [0 for _ in range(46)]

N = int(input())
for a in input().split():
    a_mod46_nums[int(a) % 46] += 1

for b in input().split():
    b_mod46_nums[int(b) % 46] += 1

for c in input().split():
    c_mod46_nums[int(c) % 46] += 1

# 和が 0， 46， 92 になる組み合はせの総数を求めれば良い
answer = 0

# 和が 0
answer += a_mod46_nums[0] * b_mod46_nums[0] * c_mod46_nums[0]

# 和が 46
for i in range(46):
    for j in range(46 - i + 1):
        k = 46 - i - j
        if j >= 46 or k >= 46:
            continue
        answer += a_mod46_nums[i] * b_mod46_nums[j] * c_mod46_nums[k]

# 和が 92
for i in range(46):
    for j in range(46):
        k = 92 - i - j
        if k >= 46:
            continue
        answer += a_mod46_nums[i] * b_mod46_nums[j] * c_mod46_nums[k]

print(answer)
