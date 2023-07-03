class Graph:
    def __init__(self, num_vertices, edges, pheromones, total_edges=None, max_pheromone=100, min_pheromone=1):
        self.num_vertices = num_vertices
        self.edges = edges if edges else [[] for _ in range(num_vertices)]  # Adjacency lists
        self.pheromones = pheromones if pheromones else [[1 for _ in range(num_vertices)] for _ in range(num_vertices)]  # Initial pheromones
        self.total_edges = total_edges if total_edges else 0  # Initialize total_edges
        self.max_pheromone = max_pheromone
        self.min_pheromone = min_pheromone
    def add_edge(self, u, v):
        #Add an edge between vertices u and v
        self.edges[u].append(v)
        self.edges[v].append(u)  # Assuming the graph is undirected
        self.total_edges += 1  # Update total_edges

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
        return self.get_degree(v)

    def set_pheromone(self, u, v, value):
        #Set the pheromone level of the edge between u and v respecting max and min value
        value = max(self.min_pheromone, min(self.max_pheromone, value))
        self.pheromones[u][v] = value
        self.pheromones[v][u] = value

    def evaporate_pheromones(self, evaporation_rate, solution_edges):
        #Evaporate some of the pheromones on all edges except the ones in the solution
        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                # Check if the edge (u, v) or (v, u) is not in the solution
                if (u, v) not in solution_edges and (v, u) not in solution_edges:
                    self.pheromones[u][v] *= (1 - evaporation_rate)
                    self.pheromones[u][v] = max(self.min_pheromone, self.pheromones[u][v])  # Don't let it go below the min
                    self.pheromones[v][u] = self.pheromones[u][v]  # Assuming the graph is undirected
    
    @classmethod
    def from_dict(cls, graph_dict, max_pheromone=100, min_pheromone=1):
        num_vertices = len(graph_dict)
        edges = [[] for _ in range(num_vertices)]
        pheromones = [[1 for _ in range(num_vertices)] for _ in range(num_vertices)]  # Initial pheromones
        total_edges = 0

        for vertex, neighbors in graph_dict.items():
            # subtracting 1 because vertices in the dict are 1-indexed, but our list is 0-indexed
            for neighbor in neighbors:
                edges[vertex-1].append(neighbor-1)
                edges[neighbor-1].append(vertex-1)  # Assuming the graph is undirected
                total_edges += 1

        total_edges //= 2  # since each edge was counted twice

        return cls(num_vertices, edges, pheromones, total_edges, max_pheromone, min_pheromone)