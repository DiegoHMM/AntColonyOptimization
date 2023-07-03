from aco import ant_colony_optimization
import random
from utils import save_hyperparameters, create_stats_folder


if __name__ == "__main__":
    # 10 seeds
    seeds = [57, 12, 89, 42, 76, 28, 63, 95, 51, 10]
    alpha = 1
    beta = 1
    num_ants = 50  # graph.num_vertices
    evaporation = 0.5
    max_it = 100
    max_pheromone = 100
    min_pheromone = 1
    elitism = True

    # Data files and corresponding click sizes
    experiments = [('g_125', 3), ('g_500', 13), ('g_700', 44)]

    for seed in seeds:
        random.seed(seed)

        for data_file, click_size in experiments:
            print(f"Seed: {seed}")
            print(f"Grafo: {data_file}")

            folder = f'Stats/{data_file}/{seed}'
            print(folder)
            create_stats_folder(folder)

            # Run ACO
            stats_df = ant_colony_optimization(data_file, click_size, alpha, beta, num_ants, evaporation, max_it, elitism, seed, max_pheromone, min_pheromone)

            # Save stats
            save_hyperparameters(f'{folder}', data_file, alpha, beta, num_ants, evaporation, max_it, elitism, click_size, seed, max_pheromone, min_pheromone)
            stats_df.to_csv(f'{folder}/stats.csv', index=False)

            print('')