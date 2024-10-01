import networkx as nx 
import matplotlib.pyplot as plot 
import numpy as np

def calculateGraphMeasurements(G, fileName):
    
    largest_cc = max(nx.connected_components(G), key=len)
    #node degree distribution plot
    

    #local clustering coefficient plot


    #shortest path lengths plot


    file = open(fileName + "/" + fileName + "_data.txt", "w")
    #global clustering coefficient
    file.write("Global clustering coefficient: %s\n" % nx.average_clustering(G))

    #average shortest path length
    file.write("Average shortest path length: %s\n" % nx.average_shortest_path_length(G))

    #diameter of graph
    file.write("Diameter of the graph: %s\n" % nx.diameter(G))

    file.close()
