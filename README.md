# BitonicTSP

This is a no-frills implementation of a bitonic TSP algorithm in C with a Python binding. There is some mitigable overhead in the Python binding, but this code is primarily intended to provide speed-up over a pure Python implementation (such as that in [TSP-vs-Graphs](https://github.com/samvanderpoel/TSP-vs-Graphs)), especially on problem instances with more than 1000 points. The included code was tested on MacOS.

To set up the shared library, run
```
gcc -shared -o bitolib.so -fPIC bitonic.c
```
