class Graph:
    def __init__(self, num_vertices, edges=None, pheromones=None):
        self.num_vertices = num_vertices
        self.edges = edges if edges else [[] for _ in range(num_vertices)]  # Adjacency lists
        self.pheromones = pheromones if pheromones else [[1 for _ in range(num_vertices)] for _ in range(num_vertices)]  # Initial pheromones

    def add_edge(self, u, v):
        #Add an edge between vertices u and v
        self.edges[u].append(v)
        self.edges[v].append(u)  # Assuming the graph is undirected

    def get_neighbors(self, v):
        #Get the neighbors of a vertex v
        return self.edges[v]

    def get_pheromone(self, u, v):
        #Get the pheromone level of the edge between u and v
        return self.pheromones[u][v]


    def get_degree(self, v):
        #Get the degree of a vertex v
        return len(self.edges[v])

    def get_desirability(self, u, v):
        #Get the desirability of moving from vertex u to vertex v
        return self.get_pheromone(u, v) * self.get_degree(v)

    def set_pheromone(self, u, v, value):
        #Set the pheromone level of the edge between u and v
        self.pheromones[u][v] = value
        self.pheromones[v][u] = value  # Assuming the graph is undirected

    def evaporate_pheromones(self, evaporation_rate):
        #Evaporate some of the pheromones on all edges
        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                self.pheromones[u][v] *= (1 - evaporation_rate)
                self.pheromones[v][u] = self.pheromones[u][v]  # Assuming the graph is undirected

    @classmethod
    def build_graph(cls, graph_dict):
        num_vertices = len(graph_dict)
        edges = [[] for _ in range(num_vertices)]
        pheromones = [[1 for _ in range(num_vertices)] for _ in range(num_vertices)]  # Initialize pheromones
        for vertex, neighbors in graph_dict.items():
            edges[vertex-1] = [n-1 for n in neighbors]  # Adjusting for 0-based indexing
        return cls(num_vertices, edges, pheromones)