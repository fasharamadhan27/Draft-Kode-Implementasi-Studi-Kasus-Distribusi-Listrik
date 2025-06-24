import networkx as nx
import matplotlib.pyplot as plt

# Daftar simpul (nodes)
vertices = ['A', 'B', 'C', 'D', 'E', 'G']

# Daftar sisi (edges) dan bobot
edges = [
    ('B', 'C', 1),
    ('A', 'C', 2),
    ('D', 'E', 2),
    ('C', 'G', 3),
    ('A', 'B', 4),
    ('B', 'D', 5),
    ('E', 'G', 5),
    ('B', 'G', 6),
    ('A', 'G', 7),
    ('C', 'D', 8),
    ('D', 'G', 9),
    ('C', 'E', 10)
]

# Struktur Union-Find
class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False

# Kruskal's Algorithm
uf = UnionFind(vertices)
edges.sort(key=lambda x: x[2])
mst = []
total_weight = 0

for u, v, w in edges:
    if uf.union(u, v):
        mst.append((u, v, w))
        total_weight += w
        if len(mst) == len(vertices) - 1:
            break

# Buat graf menggunakan NetworkX
G = nx.Graph()
G.add_weighted_edges_from(edges)        # Semua edge
MST = nx.Graph()
MST.add_weighted_edges_from(mst)        # Hanya MST

# Posisi node
pos = nx.spring_layout(G, seed=42)

# Gambar semua edge sebagai background (warna abu-abu)
nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='lightgray', node_size=1000, font_weight='bold')

# Gambar MST (warna biru)
nx.draw_networkx_edges(MST, pos, edge_color='blue', width=2)
nx.draw_networkx_nodes(MST, pos, node_color='skyblue', node_size=1000)

# Tambahkan label bobot
edge_labels = nx.get_edge_attributes(MST, 'weight')
nx.draw_networkx_edge_labels(MST, pos, edge_labels=edge_labels, font_color='blue')

# Judul
plt.title("Minimum Spanning Tree (MST) - Algoritma Kruskal")
plt.axis('off')
plt.tight_layout()
plt.show()
