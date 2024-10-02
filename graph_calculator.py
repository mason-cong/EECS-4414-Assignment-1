import networkx as nx 
import matplotlib.pyplot as plt 
import numpy as np

def calculateGraphMeasurements(G, fileName):

    gcc = max(nx.connected_components(G), key=len)
    gcc_graph = G.subgraph(gcc).copy()

    degree_distrbution(gcc_graph, fileName)
    clustering_distrbution(gcc_graph, fileName)
    shortest_path_distribution(gcc_graph, fileName)

    graph_type = fileName[:-1]
    #open file to put in numerical values
    file = open("graph_data/" + graph_type + "/" + fileName + "_data.txt", "w")
    #global clustering coefficient
    file.write("Global clustering coefficient: %s\n" % nx.average_clustering(gcc_graph))

    #average shortest path length
    file.write("Average shortest path length: %s\n" % nx.average_shortest_path_length(gcc_graph))

    #diameter of graph
    file.write("Diameter of the graph: %s\n" % nx.diameter(gcc_graph))

    #nodes and edges of GCC
    file.write("Number of nodes in GCC: %s\n" % nx.number_of_nodes(gcc_graph))
    file.write("Number of edges in GCC: %s\n" % nx.number_of_edges(gcc_graph))

    file.close()

def degree_distrbution(G, fileName):
    graph_type = fileName[:-1]
    #node degree distribution plot
    hist = nx.degree_histogram(G)
    plt.title("Node Degree Distribution Plot")
    plt.xlabel("Node degree")
    plt.ylabel("Frequency")
    plt.plot(hist)
    plt.savefig("graph_data/" + graph_type + "/" + fileName + "_degree_dist.png")
    plt.close()

def clustering_distrbution(G, fileName):
    graph_type = fileName[:-1]
    #clustering plot
    clus = nx.clustering(G)
    plt.title("Local Clustering Distribution Plot")
    plt.xlabel("Clustering Coefficient")
    plt.ylabel("Frequency")
    plt.hist(clus.values(), bins=20)
    plt.savefig("graph_data/" + graph_type + "/" + fileName + "_clustering_dist.png")
    plt.close()

def shortest_path_distribution(G, fileName):
    graph_type = fileName[:-1]
    #shortest path lengths plot
    lengths = dict(nx.shortest_path_length(G))
    all_lengths = [length for target_lengths in lengths.values() for length in target_lengths.values()]
    plt.hist(all_lengths, bins=20, density=True)
    plt.title("Shortest Path Lengths Distribution Plot")
    plt.xlabel("Path Lengths")
    plt.ylabel("Frequency")
    plt.savefig("graph_data/" + graph_type + "/" + fileName + "_shortest_paths_dist.png")
    plt.close()