import numpy as np

def fold_count(file_path, first_fold_only):

    folds = []
    points = []
    with open(file_path) as fin:
        points, folds = fin.read().strip().split('\n\n')
        points = [(int(point.split(",")[0]), int(point.split(",")[1])) for point in points.splitlines()]
        folds = [(axis[-1], int(val)) for fold in folds.splitlines() for axis, val in [fold.split("=")]]

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


    
    for axis, loc in folds:
        loc = int(loc)
        if axis == 'x':
            b = paper[(loc+1):,:]
            b = np.flipud(b)
            paper[(2*loc - len(paper)+1):loc,:] += b
            paper = paper[:loc,:]
        else:
            b = paper[:,(loc+1):]
            b = np.fliplr(b)
            paper[:,(2*loc-len(paper[0])+1):loc] += b
            paper = paper[:,:loc]

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
