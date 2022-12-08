def day01(filepath, sliding_range=1):
    with open(filepath) as fin:
        lines = [int(i) for i in fin.readlines()]

    return len([1 for i in range(len(lines) - sliding_range) if sum(lines[i:i+sliding_range]) < sum(lines[i+1:i+1+sliding_range])])


def main():
    assert day01('test01') == 7
    print(day01('input01'))

    assert day01('test01', 3) == 5
    print(day01('input01', 3))


if __name__ == '__main__':
    main()
