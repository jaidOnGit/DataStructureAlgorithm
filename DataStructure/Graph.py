class Graph:
    """
    Abstract Data Type: Graph

    A graph is a non-linear data structure consisting of vertices (nodes) and edges
    that connect pairs of vertices. This class provides basic operations like adding vertices,
    adding edges, and performing BFS and DFS traversals.

    Applications:
      - Representing networks such as transportation and communication.
      - Pathfinding problems in maps and navigation systems.
    
    Limitations:
      - Memory-intensive for dense graphs (using adjacency matrix representation).
      - Traversals may become computationally expensive for large graphs.
    """
    def __init__(self):
        """
        Initialize an empty graph.
        """
        self.graph = {}  # Adjacency list representation

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.

        :param vertex: The vertex to add.
        :return: None
        """
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """
        Add an edge between two vertices.

        :param vertex1: The first vertex.
        :param vertex2: The second vertex.
        :return: None
        """
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)  # Remove this line for a directed graph

    def bfs(self, start_vertex):
        """
        Perform Breadth-First Search (BFS) traversal.

        :param start_vertex: The starting vertex for BFS.
        :return: List of vertices in BFS order.
        """
        visited = set()
        queue = [start_vertex]
        bfs_order = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                bfs_order.append(vertex)
                queue.extend([v for v in self.graph[vertex] if v not in visited])

        return bfs_order

    def dfs(self, start_vertex):
        """
        Perform Depth-First Search (DFS) traversal.

        :param start_vertex: The starting vertex for DFS.
        :return: List of vertices in DFS order.
        """
        visited = set()
        stack = [start_vertex]
        dfs_order = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                dfs_order.append(vertex)
                stack.extend([v for v in self.graph[vertex] if v not in visited])

        return dfs_order

def test_graph():
    # Instantiate the Graph class
    graph = Graph()

    # Add vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    # Add edges
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")

    # Example 1: BFS Traversal
    bfs_result = graph.bfs("A")
    print("\nBFS Traversal:", bfs_result)

    # Example 2: DFS Traversal
    dfs_result = graph.dfs("A")
    print("\nDFS Traversal:", dfs_result)

    # Example 3: Graph Structure
    print("\nGraph Structure:")
    print(graph.graph)
