def day02(filepath, read_manual=False):
    with open(filepath) as fin:
        lines = [line.split() for line in fin.readlines()]

    h_pos = 0
    depth = 0
    if not read_manual:
        for line in lines:
            if line[0] == 'forward':
                h_pos += int(line[1])
            elif line[0] == 'down':
                depth += int(line[1])
            elif line[0] == 'up':
                depth -= int(line[1])
            else:
                print('oops')
    else:
        aim = 0
        for line in lines:
            if line[0] == 'forward':
                h_pos += int(line[1])
                depth += aim * int(line[1])
            elif line[0] == 'down':
                aim += int(line[1])
            elif line[0] == 'up':
                aim -= int(line[1])
            else:
                print('oops')

    return h_pos * depth


def main():
    assert day02('test02') == 150
    print(day02('input02'))

    assert day02('test02', True) == 900
    print(day02('input02', True))


if __name__ == '__main__':
    main()
