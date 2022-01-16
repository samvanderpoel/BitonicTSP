import argparse
import ctypes
import numpy as np
import numpy.ctypeslib as ctl
import os

def get_bitonic_edges(coords, k):
    os.system("python bitonic.py --coords \"" \
              + str(coords) + "\" > res" + str(k) + ".txt")
    lines = open("res" + str(k) + ".txt", "r").readlines()
    os.remove("res" + str(k) + ".txt")
    edges = [(int(x), int(y))
             for x, y in [line.strip().split('\t')
             for line in lines]]
    return edges

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--coords', type=str, required=True)
    args = parser.parse_args()
    coords = eval(args.coords)
    coords = [c for pair in coords for c in pair]

    libname = 'bitolib.so'
    libdir = './'
    lib = ctl.load_library(libname, libdir)

    py_bitonic = lib.bitonic
    py_bitonic.argtypes = [ctl.ndpointer(np.float64, 
                                         flags='aligned, c_contiguous'), 
                           ctypes.c_int]
    A = np.array(coords, dtype=np.float64)
    py_bitonic(A, int(len(coords)/2))
