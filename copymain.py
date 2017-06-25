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
        return float(2*nx.number_of_edges(community)/nx.number_of_nodes(community))

def orderNodes(graph):
    #Input: a networkx graph
    #Output: list of nodes sorted in the decreasing order of their page rank
    dictOfNodes = nx.pagerank(graph)
    orderedNodes = dictOfNodes.items()
    orderedNodes = sorted(orderedNodes, reverse=True, key=get_key)
    return orderedNodes

def get_key(node):
    #Input: list containing node name and its page rank
    #Output: return rank of the node
    return node[1]

def RaRe(graph):
    #Input: a networkx graph
    #Output: a group of clusters (initial guesses to be fed into the second algorithm)
    #Order the vertices using page rank
    orderedNodes = orderNodes(graph)
    C = []
    for i in orderedNodes:
        added = False
        for c in C:
            #Add the node and see if the weight of the cluster increases
            temp1 = graph.subgraph(c)
            cc = list(c)
            cc.append(i[0])
            temp2 = graph.subgraph(cc)
            #If wieght increases, add the node to the cluster
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
    #    N = C.copy()
        listOfNodes = cluster
        for vertex in C.nodes():
            #Get adjacent nodes
            adjacentNodes = graph.neighbors(vertex)
            #Adding all adjacent nodes to the cluster
            #listOfNodes = listOfNodes + adjacentNodes
            listOfNodes = list(set(listOfNodes).union(set(adjacentNodes)))
    #    N = graph.subgraph(listOfNodes)
        for vertex in listOfNodes:
            listOfNodes = list(C.nodes())
            #If the vertex was a part of inital cluster
            if vertex in C.nodes():
                #Remove vertex from the cluster
                listOfNodes.remove(vertex)
            #If the vertex is one of the recently added neighbours
            else:
                #Add vertex to the cluster
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
    # Get final clusters using Improved Iterative Scan Algorithm
    finalClusters = []
    initalClustersWithoutDuplicates = []
    for cluster in initalClusters:
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
