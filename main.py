from graph import Graph
from utils import *
from ant import Ant


if __name__ == "__main__":
    graph_dict = read_graph('graph_1.txt')
    graph = Graph.build_graph(graph_dict)
    print(graph.num_vertices)
    print(len(graph.edges))

    MAX_ITERACTIONS = 50
    alpha = 1
    beta = 1
    num_ants = len(graph.edges)
    best_clique_size_of_all = 0
    best_clique_size_local = 0
    best_ant_off_all = Ant(graph, 1, 1)
    best_ant_local = Ant(graph, 1, 1)
    taxa_evaporacao = 0.3

    for i in range(5):
        ants = [Ant(graph, alpha, beta) for _ in range(num_ants)]

        for ant in ants:
            for _ in range(num_ants):
                ant.select_next_vertex()

            if ant.is_complete_subgraph():
                print("Found a solution: ", str(len(ant.visited_vertices)))
                if len(ant.visited_vertices) > best_clique_size_of_all:
                    solution.append(ant.visited_vertices)
                    best_clique_size = len(ant.visited_vertices)
                    best_ant_off_all = ant
                    best_ant_local = ant
                elif len(ant.visited_vertices) > best_clique_size_local:
                    best_clique_size_local = len(ant.visited_vertices)
                    best_ant_local = ant
                    
            
            #increase delta pheromone
            ant.update_pheromone_delta()

        #update pheromone without best way

        solution_edges = []
        for i in range(len(best_ant_local.visited_vertices) -1):
            edge = (best_ant_local.visited_vertices[i], best_ant_local.visited_vertices[i+1])
            solution_edges.append(edge)
            graph.pheromone[edge] += best_ant_local.pheromone_delta[edge]
        
        graph.evaporate_pheromones(taxa_evaporacao, solution_edges)


    
    print("Best clique size: ", best_clique_size_of_all)
    print("Best clique: ", best_ant_off_all.visited_vertices)

    