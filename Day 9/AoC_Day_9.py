def search(loc, loc_list, h_map):

    a_loc = [[loc[0] + 1, loc[1]],
             [loc[0] - 1, loc[1]],
             [loc[0], loc[1] + 1],
             [loc[0], loc[1] - 1]]

    for pos_loc in a_loc:
        if (pos_loc not in loc_list and
            h_map[pos_loc[0]][pos_loc[1]] != 9):
            loc_list.append(pos_loc)
            loc_list = search(pos_loc, loc_list, h_map)

    return loc_list

def find_lows(file_path, count_only):

    with open(file_path) as fin:
        h_map = [str(x) for x in fin.read().split('\n')]
    for ind, row in enumerate(h_map):
        h_map[ind] = [int(x) for x in str(row)]
        h_map[ind].insert(0,9)
        h_map[ind].append(9)

    h_map.insert(0, [9] * len(h_map[0]))
    h_map.append([9] * len(h_map[0]))

    danger_sum = 0
    low_loc = []
    
    for r_i in range(1, len(h_map) - 1):
        for c_i in range(1, len(h_map[r_i]) - 1):
            val = h_map[r_i][c_i]
            if (val < h_map[r_i + 1][c_i] and
                val < h_map[r_i - 1][c_i] and
                val < h_map[r_i][c_i + 1] and
                val < h_map[r_i][c_i - 1]):
                    danger_sum += val + 1
                    low_loc.append([r_i, c_i])

    if count_only:
        return danger_sum

    top_three = [0, 0, 0]
    
    for loc in low_loc:
        loc_list = search(loc, [loc], h_map)
        loc_size = len(loc_list)
        
        if loc_size > min(top_three):
            top_three.pop(top_three.index(min(top_three)))
            top_three.append(loc_size)

    return (top_three[0] * top_three[1] * top_three[2])

if __name__ == '__main__':

    assert find_lows('test_input.txt', True) == 15
    print(find_lows('input.txt', True))

    assert find_lows('test_input.txt', False) == 1134
    print(find_lows('input.txt', False))
