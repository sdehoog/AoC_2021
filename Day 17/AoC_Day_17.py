from numpy import ceil, sqrt

def read_target(file_path):

    with open(file_path) as fin:
        line = fin.readline().strip()[15:]
    x_r, y_r = [(int(part.split('..')[0]), int(part.split('..')[1]))  for part in line.split(', y=')]
    return range(x_r[0], x_r[1] + 1), range(y_r[0], y_r[1] + 1)

def hit_target(v_x, v_y, x_r, y_r):
    # This only works for positive x target ranges
    
    if min(x_r) < 0:
        raise Exception('x target range is negative')
    
    x = 0
    y = 0

    while x < max(x_r) and y > min(y_r):
        x += v_x
        y += v_y
        if v_x > 0:
            v_x -= 1
        v_y -= 1
        
        if x in x_r and y in y_r:
            return True

    return False
        

def part1(file_path):
    # This only works for y target ranges that are completely negative
    
    x_r, y_r = read_target(file_path)

    if max(y_r) > 0:
        raise Exception('y target range is positive.')

    n = abs(min(y_r)) - 1

    return (n * (n + 1)) // 2

def part2(file_path):
    # This only works for y target ranges that are completely negative

    x_r, y_r = read_target(file_path)

    if max(y_r) > 0:
        raise Exception('y target range is positive.')

    v_x_min = int(ceil((-1 + sqrt(1 - 4 * (-2 * min(x_r)))) / 2))

    v_x_r = range(v_x_min,max(x_r)+ 1)

    v_y_r = range(min(y_r), abs(min(y_r)))

    hit_count = 0

    for v_x in v_x_r:
        for v_y in v_y_r:
            if hit_target(v_x, v_y, x_r, y_r):
                hit_count += 1

    return hit_count
    


def main():

    assert part1('test_input.txt') == 45
    print(part1('input.txt'))

    assert part2('test_input.txt') == 112
    print(part2('input.txt'))


if __name__ == '__main__':
    main()
