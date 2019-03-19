import matplotlib.pyplot as plt
import math
import networkx as nx
import random
import time

def adjacent_edges(nodes, k):
    n = len(nodes)
    for i, u in enumerate(nodes):
        for j in range(i+1, i+k+1):
            v = nodes[j % n]
            yield u, v

def make_ring_lattice(n, k):
    G = nx.Graph()
    nodes = range(n)
    G.add_nodes_from(nodes)
    G.add_edges_from(adjacent_edges(nodes, k))
    return G

def apl_first(n, k):
    sum_of_range = sum(range(1, int(math.ceil(n/(2.0*k))))) # 1+2+3..+n/2k
    return (2.0 * k * sum_of_range) / n

def apl_second(n, k):
    return n / (4.0*k)

def show_graph(G):
    nx.draw(G, pos=nx.circular_layout(G), nodecolor='r', edge_color='b')
    plt.show()

# Bug in NetworkX DEPRECATION
def save_graph(G, name):
    nx.draw(G, pos=nx.circular_layout(G), nodecolor='r', edge_color='b')
    plt.savefig(name+'.pdf', format="PDF")

if __name__ == '__main__':
    for i in range(0,5):
        print('***** Run #' + str(i+1) + '*****')
        n = random.randint(4, 10) * 10
        print('Number of vertices(n): ' + str(n))
        k = random.randint(1, max(1,(n/2) - 1))
        print('Number of neighbours(k): ' + str(k))
        G = make_ring_lattice(n, k)
        #save_graph(G, 'n' + str(n) + 'k' + str(k))
        apld = nx.average_shortest_path_length(G, 'dijkstra')
        aplb = nx.average_shortest_path_length(G, 'bellman-ford')
        apl1 = apl_first(n, k)
        apl2 = apl_second(n, k)
        print('Dijsktra: ' + str(apld))
        print('Bellman-ford: ' + str(aplb))
        print('First estimation: ' + str(apl1))
        print('Second estimation: ' + str(apl2))
