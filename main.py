from graph import Graph
from utils import *


if __name__ == "__main__":
    graph_dict = read_graph('graph_1.txt')
    graph = Graph.build_graph(graph_dict)
    print(graph.num_vertices)
    print(len(graph.edges))
    