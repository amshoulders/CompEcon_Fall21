import numpy as np
import matplotlib.pyplot as plt

# Value function iteration

def vfi(params, h_grid, u, c):
    beta, delta, omega, phi = params
    iter = 1
    max_iter = 1000
    v_diff = 7 # number doesn't matter just needs to be bigger that v_tol
    v_tol = 0.0001
    v_i = np.zeros_like(h_grid)
    v_mat = np.zeros_like(u)
    while v_diff > v_tol and iter < max_iter:
        for i, h in enumerate(h_grid):
            for j, h_prime in enumerate(h_grid):
                c = (h - h_prime)/delta
                u[i, j] = (omega * c) + (h ** (phi))
                v_mat[i, j] = u[i, j] + beta * v_i[j]
        v_ip1 = v_mat.max(axis=1)
        #make policy function - returns index of h' that is optimal
        PF = np.argmax(v_mat, axis=1)
        v_diff = np.abs(v_i - v_ip1).max()
        v_i = v_ip1
        iter += 1
        print('iteration = ', iter)
        # v_i+1 = max_h' u(-c, h) + beta v_i(h')
    if iter < max_iter:
        print('value function converged')
        print('difference = ', v_diff)
    else:
        print('value function did not converge')
    return(v_i, PF)
