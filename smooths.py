import numpy as np

def sigma(x, a, alpha):
    return 1.0/(1.0+np.exp(-1*(x-a)*4/alpha))
def sigman(x, a, b, alpha_n):
    return sigma(x, a, alpha_n)*(1.0-sigma(x, b, alpha_n))
def sigmam(x, y, m, alpha_m):
    return x*(1.0-sigma(m, 0.5, alpha_m))+y*sigma(m, 0.5, alpha_m)
def s(n, m, b1, d1, b2, d2, alpha_n, alpha_m):
    return sigman(n, sigmam(b1, d1, m, alpha_m), sigmam(b2, d2, m, alpha_m), alpha_n)