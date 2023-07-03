import json
import os

def save_hyperparameters(path, data_file, alpha, beta, num_ants, evaporation, max_it, elitism, click_size, seed, max_pheromone, min_pheromone):
    hyperparams = {'data_file': data_file, 'alpha': alpha, 'beta': beta,
                   'num_ants': num_ants, 'evaporation': evaporation, 'max_it': max_it,
                   'elitism': elitism, 'click_size': click_size, 'seed': seed, 'max_pheromone': max_pheromone, 'min_pheromone': min_pheromone}

    create_stats_folder(path)
    with open(path+'/'+data_file+'.json', 'w') as f:
        json.dump(hyperparams, f)


def create_stats_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def read_graph(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            tokens = line.split()

            # Ignorar linhas de comentários
            if tokens[0] == 'c':
                continue

            # Inicializar o grafo com o número correto de vértices
            elif tokens[0] == 'p' and tokens[1] == 'edge':
                for i in range(1, int(tokens[2]) + 1):
                    graph[i] = []

            # Adicionar as arestas ao grafo
            elif tokens[0] == 'e':
                graph[int(tokens[1])].append(int(tokens[2]))
                graph[int(tokens[2])].append(int(tokens[1]))
    return graph
