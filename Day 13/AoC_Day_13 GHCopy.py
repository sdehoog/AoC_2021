import sys
from collections import defaultdict
import numpy as np

dotsdict = defaultdict(list)
folds = []

with open('input.txt') as input_file:
    for line in input_file:
        if line[0:4] == "fold":
            folds.append([line[11], int(line[13:].strip())])
        elif line.strip() != "":
            x, y = map(int, line.strip().split(","))
            dotsdict[x].append(y)


maxsizey = max(dotsdict.keys()) + 1
maxsizex = max(max(subdict) for subdict in dotsdict.values()) + 1

dots = np.full((maxsizex, maxsizey), False)

for y, xs in dotsdict.items():
    for x in xs:
        dots[x, y] = True

for fold in folds:
    if fold[0] == "y":
        belowfold = np.flipud(dots[fold[1]+1:, :])
        dots = dots[:fold[1], :] | belowfold
    else:
        belowfold = np.fliplr(dots[:, fold[1]+1:])
        dots = dots[:, :fold[1]] | belowfold

dotsprint = np.full(dots.shape, ".")
dotsprint[dots] = "#"
np.set_printoptions(linewidth=200)
print(dotsprint)
