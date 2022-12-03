from collections import Counter
from functools import cache

class NodeList:

    def __init__(self):
        self.nodes =[]
        
    def add_node(self,name):
        self.nodes.append(Node(name))


    def get_names(self):
        return [x.name for x in self.nodes]

    def find_by_name(self, name):
        return self.nodes[self.get_names().index(name)]

    def __getitem__(self, i):
        return self.nodes[i]

    def __len__(self):
        return len(self.nodes)
        
class Node:

    def __init__(self, name):
        self.name = name
        self.neighbors = []
        if name.islower():
            self.size = 'small'
        else:
            self.size = 'big'

    def add_neighbor(self, nb):
        self.neighbors.append(nb)

def sde(check_path):

    smalls = []
    for entry in check_path:
        if entry.size == 'small':
            smalls.append(entry)
            
    counted = Counter(smalls)

    for count in counted.values():
        if count == 2:
            return True

    return False


def take_a_step(path, found_paths, sda):

    for nb in path[-1].neighbors:
        if nb.name == 'end':
            found_paths.append(path + [nb])
        elif nb.name == 'start':
            pass                
        elif nb.size =='big':            
            found_paths = take_a_step(path +[nb], found_paths, sda)
        elif not sda:
            if nb.size == 'small' and nb not in path:
                found_paths = take_a_step(path + [nb], found_paths, sda)
            elif nb.size == 'small' and nb in path:
                pass
        elif sda:
            if nb.size == 'small' and nb not in path:
                found_paths = take_a_step(path + [nb], found_paths, sda)
            elif nb.size == 'small' and nb in path and not sde(path):
                found_paths = take_a_step(path + [nb], found_paths, sda)
            else:
                pass          

    return found_paths


def find_path(file_path, sda):

    with open(file_path) as fin:
        connections = [x.split('-') for x in fin.read().strip().split('\n')]

    nodes = NodeList()
    
    for conn in connections:
        if conn[0] not in nodes.get_names():
            nodes.add_node(conn[0])
        if conn[1] not in nodes.get_names():
            nodes.add_node(conn[1])

    for conn in connections:
        nodes.find_by_name(conn[0]).add_neighbor(nodes.find_by_name(conn[1]))
        nodes.find_by_name(conn[1]).add_neighbor(nodes.find_by_name(conn[0]))
        
    start = nodes.find_by_name('start')

    path = [start]
    found_paths = []

    found_paths = take_a_step(path, found_paths, sda)

    return len(found_paths)
    
    
def main():

    assert find_path('test_input1.txt', False) == 10
    assert find_path('test_input2.txt', False) == 19
    assert find_path('test_input3.txt', False) == 226
    print(find_path('input.txt', False))

    assert find_path('test_input1.txt', True) == 36
    assert find_path('test_input2.txt', True) == 103
    assert find_path('test_input3.txt', True) == 3509
    print(find_path('input.txt', True))

if __name__ == '__main__':
    main()
