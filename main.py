#Implementation for paper 1:Efficient Identification of Overlapping Communities?

#Project Team Members:
#1. Manjusha Trilochan Awasthi (mawasth)
#2. Kriti Shrivastava (kshriva)
#3. Rachit Thirani (rthiran)

import networkx as nx
import numpy as np
import os
import sys

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

def LA(graph):
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
        listOfNodes = cluster
        for vertex in C.nodes():
            #Get adjacent nodes
            adjacentNodes = graph.neighbors(vertex)
            #Adding all adjacent nodes to the cluster
            listOfNodes = list(set(listOfNodes).union(set(adjacentNodes)))
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
    #Read input file name and create file path accordingly
    graphName = sys.argv[1]
    if "amazon" in graphName:
        filename = "amazon\\" + graphName
    elif "dblp" in graphName:
        filename = "dblp\\" + graphName
    else:
        filename = "youtube\\" + graphName
    #Read file and create a graph
    g = readGraph(filename)
    #Generate initial "guesses" for clusters using Link Aggregate algorithm
    initalClusters = LA(g)
    #Get final clusters using Improved Iterative Scan Algorithm
    finalClusters = []
    initalClustersWithoutDuplicates = []
    for cluster in initalClusters:
        cluster = sorted(cluster)
        if cluster not in initalClustersWithoutDuplicates:
            initalClustersWithoutDuplicates.append(cluster)
            updatedCluster = IS2(cluster,g)
            finalClusters.append(updatedCluster.nodes())
    #Removing duplicate clusters and printing output to a file
    outputfile = graphName + ".clusters.txt"
    f = open(outputfile, 'w')
    finalClustersWithoutDuplicates = []
    for cluster in finalClusters:
        cluster = sorted(cluster)
        if cluster not in finalClustersWithoutDuplicates:
            finalClustersWithoutDuplicates.append(cluster)
            f.write(*cluster,sep=" ")
            f.write("\n")
