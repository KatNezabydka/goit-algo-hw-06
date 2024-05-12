import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(["Kate", "Nick", "Charlie", "David", "Natalia", "Frank", "Mike"])

G.add_edges_from([("Kate", "Nick"), ("Kate", "Charlie"), ("Nick", "David"), ("Charlie", "David"),
                  ("Charlie", "Natalia"), ("David", "Natalia"), ("Natalia", "Frank"), ("Natalia", "Mike"),
                  ("Frank", "Mike")])

nx.draw(G, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")
plt.title("Social network")
plt.show()

print("Vertices count:", G.number_of_nodes())
print("Edges count:", G.number_of_edges())

degrees = dict(G.degree())
print("Degree of vertices:", degrees)
