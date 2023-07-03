import json
import os

def save_hyperparameters(data_file, alpha, beta, num_ants, evaporation, max_it, elitism, click_size, seed):
    hyperparams = {'data_file': data_file, 'alpha': alpha, 'beta': beta,
                   'num_ants': num_ants, 'evaporation': evaporation, 'max_it': max_it,
                   'elitism': elitism, 'click_size': click_size}

    if not os.path.exists('Stats/'+data_file):
        os.makedirs('Stats/'+data_file)
    with open('Stats/'+data_file+'/stats_'+data_file + "_" + str(seed) + '.json', 'w') as f:
        json.dump(hyperparams, f)

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
