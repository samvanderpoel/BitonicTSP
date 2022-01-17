#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double *allocate_doubles(int m);
void deallocate_doubles(double* ptr);
int *allocate_ints(int m);
void deallocate_ints(int* ptr);
double norm(double px, double py, double qx, double qy);

void bitonic(double* points, int N) {
    int i, k, l;
    
    double *minlengths = allocate_doubles(N);
    minlengths[0] = 0.0;
    minlengths[1] = norm(points[0], points[1],
                         points[2], points[3]);
    int *partial_path_edges = allocate_ints(2*N*N);
    partial_path_edges[0] = 1;
    partial_path_edges[1] = 0;
    int *partial_path_delim = allocate_ints(N+1);
    partial_path_delim[0] = 0;
    partial_path_delim[1] = 1;

    for (l=2; l<N; ++l) {
        double *path_vals = allocate_doubles(l-1);
        for (i=2; i<l+1; ++i) {
            double tempnorm = norm(points[2*l], points[2*l+1],
                                   points[2*(i-2)], points[2*(i-2)+1]);
            double pathlength = 0.0;
            for (k=i; k<l; ++k) {
                pathlength += norm(points[2*k], points[2*k+1],
                                   points[2*(k-1)], points[2*(k-1)+1]);
            }
            path_vals[i-2] = tempnorm + minlengths[i-1] + pathlength;
        }

        int minind = 0;
        for (k=1; k<l-1; ++k) {
            if (path_vals[k] < path_vals[minind])
                minind = k;
        }
        minlengths[l] = path_vals[minind];

        int j = 2*partial_path_delim[l-1];
        for (k=partial_path_delim[minind];
             k<partial_path_delim[minind+1];
             ++k) {
            partial_path_edges[j] = partial_path_edges[2*k];
            partial_path_edges[j+1] = partial_path_edges[2*k+1];
            j += 2;
        }
        partial_path_edges[j] = l;
        partial_path_edges[j+1] = minind;
        for (k=minind+2; k<l; ++k) {
            j += 2;
            partial_path_edges[j] = k-1;
            partial_path_edges[j+1] = k;
        }

        partial_path_delim[l] = (j+2)/2;

        deallocate_doubles(path_vals);
    }

    for (k=partial_path_delim[N-2];
         k<partial_path_delim[N-1];
         ++k) {
        printf("%d\t%d\n",
               partial_path_edges[2*k],
               partial_path_edges[2*k+1]);
    }

    deallocate_doubles(minlengths);
    deallocate_ints(partial_path_edges);
    deallocate_ints(partial_path_delim);
}

double norm(double px, double py, double qx, double qy) {
    return sqrt(
        pow(px-qx, 2) +
        pow(py-qy, 2)
    );
}

double *allocate_doubles(int m) {
    double* M;
    M = (double *)malloc(sizeof(double) * m);
    return M;
}

void deallocate_doubles(double* ptr) {
    free(ptr); ptr=NULL;
}

int *allocate_ints(int m) {
    int* M;
    M = (int *)malloc( sizeof(int) * m);
    return M;
}

void deallocate_ints(int* ptr) {
    free(ptr); ptr=NULL;
}
