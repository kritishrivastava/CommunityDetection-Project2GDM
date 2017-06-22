import networkx as nx
import numpy as np
import os

def readGraph(graphName):
    #Read file and create a networkx graph
    g = nx.Graph()
    filePath = os.getcwd() + '\datasets\\'+graphName
    f = open(filePath, 'r')
    next(f) #Skipping the first row containing number of nodes and edges
    for line in f:
        line = line.split()
        g.add_edge(line[0],line[1])
    return g

if __name__ == "__main__":
    g = readGraph('amazon\\amazon.graph.medium')
