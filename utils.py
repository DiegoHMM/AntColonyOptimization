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

def is_complete(graph):
    vertices = list(graph.keys())
    n = len(vertices)
    for vertex in vertices:
        if len(graph[vertex]) != n - 1:
            return False
    return True

def count_vertices(graph):
    return len(graph.keys())
