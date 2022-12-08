import time

def find_crab_fuel(file_path, constant_fuel_burn):

    with open(file_path) as fin:
        crab_pos = [int(x) for x in fin.read().split(',')]

    max_pos = max(crab_pos)
    min_pos = min(crab_pos)
    
    fuel = []


    for pos_pos in range(min_pos, max_pos + 1):
        fuel.append(0)
        for crab in crab_pos:
            if constant_fuel_burn:
                fuel[-1] += abs(crab - pos_pos)
            else:
                fuel[-1] += sum(range(abs(crab - pos_pos) + 1))

    return min(fuel)

if __name__ == '__main__':
    
    start_time = time.time()
    assert find_crab_fuel('test_input.txt', True) == 37
    print('Part 1 test execution time:', 1000*(time.time() - start_time), 'milliseconds')

    start_time = time.time()
    print(find_crab_fuel('input.txt', True))
    print('Part 1 execution time:', 1000*(time.time() - start_time), 'milliseconds')
    
    start_time = time.time()
    assert find_crab_fuel('test_input.txt', False) == 168
    print('Part 2 test execution time:', 1000*(time.time() - start_time), 'milliseconds')
    
    start_time = time.time()
    print(find_crab_fuel('input.txt', False))
    print('Part 2 execution time:', 1000*(time.time() - start_time), 'milliseconds')
    
