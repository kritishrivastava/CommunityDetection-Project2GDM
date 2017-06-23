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
        g.add_edge(int(line[0]),int(line[1]))
    return g

def weight(community):
    #Input: a subgraph/community in the graph
    #Output: weight of the community (using the formula mentioned in the paper)
    if nx.number_of_nodes(community) == 0:
        return 0
    else:
        wght = float(2* nx.number_of_edges(community))/float(nx.number_of_nodes(community))
        return wght

def orderNodes(graph):
    #Input: a networkx graph
    #Output: list of nodes sorted in the decreasing order of their page rank
    dictOfNodes = nx.pagerank(graph)
    pr = dictOfNodes.items()
    pr = sorted(pr, reverse=True, key=get_key)
    return pr

def get_key(l):
    return l[1]

def RaRe(graph):
    #Input: a networkx graph
    #Output: a group of clusters (initial guesses to be fed into the second algorithm)
    #Order the vertices using page rank
    orderedNodes = orderNodes(graph)
    C = []
    for i in orderedNodes:
        added = False
        for c in C:
            temp1 = graph.subgraph(c)
            cc = list(c)
            cc.append(i[0])
            temp2 = graph.subgraph(cc)
            if weight(temp2) > weight(temp1):
                added = True
                c.append(i[0])
        if added == False:
            C.append([i[0]])
    return C

def IS2(cluster, graph):
    #Input: cluster to be improved and the networkx graph
    #Output: improved cluster
    C = graph.subgraph(cluster)
    intialWeight = weight(C)
    increased = True
    while increased:
        N = C.copy()
        listOfNodes = cluster
        for vertex in C.nodes():
            #Get adjacent nodes
            adjacentNodes = graph.neighbors(vertex)
            #Adding all adjacent nodes to the cluster
            for neighbor in adjacentNodes:
                listOfNodes.append(neighbor)
        N = graph.subgraph(listOfNodes)
        for vertex in N.nodes():
            #If the vertex was a part of inital cluster
            if vertex in C.nodes():
                #Remove vertex from the cluster
                listOfNodes = list(C.nodes())
                listOfNodes.remove(vertex)
                CDash = graph.subgraph(listOfNodes)
            #If the vertex is one of the recently added neighbours
            else:
                #Add vertex to the cluster
                listOfNodes = list(C.nodes())
                listOfNodes.append(vertex)
                CDash = graph.subgraph(listOfNodes)
            if weight(CDash) > weight(C):
                C = CDash.copy()
        newWeight = weight(C)
        if newWeight == intialWeight:
            increased = False
        else:
            intialWeight = newWeight
    return C


if __name__ == "__main__":
    #Read file and create a graph
    g = readGraph('amazon\\amazon.graph.medium')
    #Generate initial "guesses" for clusters using RaRe algorithm
    initalClusters = RaRe(g)
    #Get final clusters using Improved Iterative Scan Algorithm
    finalClusters = []
    initalClustersWithoutDuplicates = []
    for cluster in initalClusters:
      #  cluster = list(map(int,cluster))
        cluster = sorted(cluster)
        if cluster not in initalClustersWithoutDuplicates:
            initalClustersWithoutDuplicates.append(cluster)
            updatedCluster = IS2(cluster,g)
            finalClusters.append(updatedCluster.nodes())

    #Removing duplicate clusters and printing output to a file
    f = open('amazon.graph.medium.clusters.txt', 'w')
    finalClustersWithoutDuplicates = []
    for cluster in finalClusters:
        cluster = sorted(cluster)
        if cluster not in finalClustersWithoutDuplicates:
            finalClustersWithoutDuplicates.append(cluster)
            for node in cluster:
                f.write("%s " % node)
            f.write("\n")
