
from collections import namedtuple

Graph = namedtuple("Graph", ["nodes", "edges", "is_directed"])


def adjacency_dict(graph):
    """
    Returns the adjacency list representation
    of the graph.
    """
    adj = {node: [] for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        if not graph.is_directed:
            adj[node2].append(node1)
    return adj


def adjacency_matrix(graph):
    """
    Returns the adjacency matrix of the graph.

    Assumes that graph.nodes is equivalent to range(len(graph.nodes)).
    """
    adj = [[0 for node in graph.nodes] for node in graph.nodes]
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1][node2] += 1
        if not graph.is_directed:
            adj[node2][node1] += 1
    return adj


from pyvis.network import Network


Cities = ["Thika", "Nairobi", "Roysambu", "Kahawa west", "Allsops", "Umoja", "Limuru", "Naivasha", "Meru", "Garissa", "Nakuru",
          "Eldoret", "Eldama ravine", "Kisumu", "Kakamega", "Busia", "Lodwar"]
City_Edges = [
    ("Thika", "Nairobi"),
    ("Thika", "Roysambu"),
    ("Roysambu", "Kahawa west"),
    ("Allsops", "Umoja"),
    ("Thika", "Limuru"),
    ("Limuru", "Thika"),
    ("Naivasha", "Meru"),
    ("Meru", "Garissa"),
    ("Thika", "Naivasha"),
    ("Naivasha", "Nakuru"),
    ("Naivasha", "Eldoret"),
    ("Nakuru", "Eldama ravine"),
    ("Eldoret", "Kisumu"),
    ("Kisumu", "Kakamega"),
    ("Kakamega", "Busia"),
    ("Nairobi", "Kisumu"),
    ("Nairobi", "Thika"),
    ("Busia", "Lodwar"),
    ("Nairobi", "Nakuru"),
    ("Nairobi", "Lodwar")
   ]



def show(graph, output_filename):
   g = Network(height = "1500px", width ="100%", bgcolor = "#222222", font_color = "white", directed=graph.is_directed)
   g.add_nodes(graph.nodes)
   g.add_edges(graph.edges)
   g.show(output_filename)
   g.barnes_hut()
   return g

nodes = Cities
edges =City_Edges

G = Graph(nodes, edges,is_directed=True)
show(G,"basic.html")


