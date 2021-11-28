
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


Cities = ["Thika", "Ruiru", "Meru", "Kikuyu", "Eldoret", "Nairobi", "Garisa", "Kakamega", "Molo", "Kisumu", "Nakuru", "Naivasha", "Mombasa", "Kitale", "Malindi"]

City_Edges = [
    ("Thika", "Nairobi"),
    ("Thika", "Ruiru"),
    ("Ruiru", "Kikuyu"),
    ("Ruiru", "Meru"),
    ("Meru", "Kikuyu"),
    ("Meru", "Eldoret"),
    ("Kikuyu", "Eldoret"),
    ("Kikuyu", "Nairobi"),
    ("Eldoret", "Nakuru"),
    ("Eldoret", "Naivasha"),
    ("Nakuru", "Nairobi"),
    ("Nakuru", "Molo"),
    ("Nakuru", "Naivasha"),
    ("Naivasha", "Molo"),
    ("Naivasha", "Kisumu"),
    ("Molo", "Nairobi"),
    ("Molo", "Malindi"),
    ("Molo", "Kisumu"),
    ("Kisumu", "Malindi"),
    ("Nairobi", "Mombasa"),
    ("Mombasa", "Garisa"),
    ("Mombasa", "Malindi"),
    ("Mombasa", "Kakamega"),
    ("Garisa", "Kakamega"),
    ("Kakamega", "Kitale"),
    ("Kitale", "Malindi"), ]



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
