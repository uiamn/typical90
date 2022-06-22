import sys
sys.setrecursionlimit(100000)

class UnionFind():
    def __init__(self, n: int) -> None:
        self.n = n
        self.root = [-1]*n
        self.rank = [0]*n
        self.is_red = [False for _ in range(n)]

    def find(self, x: int) -> int:
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y) -> None:
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return None
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y) -> bool:
        return self.find(x) == self.find(y)




H, W = map(int, input().split())
Q = int(input())

uf = UnionFind(H*W)
c2i = lambda x, y: x + y*W

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        y = q[1] - 1
        x = q[2] - 1
        uf.is_red[c2i(x, y)] = True

        if x != 0 and uf.is_red[c2i(x-1, y)]:
            uf.unite(c2i(x-1, y), c2i(x, y))

        if x != W-1 and uf.is_red[c2i(x+1, y)]:
            uf.unite(c2i(x+1, y), c2i(x, y))

        if y != 0 and uf.is_red[c2i(x, y-1)]:
            uf.unite(c2i(x, y-1), c2i(x, y))

        if y != H-1 and uf.is_red[c2i(x, y+1)]:
            uf.unite(c2i(x, y+1), c2i(x, y))
    else:
        y1 = q[1] - 1
        x1 = q[2] - 1
        y2 = q[3] - 1
        x2 = q[4] - 1
        if (not uf.is_red[c2i(x1, y1)]) or (not uf.is_red[c2i(x2, y2)]):
            print('No')
        elif uf.same(c2i(x1, y1), c2i(x2, y2)):
            print('Yes')
        else:
            print('No')
