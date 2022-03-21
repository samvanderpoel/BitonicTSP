import os
import numpy as np
from bitonic import *

def uniform_square(numpts, xlim=[0,1], ylim=[0,1]):
    xs = xlim[0] + abs(xlim[1]-xlim[0]) * np.random.random(numpts)
    ys = ylim[0] + abs(ylim[1]-ylim[0]) * np.random.random(numpts)
    return np.asarray(list(zip(xs,ys)))

if __name__ == "__main__":
    numpts = 250
    coords = uniform_square(numpts)
    edges = get_bitonic_edges(coords)
    print(edges)
