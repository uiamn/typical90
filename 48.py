import heapq

# すべてにおいて A と B が逆

A = []
B = []

N, K = map(int, input().split())

class Node():
    def __init__(self, is_a: bool, index: int, value: int) -> None:
        self.is_a = is_a
        self.index = index
        self.value = value

    def __lt__(self, other):
        # value が大きい方が大きい
        if self.value < other.value:
            return True
        elif self.value > other.value:
            return False

        # value が同じで片方が B の元なら， B の元の方が小さい
        if self.is_a and not other.is_a:
            return False
        elif not self.is_a and other.is_a:
            return True

        # value が同じで両方 A の元なら， B の元の大小で比較
        if self.is_a and other.is_a:
            if B[self.index] < B[other.index]:
                return True
            elif B[self.index] > B[other.index]:
                return False
            else:
                # それも等しいなら等しい
                return False
        else:
            # value が同じで両方 B の元なら，等しい
            return False

    def __eq__(self, other):
        if self.value != other.value:
            return False

        if self.is_a and other.is_a and B[self.index] == B[other.index]:
            return True
        elif (not self.is_a) and (not other.is_a):
            return True

        return False

for _ in range(N):
    a, b = map(int, input().split())

    # 最小ヒープなので -1 倍した値を格納する
    # A と B が逆転してゐる
    A.append(-b)
    B.append(-a+b)

nodes = []
for i, a in enumerate(A):
    nodes.append(Node(True, i, a))

heapq.heapify(nodes)

result = 0
for _ in range(K):
    n = heapq.heappop(nodes)
    result += n.value
    if n.is_a:
        heapq.heappush(nodes, Node(False, n.index, B[n.index]))

print(-result)
