import argparse
import ctypes
import numpy as np
import numpy.ctypeslib as ctl
import os

def get_bitonic_edges(coords, k=0):
    n = len(coords)
    coords = [[x,y] for x, y in coords]
    os.system(
        f"python bitonic.py --coords \"{coords}\" > res{k}.txt"
    )
    lines = open(f"res{k}.txt", "r").readlines()
    os.remove(f"res{k}.txt")
    edges = [
        (int(x), int(y))
        for x, y in [
            line.strip().split('\t')
            for line in lines
        ]
    ]
    return edges + [(n-2, n-1)]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--coords', type=str, required=True)
    coords_input = eval(parser.parse_args().coords)
    coords_sort = sorted(coords_input, key=lambda k: [k[0], k[1]])
    coords_flat = [c for pair in coords_sort for c in pair]

    libname = 'bitolib.so'
    libdir = './'
    lib = ctl.load_library(libname, libdir)

    py_bitonic = lib.bitonic
    py_bitonic.argtypes = [
        ctl.ndpointer(
            np.float64,
            flags='aligned, c_contiguous'
        ), 
        ctypes.c_int
    ]
    A = np.array(coords_flat, dtype=np.float64)
    py_bitonic(A, int(len(coords_flat)/2))
