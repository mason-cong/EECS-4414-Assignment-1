import networkx as net

def watts_graphs():
    n = 1000
    k = 3
    p = 1/4
    #1
    G = net.watts_strogatz_graph(n, k, p)
    net.draw(G)
    #2
    #p = 1/5
    #G = net.watts_strogatz_graph(n, k, p)
    #3
    #p = 1/6
    #G = net.watts_strogatz_graph(n, k, p)
watts_graphs()

