from aco import ant_colony_optimization
import random


if __name__ == "__main__":
    alpha = 1
    beta = 1
    num_ants = 50  # graph.num_vertices
    evaporation = 0.001
    max_it = 5
    elitism = True
    #10 seeds
    seeds = [57, 12, 89, 42, 76, 28, 63, 95, 51, 10]


    for seed in seeds:
        random.seed(seed)
        data_file = 'g_125'
        click_size = 3
        click = ant_colony_optimization(data_file, click_size, alpha, beta, num_ants, evaporation, max_it, elitism, seed)

        #data_file = 'g_500'
        #click_size = 13
        #click = ant_colony_optimization(data_file, click_size, alpha, beta, num_ants, evaporation, max_it, elitism, seed)

        #data_file = 'g_700'
        #click_size = 44
        #click = ant_colony_optimization(data_file, click_size, alpha, beta, num_ants, evaporation, max_it, elitism, seed)
