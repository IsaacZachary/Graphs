
from typing import TypeVar, Generic, List, Optional
from pyvis.network import Network


V = TypeVar('V') # type of the vertices in the graph


class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices) # Number of vertices

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges)) # Number of edges

    # Add a vertex to the graph and return its index
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([]) # add empty list for containing edges
        return self.vertex_count - 1 # return index of added vertex

    # This is an undirected graph,
    # so we always add edges in both directions
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    # Add an edge using vertex indices (convenience method)
    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.add_edge(edge)

    # Add an edge by looking up vertex indices (convenience method)
    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    # Find the vertex at a specific index
    def vertex_at(self, index: int) -> V:
        return self._vertices[index]

    # Find the index of a vertex in the graph
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)

    # Find the vertices that a vertex at some index is connected to
    def neighbors_for_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    # Lookup a vertice's index and find its neighbors (convenience method)
    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))

    # Return all of the edges associated with a vertex at some index
    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    # Lookup the index of a vertex and return its edges (convenience method)
    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    # Make it easy to pretty-print a Graph
    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc


if __name__ == "__main__":
    # test basic Graph construction
    city_graph: Graph[str] = Graph(["Nairobi", "Mombasa", "Nakuru", "Naivasha", "Nakuru", "Eldoret", "Embu", "Kisumu", "Homabay", "Kiambu", "Samburu", "Kisii", "Kajiado", "Isiolo", "Garrissa"])
    city_graph.add_edge_by_vertices("Nairobi", "Eldoret")
    city_graph.add_edge_by_vertices("Nairobi", "Mombasa")
    city_graph.add_edge_by_vertices("Mombasa", "Naivasha")
    city_graph.add_edge_by_vertices("Mombasa", "Los Angeles")
    city_graph.add_edge_by_vertices("Mombasa", "Naivasha")
    city_graph.add_edge_by_vertices("Mombasa", "Nakuru")
    city_graph.add_edge_by_vertices("Naivasha", "Nakuru")
    city_graph.add_edge_by_vertices("Naivasha", "Eldoret")
    city_graph.add_edge_by_vertices("Nakuru", "Homabay")
    city_graph.add_edge_by_vertices("Nakuru", "Kiambu")
    city_graph.add_edge_by_vertices("Kiambu", "Eldoret")
    city_graph.add_edge_by_vertices("Kiambu", "Homabay")
    city_graph.add_edge_by_vertices("Kiambu", "Kisii")
    city_graph.add_edge_by_vertices("Kisii", "Homabay")
    city_graph.add_edge_by_vertices("Kisii", "Kiambu")
    city_graph.add_edge_by_vertices("Homabay", "Naivasha")
    city_graph.add_edge_by_vertices("Homabay", "Garrissa")
    city_graph.add_edge_by_vertices("Homabay", "Kisii")
    city_graph.add_edge_by_vertices("Kisii", "Garrissa")
    city_graph.add_edge_by_vertices("Kiambu", "Kajiado")
    city_graph.add_edge_by_vertices("Kajiado", "Embu")
    city_graph.add_edge_by_vertices("Kajiado", "Garrissa")
    city_graph.add_edge_by_vertices("Kajiado", "Kisumu")
    city_graph.add_edge_by_vertices("Embu", "Kisumu")
    city_graph.add_edge_by_vertices("Kisumu", "Isiolo")
    city_graph.add_edge_by_vertices("Isiolo", "Garrissa")
    print(city_graph)

    # Reuse BFS from Chapter 2 on city_graph
    import sys
    sys.path.insert(0, '..') # so we can access the Chapter2 package in the parent directory
    from Chapter2.generic_search import bfs, Node, node_to_path

    bfs_result: Optional[Node[V]] = bfs("Embu", lambda x: x == "Kisii", city_graph.neighbors_for_vertex)
    if bfs_result is None:
        print("No solution found using breadth-first search!")
    else:
        path: List[V] = node_to_path(bfs_result)
        print("Path from Embu to Kisii:")
        print(path)
()