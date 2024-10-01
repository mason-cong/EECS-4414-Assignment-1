import networkx as nx
import matplotlib.pyplot as plt
from graph_calculator import calculateGraphMeasurements

def watts_graphs():
    #1
    n = 1000
    k = 20
    p = 1/5
    fileName = "ws1"

    G = nx.watts_strogatz_graph(n, k, p)
    calculateGraphMeasurements(G, fileName)

    #2
    n = 1000
    k = 20
    p = 1/7
    fileName = "ws2"

    G = nx.watts_strogatz_graph(n, k, p)
    calculateGraphMeasurements(G, fileName)

    #3
    n = 1000
    k = 20
    p = 1/2
    fileName = "ws3"

    G = nx.watts_strogatz_graph(n, k, p)
    calculateGraphMeasurements(G, fileName)
    
watts_graphs()

