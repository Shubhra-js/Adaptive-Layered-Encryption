import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes (people/routers)
G.add_nodes_from(["Alice", "Bob", "R1", "R2", "R3"])

# Add edges (connections)
G.add_edges_from([
    ("Alice", "R1"), ("R1", "R2"), ("R2", "Bob"),  # Path 1
    ("Alice", "R3"), ("R3", "Bob")                # Path 2
])

# Find shortest paths from Alice to Bob
all_paths = list(nx.all_simple_paths(G, source="Alice", target="Bob"))

print("All possible paths from Alice to Bob:")
for path in all_paths:
    print(path, " -> Hops:", len(path)-1)
