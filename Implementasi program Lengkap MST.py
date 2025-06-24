# Daftar sisi berdasarkan tabel (tidak termasuk diagonal dan nilai '-')
edges = [
    (4, 'A', 'B'),
    (2, 'A', 'C'),
    (7, 'A', 'G'),
    (1, 'B', 'C'),
    (5, 'B', 'D'),
    (6, 'B', 'G'),
    (8, 'C', 'D'),
    (10, 'C', 'E'),
    (3, 'C', 'G'),
    (2, 'D', 'E'),
    (9, 'D', 'G'),
    (5, 'E', 'G')
]

# Simpul unik
nodes = {'A', 'B', 'C', 'D', 'E', 'G'}
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
mst_result, total_length = kruskal(edges, nodes)

print("Minimum Spanning Tree (MST):")
for u, v, weight in mst_result:
    print(f"{u} - {v} : {weight}")
print(f"\nTotal panjang kabel minimum (MST): {total_length}")
