import numpy as np

def circular_kernel(r):
    kernel = np.zeros((r*2+1, r*2+1))
    for row in range(kernel.shape[0]):
        for col in range(kernel.shape[1]):
            x, y = col,(r*2)-row
            if r**2>= (x-r)**2+(y-r)**2:
                kernel[row][col] = 1
    return kernel

def circular_kernel_pair(r_a, factor):
    m = circular_kernel(r_a)
    r_i = r_a//factor
    n = circular_kernel(r_i)

    m[r_a-r_i:r_a+1+r_i, r_a-r_i:r_a+1+r_i] -= n
    n[r_i, r_i] = 0
    m[r_a, r_a] = 0
    return (m, n)