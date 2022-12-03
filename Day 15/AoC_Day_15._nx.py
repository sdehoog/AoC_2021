import sys
import networkx as nx
import numpy as np
from time import perf_counter



data = np.genfromtxt('input.txt', delimiter=1, dtype=int)    
data = np.concatenate((data, data + 1, data + 2, data + 3, data + 4), axis=0)
data = np.concatenate((data, data + 1, data + 2, data + 3, data + 4), axis=1)

data[data > 9] -= 9
G = nx.DiGraph()

for ix, iy in np.ndindex(data.shape):
    if ix > 0: 
        G.add_edge((ix - 1, iy), (ix, iy), weight = data[(ix, iy)])

    if ix < data.shape[0] - 1:
        G.add_edge((ix + 1, iy), (ix, iy), weight = data[(ix, iy)])

    if iy > 0:
        G.add_edge((ix, iy - 1), (ix, iy), weight = data[(ix, iy)])

    if iy < data.shape[1] -1:
        G.add_edge((ix, iy + 1), (ix, iy), weight = data[(ix, iy)])



start = perf_counter()
print(nx.dijkstra_path_length(G, (0, 0), (data.shape[0] - 1, data.shape[1] -1)))
print('Completed in :', perf_counter() - start)
