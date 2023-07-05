import random

class Ant:
    def __init__(self, graph, alpha, beta):
        self.graph = graph
        self.alpha = alpha  # Pheromone importance
        self.beta = beta  # Desirability importance
        self.current_node = random.randrange(graph.num_vertices)  # Start at a random vertex
        self.visited_vertices = [self.current_node]  # List of visited vertices
        self.pheromone_delta = [[0 for _ in range(graph.num_vertices)] for _ in range(graph.num_vertices)]  # Changes of pheromones

    def calculate_probability(self, v):
        # Calculate the probability of moving to vertex v
        pheromone = self.graph.get_pheromone(self.current_node, v) ** self.alpha
        #desirability = self.graph.get_desirability(self.current_node, v) ** self.beta
        return pheromone# * desirability

    def select_next_vertex(self):
        # Select the next vertex to visit
        candidate_vertices = [v for v in range(self.graph.num_vertices) if v not in self.visited_vertices and all(
            u in self.graph.get_neighbors(v) for u in self.visited_vertices)]
        if not candidate_vertices:
            return  # If no candidates, we don't add a new vertex and return from the function
        probabilities = [self.calculate_probability(v) for v in candidate_vertices]
        total = sum(probabilities)
        probabilities = [p / total for p in probabilities]  # Normalize to make it a probability distribution
        next_vertex = random.choices(candidate_vertices, probabilities)[0]  # Select a vertex based on the probabilities
        self.visited_vertices.append(next_vertex)
        self.current_node = next_vertex

    def is_complete_subgraph(self):
        # Check if the visited vertices form a complete subgraph (clique)
        for u in self.visited_vertices:
            for v in self.visited_vertices:
                if u != v and v not in self.graph.get_neighbors(u):
                    return False
        return True

    def update_pheromone_delta(self):
        # Update the changes of pheromones
        #if self.is_complete_subgraph():
        for i in range(len(self.visited_vertices) - 1):
            u = self.visited_vertices[i]
            v = self.visited_vertices[i + 1]
            self.pheromone_delta[u][v] = 1 / len(self.visited_vertices)  # Increase the pheromone level edge (u,v)
            self.pheromone_delta[v][u] = self.pheromone_delta[u][v] # edge (v,u)