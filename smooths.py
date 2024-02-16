import numpy as np

def sigma1(x,a,alpha):
    return 1.0/(1.0+np.exp(-1*(x-a)*4/alpha))
def sigma2(x, a, b, alpha):
    return sigma1(x, a, alpha) * (1.0 - sigma1(x, b, alpha))
def sigmam(x, y, m, alpha):
    return x*(1.0-sigma1(m, 0.5, alpha)) + y*sigma1(m, 0.5, alpha)
def s(n, m, b1, d1, b2, d2, alpha):
    return sigma2(n, sigmam(b1, d1, m, alpha), sigmam(b2, d2, m, alpha), alpha)