# Struktur Union-Find
class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_b] = root_a
            return True
        return False

# Algoritma Kruskal
def kruskal(edges, nodes):
    uf = UnionFind(nodes)
    mst = []
    total_weight = 0
    for weight, u, v in sorted(edges):
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
    return mst, total_weight
