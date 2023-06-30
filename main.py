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
    best_clique_size_local = 0
    best_click_of_all = []
    best_click_local = []
    best_ant_local = Ant(graph, alpha, beta)
    best_ant_off_all = Ant(graph, alpha, beta)
    taxa_evaporacao = 0.3

    ants = [Ant(graph, alpha, beta) for _ in range(num_ants)]
    for i in range(10):
        
        for ant in ants:
            for _ in range(graph.num_vertices):
                ant.select_next_vertex()

                if ant.is_complete_subgraph():
                    print("Found a solution: ", str(len(ant.visited_vertices)))
                    if len(ant.visited_vertices) > len(best_click_of_all):
                        best_clique_size = len(ant.visited_vertices)
                        best_click_of_all = ant.visited_vertices
                        best_click_local = ant.visited_vertices
                        #save pheromone delta
                        ant.update_pheromone_delta()
                        best_ant_off_all = ant
                        best_ant_local = ant
                    elif len(ant.visited_vertices) > best_clique_size_local:
                        best_clique_size_local = len(ant.visited_vertices)
                        best_click_local = ant.visited_vertices
                        #save pheromone delta
                        ant.update_pheromone_delta()
                        best_ant_local = ant
                    
            
            #increase delta pheromone
            ant.update_pheromone_delta()

        #update pheromone without best way

        solution_edges = []
        for i in range(len(best_click_local) -1):
            u = best_click_local[i]
            v = best_click_local[i+1]
            edge = (u, v)
            solution_edges.append(edge)
            # Update pheromone levels with delta
            graph.set_pheromone(u, v, graph.get_pheromone(u, v) + best_ant_local.pheromone_delta[u][v])

        graph.evaporate_pheromones(taxa_evaporacao, solution_edges)


    
    print("Best clique size: ", len(best_click_of_all))
    print("Best clique: ", best_click_of_all)

    