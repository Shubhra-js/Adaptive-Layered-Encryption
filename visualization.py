import networkx as nx
import matplotlib.pyplot as plt

# Build Graph
G = nx.Graph()
G.add_nodes_from(["Alice", "Bob", "R1", "R2", "R3", "R4", "R5", "R6", "R7"])
G.add_edges_from([
    ("Alice", "R1"), ("R1", "R2"), ("R2", "Bob"),        # Path 1 (3 hops)
    ("Alice", "R3"), ("R3", "Bob"),                      # Path 2 (2 hops)
    ("Alice", "R4"), ("R4", "R5"), ("R5", "R6"), ("R6", "Bob"), # Path 3 (4 hops)
    ("Alice", "R7"), ("R7", "Bob")                       # Path 4 (2 hops)
])

# Define paths manually (for coloring)
paths = [
    ["Alice", "R1", "R2", "Bob"],  # Path 1 (3 hops)
    ["Alice", "R3", "Bob"],        # Path 2 (2 hops)
    ["Alice", "R4", "R5", "R6", "Bob"], # Path 3 (4 hops)
    ["Alice", "R7", "Bob"]         # Path 4 (2 hops)
]

colors = ["red", "green", "blue", "orange"]  # different colors for paths

pos = nx.spring_layout(G, seed=42)  # positions nodes nicely
plt.figure(figsize=(8, 6))

# Draw all nodes first
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color="skyblue")
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

# Draw edges with different colors per path
for path, color in zip(paths, colors):
    edges = list(zip(path, path[1:]))  # pairs of consecutive nodes
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=3, edge_color=color)

plt.title("Highlighted Paths from Alice to Bob")
plt.show()
