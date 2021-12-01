import numpy as np
import matplotlib.pyplot as plt
import functions

# create grid of h
h_lb = 0.1
h_ub = 4
size_h = 300
h_grid = np.linspace(h_lb, h_ub, size_h)

# define parameters
beta = 0.95
delta = 0.9
omega = 0.5
phi = 0.5
params = [beta, delta, omega, phi]
u = np.zeros((size_h,size_h))
c = np.zeros((size_h,size_h))

# call value function from functions.py
x = functions.vfi(params, h_grid, u, c)

# create visualization of value function
plt.figure()
plt.plot(h_grid, x[0])
plt.xlabel('Size of Health')
plt.ylabel('Value Function')
