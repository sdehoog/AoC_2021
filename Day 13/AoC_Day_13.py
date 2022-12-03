import numpy as np

def fold_count(file_path, first_fold_only):

    folds = []
    points = []
    with open(file_path) as fin:
        for line in fin.readlines():
            if line.startswith('fold'):
                folds.append(line[11:].strip().split('='))
            elif line.startswith('\n'):
                pass
            else:
                points.append(tuple([int(x) for x in line.strip().split(',')]))

    max_y = 0
    max_x = 0

    for x, y in points:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
            
    paper = np.zeros((max_x + 1,max_y + 1))

    for point in points:
        paper[point] = 1


    
    for fold in folds:
        if fold[0] == 'x':
            row = int(fold[1])
            paper = np.delete(paper,(row), axis = 0)
            a, b = np.vsplit(paper,2)
            b = np.flipud(b)
            paper = a + b
        else:
            col = int(fold[1])
            paper = np.delete(paper, (col), axis = 1)
            a, b = np.hsplit(paper,2)
            b = np.fliplr(b)
            paper = a + b

        if first_fold_only:
            return np.count_nonzero(paper)
    
    paper = np.transpose(paper)
    
    for row in paper:
        for item in row:
            if item > 0:
                print('#',end='')
            else:
                print(' ', end='')
        print()

    return

def main():

    assert fold_count('test_input.txt', True) == 17
    print(fold_count('input.txt',True))

    fold_count('test_input.txt', False)
    fold_count('input.txt', False)

    fold_count('fun_input2.txt', False)

    
if __name__ == '__main__':
    main()
