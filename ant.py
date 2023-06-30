class Ant:
    def __init__(self, start_node):
        # The nodes visited by this ant will be stored in self.clique
        self.clique = [start_node]
        self.current_node = start_node

    def add_node(self, node):
        #Add a node to the ant's clique
        self.clique.append(node)
        self.current_node = node

    def get_current_node(self):
        #Get the current node of the ant
        return self.current_node

    def get_clique(self):
        #Get the nodes visited by the ant
        return self.clique

    def get_clique_size(self):
        #Get the size of the ant's clique
        return len(self.clique)

    def clear_clique(self):
        #Clear the ant's clique
        start_node = self.clique[0]
        self.clique = [start_node]
        self.current_node = start_node