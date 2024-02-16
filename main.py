import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
np.random.seed(1)

from smooths import sigma, sigman, sigmam, s
from kernels import circular_kernel_pair


def initialize_state(HEIGHT, WIDTH, R_A, FACTOR, MASK_RATIO, ORGANISM_COUNT):
    b_kernel, s_kernel = circular_kernel_pair(R_A,FACTOR)
    sim_state = np.zeros((HEIGHT,WIDTH),dtype=np.float16)
    mask_height, mask_width = int(HEIGHT*MASK_RATIO),int(WIDTH*MASK_RATIO)

    for i in range(ORGANISM_COUNT):
        mask = np.random.rand(mask_height, mask_width)
        start_x = np.random.randint(0, WIDTH-mask_width+1)
        start_y = np.random.randint(0, HEIGHT-mask_height+1)
        sim_state[start_y:start_y+mask_height\
                    ,start_x:start_x+mask_width] += mask
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
    sim_state_diff= 2*q - 1
    return sim_state_diff

def get_next_state(HEIGHT,WIDTH,R_A,FACTOR,MASK_RATIO,ALPHA_N,ALPHA_M,B1,B2,D1,D2,DT,ORGANISM_COUNT):

    s_kernel, b_kernel, sim_state = initialize_state(HEIGHT, WIDTH, R_A, FACTOR, MASK_RATIO, ORGANISM_COUNT)
    
    #plt.imshow(sim_state, cmap='gray')
    #plt.axis('off')
    #plt.savefig(f'./ims/output_image{0:06d}.jpg', bbox_inches='tight', pad_inches=0)
    

    while True:
        yield sim_state
        sim_state_diff = run_sim(sim_state, s_kernel, b_kernel, B1, D1, B2, D2, ALPHA_N, ALPHA_M)
        #print(sim_state_diff)
        sim_state += DT*sim_state_diff
        sim_state[sim_state<0]=0
        print(sim_state)
        #plt.imshow(sim_state, cmap='gray')
        #plt.axis('off')
        #plt.savefig(f'./ims/output_image{i:06d}.jpg', bbox_inches='tight', pad_inches=0)

    