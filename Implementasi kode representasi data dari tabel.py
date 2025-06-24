# Daftar sisi dengan format: (bobot, simpul1, simpul2)
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

# Menampilkan semua sisi
print("Graf Berbobot (Distribusi Listrik):")
for weight, u, v in edges:
    print(f"{u} -- {weight}m -- {v}")
