###################### NOT A WORKING CODE YET ####################################


import networkx as nx
import numpy as np
import os

def readGraph(graphName):
    #Input: name of the file from which graph has to be read
    #Output: creates and returns a networkx graph
    #Read file and create a networkx graph
    g = nx.Graph()
    filePath = os.getcwd() + '\datasets\\'+graphName
    f = open(filePath, 'r')
    #Skipping the first row containing number of nodes and edges
    next(f)
    for line in f:
        line = line.split()
        g.add_edge(line[0],line[1])
    return g

def weight(community):
    #Input: a subgraph/community in the graph
    #Output: weight of the community (using the formula mentioned in the paper)
    wght = (2* nx.number_of_edges(community))/nx.number_of_nodes(community)
    return wght

def orderNodes(graph):
    #Input: a networkx graph
    #Output: list of nodes sorted in the decreasing order of their page rank
    dictOfNodes = nx.pagerank(graph)


def RaRe(graph):
    #Input: a networkx graph
    #Output: a group of clusters (initial guesses to be fed into the second algorithm)
    #Order the vertices using page rank
    orderedNodes = orderedNodes(graph)

if __name__ == "__main__":
    #Read file and create a graph
    g = readGraph('amazon\\amazon.graph.medium')
    #Generate initial "guesses" for clusters using RaRe algorithm
    initalClusters = RaRe(g)
