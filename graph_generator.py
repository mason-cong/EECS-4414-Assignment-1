import networkx as nx
import matplotlib.pyplot as plt
from graph_calculator import calculateGraphMeasurements

def erdos_graphs():
    # Seed for reproducibility
    seed = 42
    # Parameters for the Erdős-Rényi graph (approx 1000 nodes and 10,000 edges)
    N = 1000
    E = 10000
    p_er = E / (N * (N - 1) / 2)  # probability for edge creation
    fileName = "er1"
    er_graph = nx.erdos_renyi_graph(N, p_er, seed=seed)
    calculateGraphMeasurements(er_graph, fileName)

    # Seed for reproducibility
    seed = 40
    # Parameters for the Erdős-Rényi graph (approx 1000 nodes and 10,000 edges)
    N = 1000
    E = 9500
    p_er = E / (N * (N - 1) / 2)  # probability for edge creation
    fileName = "er2"
    er_graph = nx.erdos_renyi_graph(N, p_er, seed=seed)
    calculateGraphMeasurements(er_graph, fileName)

    # Seed for reproducibility
    seed = 43
    # Parameters for the Erdős-Rényi graph (approx 1000 nodes and 10,000 edges)
    N = 1000
    E = 10500
    p_er = E / (N * (N - 1) / 2)  # probability for edge creation
    fileName = "er3"
    er_graph = nx.erdos_renyi_graph(N, p_er, seed=seed)
    calculateGraphMeasurements(er_graph, fileName)

def watts_graphs():
    #1
    seed = 4
    n = 1000
    k = 20
    p = 1/5
    fileName = "ws1"

    G = nx.watts_strogatz_graph(n, k, p, seed)
    calculateGraphMeasurements(G, fileName)

    #2
    seed = 5
    n = 1000
    k = 20
    p = 1/7
    fileName = "ws2"

    G = nx.watts_strogatz_graph(n, k, p, seed)
    calculateGraphMeasurements(G, fileName)

    #3
    seed = 6
    n = 1000
    k = 20
    p = 1/2
    fileName = "ws3"

    G = nx.watts_strogatz_graph(n, k, p, seed)
    calculateGraphMeasurements(G, fileName)
    
def barabasi_graphs():
    # Seed for reproducibility
    seed = 42
    # Parameters for the Barabási-Albert graph (approx 1000 nodes and 10,000 edges)
    N = 1000
    E = 10000
    m_ba = E // N  # number of edges to attach from a new node to existing nodes
    fileName = "ba1"
    # Barabási-Albert graph generation
    ba_graph = nx.barabasi_albert_graph(N, m_ba, seed=seed)
    calculateGraphMeasurements(ba_graph, fileName)

    # Seed for reproducibility
    seed = 40
    # Parameters for the Barabási-Albert graph (approx 1000 nodes and 10,000 edges)
    N = 1000
    E = 12000
    m_ba = E // N  # number of edges to attach from a new node to existing nodes
    fileName = "ba2"
    # Barabási-Albert graph generation
    ba_graph = nx.barabasi_albert_graph(N, m_ba, seed=seed)
    calculateGraphMeasurements(ba_graph, fileName)

    # Seed for reproducibility
    seed = 41
    # Parameters for the Barabási-Albert graph (approx 1000 nodes and 10,000 edges)
    N = 1000
    E = 11000
    m_ba = E // N  # number of edges to attach from a new node to existing nodes
    fileName = "ba3"
    # Barabási-Albert graph generation
    ba_graph = nx.barabasi_albert_graph(N, m_ba, seed=seed)
    calculateGraphMeasurements(ba_graph, fileName)

erdos_graphs()
watts_graphs()
barabasi_graphs()
