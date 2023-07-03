import pandas as pd
#Local imports
from graph import Graph
from utils import *
from ant import Ant

def ant_colony_optimization(data_file, click_size, alpha, beta, num_ants, evaporation, max_it, elitism, seed):
    #Read graph
    graph_dict = read_graph('Dataset/'+data_file+'.txt')
    graph = Graph.from_dict(graph_dict)

    print("Total vértices: ", str(graph.num_vertices))
    print("Total arestas: ", str(graph.total_edges))

    # Initialize DataFrame to store statistics
    stats_df = pd.DataFrame(columns=['Iteration', 'Best_Clique_Size', 'Best_Clique'])

    best_click_of_all = []
    best_click_local = []
    best_ant_local = Ant(graph, alpha, beta)
    best_ant_off_all = Ant(graph, alpha, beta)
    i = 0
    while i < max_it and len(best_click_of_all) < click_size:
        ants = [Ant(graph, alpha, beta) for _ in range(num_ants)]
        print("Interation: ", str(i))
        best_clique_size_local = 0

        for ant in ants:
            for j in range(click_size):  # Cada formiga vai andar click_size vezes
                ant.select_next_vertex()

                if ant.is_complete_subgraph():
                    if len(ant.visited_vertices) > len(best_click_of_all):
                        print("Found a global solution: ", str(len(ant.visited_vertices)))
                        best_clique_size = len(ant.visited_vertices)
                        best_click_of_all = ant.visited_vertices.copy()
                        best_click_local = ant.visited_vertices.copy()
                        # save pheromone delta
                        ant.update_pheromone_delta()
                        best_ant_off_all = ant
                        best_ant_local = ant
                    elif len(ant.visited_vertices) > best_clique_size_local:
                        # print("Found a local solution: ", str(len(ant.visited_vertices)))
                        best_clique_size_local = len(ant.visited_vertices)
                        best_click_local = ant.visited_vertices.copy()
                        # save pheromone delta
                        ant.update_pheromone_delta()
                        best_ant_local = ant
            # increase delta pheromone
            ant.update_pheromone_delta()

        if elitism:
            solution_edges = []
            for k in range(len(best_ant_off_all.visited_vertices) - 1):
                u = best_ant_off_all.visited_vertices[k]
                v = best_ant_off_all.visited_vertices[k + 1]
                edge = (u, v)
                solution_edges.append(edge)
                # Update pheromone levels with delta
                graph.set_pheromone(u, v, graph.get_pheromone(u, v) + best_ant_off_all.pheromone_delta[u][v])
        else:
            solution_edges = []
            for k in range(len(best_ant_local.visited_vertices) - 1):
                u = best_ant_local.visited_vertices[k]
                v = best_ant_local.visited_vertices[k + 1]
                edge = (u, v)
                solution_edges.append(edge)
                # Update pheromone levels with delta
                graph.set_pheromone(u, v, graph.get_pheromone(u, v) + best_ant_local.pheromone_delta[u][v])

        graph.evaporate_pheromones(evaporation, solution_edges)
        #Save stats
        temp_df = pd.DataFrame({'Iteration': [i],
                                'Best_Clique_Size': [len(best_click_of_all)],
                                'Best_Clique': [best_click_of_all]})
        stats_df = pd.concat([stats_df, temp_df], ignore_index=True)
        i += 1
    print("Best clique size: ", len(best_click_of_all))
    print("Best clique: ", best_click_of_all)
    #Save stats as csv
    save_hyperparameters(data_file, alpha, beta, num_ants, evaporation, max_it, elitism, click_size, seed)
    stats_df.to_csv('Stats/' + data_file + '/stats_' + data_file + '_' + str(seed) + '.csv', index=False)

    return best_click_of_all