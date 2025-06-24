mst_result, total_length = kruskal(edges, nodes)

print("Minimum Spanning Tree (MST):")
for u, v, weight in mst_result:
    print(f"{u} - {v} : {weight}")
print(f"\nTotal panjang kabel minimum (MST): {total_length}")
