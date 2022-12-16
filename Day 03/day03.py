from time import time
import numpy as np


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


@timer_func
def day03(filepath, part2=False):
    with open(filepath) as fin:
        data = np.genfromtxt(fin, dtype=int, delimiter=1)

    if not part2:
        most_common = ''
        least_common = ''
        for col in range(data.shape[1]):
            val = 1 if np.average(data[:, col]) > 0.5 else 0
            o_val = 0 if val == 1 else 1
            most_common += str(val)
            least_common += str(o_val)

        return int(most_common, 2) * int(least_common, 2)

    else:
        ox = data
        co2 = data
        for col in range(data.shape[1]):
            val = 1 if np.average(ox[:, col]) >= 0.5 else 0
            ox = ox[ox[:,col] == val]
            if ox.shape[0] == 1:
                break
        ox = ''.join([str(x) for x in np.nditer(ox)])

        for col in range(data.shape[1]):
            val = 0 if np.average(co2[:, col]) >= 0.5 else 1
            co2 = co2[co2[:,col] == val]
            if co2.shape[0] == 1:
                break
        co2 = ''.join([str(x) for x in np.nditer(co2)])
        return int(ox, 2) * int(co2, 2)


def main():
    assert day03('test03') == 198
    print(f"Part 1: {day03('input03')}")

    assert day03('test03', True) == 230
    print(f"Part 2: {day03('input03', True)}")


if __name__ == '__main__':
    main()
