import heapq as hq
import numpy as np
from time import perf_counter


class Graph:

    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self.outgoing[v]) for v in self.outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj([v]))

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x = None):
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        return e

    class Vertex:

        __slots__ = '_element'

        def __init__(self, x):
            self._element = x

        def element(self):
            return self._element

        def __hash__(self):
            return hash(id(self))

        def __lt__(a, b):
            if type(a) == type(b):
                if type(a) == type(tuple()):
                    return a < b.element()
                elif type(b) == type(tuple()):
                    return a.element() < b
            return False

    class Edge:

        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            return (self._origin, self._destination)

        def opposite(self, v):
            return self._destination if v is self._origin else self._origin

        def element(self):
            return self._element
                                 
def get_neighbors(node, max_x, max_y):
    
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = []
    
    for dx, dy in dirs:
        neighbor = (node[0] + dx, node[1] + dy)
        if 0 <= neighbor[0] < max_x and 0 <= neighbor[1] < max_y:
            result.append(neighbor)
            
    return result

def shortest_path_lengths(g, src):
    d = {}
    cloud = {}
    pq = []
    pqlocator = {}

    for v in g.vertices():
        if v is src:
            d[v] = 0
            hq.heappush(pq, (d[v], v))

        else:
            d[v]= float('inf')
##        pqlocator[v] = (d[v], v)
        hq.heappush(pq, (d[v], v))

    while len(pq):
        key, u = hq.heappop(pq)
        if u in cloud:
            if cloud[u] > key:
                cloud[u] = key
            else:
                continue
        else:
            cloud[u] = key
        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v not in cloud:
                wgt = e.element()
                if d[u] + wgt < d[v]:
                    d[v] = d[u] + wgt
##                    pq[pq.index(pqlocator[v])] = (d[v], v)
                    hq.heappush(pq, (d[v], v))
##                    pqlocator[v] = (d[v], v)

    return cloud

def chiton_route_risk(file_path, map_multi):
    
    with open(file_path) as fin:
        c_map = np.genfromtxt(fin, delimiter = 1)
        
    if map_multi == 1:
        pass
    else:
        new_map = np.zeros((np.shape(c_map)[0] * map_multi, np.shape(c_map)[1] * map_multi))
        for i in range(map_multi):
            for j in range(map_multi):
                nb = c_map + i + j
                nb[nb > 9] = nb[nb > 9] % 10 + 1
                i_r, j_r = np.shape(nb)
                new_map[i*i_r:i_r*(1+i),j*j_r:j_r*(1+j)] = nb
        c_map = new_map
    g = Graph(True)

    max_x, max_y = np.shape(c_map)

    v = [[''] * max_y for x in range(max_x)]

    for i in range(max_x):
        for j in range(max_y):
            v[i][j] = g.insert_vertex((i,j))

    for row in v:
        for entry in row:
            for nb_x, nb_y in get_neighbors(entry.element(),max_x,max_y):
                g.insert_edge(entry, v[nb_x][nb_y], c_map[(nb_x, nb_y)])

    paths = shortest_path_lengths(g,v[0][0])

    return int(paths[v[-1][-1]])

def main():

    start = perf_counter()
    assert chiton_route_risk('test_input.txt', 1) == 40
    print('Part 1 Test in:', perf_counter() - start)
    print(chiton_route_risk('input.txt', 1))
    print('Part 1 actual:', perf_counter() - start)

    assert chiton_route_risk('test_input.txt', 5) == 315
    print('Part 2 Test in:', perf_counter() - start)
    print(chiton_route_risk('input.txt', 5))
    print('Part 2 actual:', perf_counter() - start)

if __name__ == '__main__':
    main()

    

                
