import os
import numpy as np
from bitonic import *

def pts_uni(numpts, xlim=[0,1], ylim=[0,1]):
    xs = xlim[0] + abs(xlim[1]-xlim[0])*np.random.random(numpts)
    ys = ylim[0] + abs(ylim[1]-ylim[0])*np.random.random(numpts)
    return np.asarray(list(zip(xs,ys)))

numpts = 250
coords = sorted(pts_uni(numpts), key=lambda k: [k[0], k[1]])
edges = get_bitonic_edges(coords, 0)
print(edges)
