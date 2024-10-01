import networkx as nx 
import matplotlib.pyplot as plt 
import numpy as np

def calculateGraphMeasurements(G, fileName):
    
    largest_cc = max(nx.connected_components(G), key=len)
    #node degree distribution plot
    hist = nx.degree_histogram(G)
    plt.xlabel("Node degree")
    plt.ylabel("Number of nodes")
    plt.plot(hist)
    plt.savefig(fileName + "/" + fileName + "_degree_dist.png")
    plt.close()

    #local clustering coefficient plot
    clus = nx.clustering(G)
    plt.xlabel("Clustering Coefficient")
    plt.ylabel("N")
    plt.savefig(fileName + "/" + fileName + "_clustering_dist.png")
    plt.close()
    #shortest path lengths plot
	#plt.savefig(fileName + "/" + fileName + "_shortest_dist.png")

    #open file to put in numerical values
    file = open(fileName + "/" + fileName + "_data.txt", "w")
    #global clustering coefficient
    file.write("Global clustering coefficient: %s\n" % nx.average_clustering(G))

    #average shortest path length
    file.write("Average shortest path length: %s\n" % nx.average_shortest_path_length(G))

    #diameter of graph
    file.write("Diameter of the graph: %s\n" % nx.diameter(G))

    file.close()
