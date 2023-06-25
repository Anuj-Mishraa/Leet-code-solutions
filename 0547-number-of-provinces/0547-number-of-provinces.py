class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n
        self.size = 1
    def find(self, u):
        if u != self.par[u]:
            self.par[u] = self.find(self.par[u])
        return self.par[u]
    def union(self, u, v):
        uu, vv = self.find(u), self.find(v)
        if uu == vv:
            return False
        if self.rank[uu] > self.rank[vv]:
            self.par[vv] = uu
        elif self.rank[vv] > self.rank[uu]:
            self.par[uu] = vv
        else:
            self.par[uu] = vv
            self.rank[vv] += 1
        self.size += 1
        return True

class Solution:
    def isConnected(self, u, v, G):
        return G[u][v] == 1

    def findCircleNum(self, G: List[List[int]]) -> int:
        n = len(G)
        uf = DSU(n)
        if not G:
            return 0
        for u in range(n):
            for v in range(u, n):
                if self.isConnected(u, v, G):
                    uf.union(u, v)
        return len(set([uf.find(i) for i in range(n)]))