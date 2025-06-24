import networkx as nx
import matplotlib.pyplot as plt

edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('A', 'G', 7),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('B', 'G', 6),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('C', 'G', 3),
    ('D', 'E', 2),
    ('D', 'G', 9),
    ('E', 'G', 5)
]

G = nx.Graph()
G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G, seed=42)  # Posisi simpul tetap konsisten

plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=12)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})

plt.title("Jaringan Distribusi Listrik Sebelum MST", fontsize=14)
plt.axis('off')
plt.show()
