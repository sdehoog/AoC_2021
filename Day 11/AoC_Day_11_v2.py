import numpy as np

def get_adj(loc):
    adj_loc = []
    x, y = loc
    for i in range(-1, 2):
        for j in range(-1, 2):
            if ((x + i) in range(10) and
                (y + j) in range(10) and
                not (i == j == 0)):
                adj_loc.append((x + i, y + j))

    return adj_loc

def flash_count(file_path, sync):
    o_map = np.genfromtxt(file_path, dtype = 'int', delimiter = 1)

    flash_count = 0
        
    for step in range(1,1000):
        o_map += 1
        
        while o_map.max() > 9:
            flash = np.nonzero(o_map > 9)
            o_map[flash] = 0
            for loc in zip(flash[0],flash[1]):
                for adj_loc in get_adj(loc):
                    if o_map[adj_loc] != 0:
                        o_map[adj_loc] += 1

        flash_count += np.count_nonzero(o_map == 0)
        
        if np.count_nonzero(o_map == 0) == 100:
            return step
        
        if step == 100 and not sync:
            return flash_count

def main():
    
    assert flash_count('test_input.txt', False) == 1656
    print(flash_count('input.txt', False))

    assert flash_count('test_input.txt', True) == 195
    print(flash_count('input.txt', True))


if __name__ == '__main__':
    main()
