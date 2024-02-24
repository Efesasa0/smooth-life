import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
np.random.seed(1)

from smooths import s
from kernels import circular_kernel_pair

def initialize_state(height, width, r_a, factor, mask_ratio, organism_count):
    b_kernel, s_kernel = circular_kernel_pair(r_a, factor)
    sim_state = np.zeros((height, width), dtype=np.float16)
    mask_height, mask_width = int(height*mask_ratio), int(width*mask_ratio)

    for i in range(organism_count):
        mask = np.random.rand(mask_height, mask_width)
        start_x = np.random.randint(0, width-mask_width+1)
        start_y = np.random.randint(0, height-mask_height+1)
        sim_state[start_y:start_y+mask_height,\
                start_x:start_x+mask_width] += mask
    return (s_kernel, b_kernel, sim_state)

def run_sim(sim_state, s_kernel, b_kernel, B1, D1, B2, D2, alpha_n, alpha_m):
    n = convolve2d(sim_state, s_kernel, mode='same')
    N = s_kernel.sum().sum()
    m = convolve2d(sim_state, b_kernel, mode='same')
    M = b_kernel.sum().sum()
    n = n / N
    m = m / M
    apply_s_func = np.vectorize(s)
    q = apply_s_func(n, m, B1 ,D1, B2, D2, alpha_n, alpha_m)
    sim_state_diff= 2*q-1
    return sim_state_diff

def get_next_state(height ,width, r_a, factor, mask_ratio, alpha_n, alpha_m, b1, b2, d1, d2, dt, organism_count):
    s_kernel, b_kernel, sim_state = initialize_state(height, width, r_a, factor, mask_ratio, organism_count)
    #plt.imshow(sim_state, cmap='gray')
    #plt.axis('off')
    #plt.savefig(f'./ims/output_image{0:06d}.jpg', bbox_inches='tight', pad_inches=0)
    while True:
        yield sim_state
        sim_state_diff = run_sim(sim_state, s_kernel, b_kernel, b1, d1, b2, d2, alpha_n, alpha_m)
        #print(sim_state_diff)
        sim_state += dt*sim_state_diff
        sim_state[sim_state<0] = 0
        #print(sim_state)
        #plt.imshow(sim_state, cmap='gray')
        #plt.axis('off')
        #plt.savefig(f'./ims/output_image{i:06d}.jpg', bbox_inches='tight', pad_inches=0)