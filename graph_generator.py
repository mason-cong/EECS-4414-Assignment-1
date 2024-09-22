import networkx as net
import matplotlib.pyplot as plt

def watts_graphs():
    n = 1000
    k = 4
    p = 0.25
    #1
    G = net.watts_strogatz_graph(n, k, p)
    net.draw(G)
    plt.show()
    #list(G.nodes)S
    #2
    #p = 1/5
    #G = net.watts_strogatz_graph(n, k, p)
    #3
    #p = 1/6
    #G = net.watts_strogatz_graph(n, k, p)

watts_graphs()

