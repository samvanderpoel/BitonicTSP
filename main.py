import os
from bitonic import *

coords = [[0, 0], [4, 3], [5, -5], [6, -4], [7, -5], [8, -4], [9, 3], [13, 6], [17, 0]]
edges = get_bitonic_edges(coords, 0)
print(edges)
