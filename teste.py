import numpy as np
import random

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = np.zeros((num_vertices, num_vertices))

class ACO:
    def __init__(self, grafo, num_formigas, num_iteracoes, evap_rate, min_ferom, max_ferom):
        self.grafo = grafo
        self.num_formigas = num_formigas
        self.num_iteracoes = num_iteracoes
        self.evap_rate = evap_rate
        self.min_ferom = min_ferom
        self.max_ferom = max_ferom
        self.feromonio = np.ones((grafo.num_vertices, grafo.num_vertices)) * max_ferom
        self.melhor_clique = []

    def busca_local(self, clique):
        vertices = list(range(self.grafo.num_vertices))
        random.shuffle(vertices)
        for v in vertices:
            if v not in clique:
                valido = True
                for c in clique:
                    if self.grafo.adj_matrix[v][c] == 0:
                        valido = False
                        break
                if valido:
                    clique.append(v)
                    break
        return clique

    def resolve(self):
        for _ in range(self.num_iteracoes):
            formiga_cliques = []
            for _ in range(self.num_formigas):
                clique_inicial = [random.randint(0, self.grafo.num_vertices - 1)]
                for _ in range(self.grafo.num_vertices - 1):
                    clique = self.busca_local(clique_inicial.copy())
                    if len(clique) > len(self.melhor_clique):
                        self.melhor_clique = clique
                    formiga_cliques.append(clique)
            for clique in formiga_cliques:
                for i in range(len(clique) - 1):
                    self.feromonio[clique[i]][clique[i + 1]] += 1
                    self.feromonio[clique[i + 1]][clique[i]] += 1
            self.feromonio = (1 - self.evap_rate) * self.feromonio
            np.clip(self.feromonio, self.min_ferom, self.max_ferom, out=self.feromonio)

def le_arquivo(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().split()
            if line[0] == "c":
                continue
            elif line[0] == "p":
                num_vertices = int(line[2])
                grafo = Grafo(num_vertices)
            elif line[0] == "e":
                grafo.adj_matrix[int(line[1])-1][int(line[2])-1] = 1
                grafo.adj_matrix[int(line[2])-1][int(line[1])-1] = 1
        return grafo

def main():
    grafo = le_arquivo("Dataset/g_700.txt")
    aco = ACO(grafo, num_formigas=10, num_iteracoes=1000, evap_rate=0.1, min_ferom=1.0, max_ferom=100.0)
    aco.resolve()
    print("Maior clique encontrado:", aco.melhor_clique)

if __name__ == "__main__":
    main()