from graph import Graph
from utils import *
from ant import Ant


if __name__ == "__main__":

    data_file = 'g_700.txt'

    if data_file == 'g_125.txt':
        graph_dict = read_graph('Dataset/'+data_file)
        graph = Graph.from_dict(graph_dict)
        click_size = 4
    elif data_file == 'g_500.txt':
        graph_dict = read_graph('Dataset/'+data_file)
        graph = Graph.from_dict(graph_dict)
        click_size = 13
    elif data_file == 'g_700.txt':
        graph_dict = read_graph('Dataset/'+data_file)
        graph = Graph.from_dict(graph_dict)
        click_size = 44


    
    print("Total vértices: ", str(graph.num_vertices))
    print("Total arestas: ", str(graph.total_edges))

    MAX_ITERACTIONS = graph.num_vertices
    alpha = 1
    beta = 1
    num_ants = 50#graph.num_vertices

    best_click_of_all = []
    best_click_local = []
    best_ant_local = Ant(graph, alpha, beta)
    best_ant_off_all = Ant(graph, alpha, beta)
    taxa_evaporacao = 0.001


    for i in range(500):
        ants = [Ant(graph, alpha, beta) for _ in range(num_ants)]
        print("Interation: ", str(i))
        best_clique_size_local = 0

        for ant in ants:
            for j in range(click_size): #Cada formiga vai andar click_size vezes
                ant.select_next_vertex()

                if ant.is_complete_subgraph():
                    if len(ant.visited_vertices) > len(best_click_of_all):
                        print("Found a global solution: ", str(len(ant.visited_vertices)))
                        best_clique_size = len(ant.visited_vertices)
                        best_click_of_all = ant.visited_vertices.copy()
                        best_click_local = ant.visited_vertices.copy()
                        #save pheromone delta
                        ant.update_pheromone_delta()
                        best_ant_off_all = ant
                        best_ant_local = ant
                    elif len(ant.visited_vertices) > best_clique_size_local:
                        #print("Found a local solution: ", str(len(ant.visited_vertices)))
                        best_clique_size_local = len(ant.visited_vertices)
                        best_click_local = ant.visited_vertices.copy()
                        #save pheromone delta
                        ant.update_pheromone_delta()
                        best_ant_local = ant
                    
            
            #increase delta pheromone
            ant.update_pheromone_delta()

        #update pheromone without best way
        #Local best
        '''
        solution_edges = []
        for i in range(len(best_ant_local.visited_vertices) -1):
            u = best_ant_local.visited_vertices[i]
            v = best_ant_local.visited_vertices[i+1]
            edge = (u, v)
            solution_edges.append(edge)
            # Update pheromone levels with delta
            graph.set_pheromone(u, v, graph.get_pheromone(u, v) + best_ant_local.pheromone_delta[u][v])

        '''

        #Global best
        solution_edges = []
        for i in range(len(best_ant_off_all.visited_vertices) -1):
            u = best_ant_off_all.visited_vertices[i]
            v = best_ant_off_all.visited_vertices[i+1]
            edge = (u, v)
            solution_edges.append(edge)
            # Update pheromone levels with delta
            graph.set_pheromone(u, v, graph.get_pheromone(u, v) + best_ant_off_all.pheromone_delta[u][v])

        graph.evaporate_pheromones(taxa_evaporacao, solution_edges)
    print("Best clique size: ", len(best_click_of_all))
    print("Best clique: ", best_click_of_all)

    