import numpy as np
import matplotlib.pyplot as plt
from line_search_bt import *

obj = lambda x: 5 * x[0] ^ 2 + 10 * x[1] ^ 2 + 5 + 12 * x[0] * x[1] - 14 * x[1] - 8 * x[0]
grad = lambda x: np.matrix([10 * x[0] + 12 * x[1] - 8, 12 * x[0] + 20 * x[1] - 14])
# termination criterion
conv = .0001
x0 = 0.  # initial guess
k = 0  # counter
soln = [x0]  # use an array to store the search steps
x = soln[k]  # start with the initial guess
error = np.linalg.norm(
    grad(x))  # compute the error. Note you will need to compute the norm for 2D grads, rather than the absolute value
# a = 0.01  # set a fixed step size to start with

# Armijo line search


def line_search(x):
    a = 1.  # initialize step size
    phi = lambda a, x: obj(x) - a * 0.8 * grad(x) ** 2  # define phi as a search criterion
    while phi(a, x) < obj(x - a * grad(x)):  # if f(x+a*d)>phi(a) then backtrack. d is the search direction
        a = 0.5 * a
    return a


while error >= conv:  # keep searching while gradient norm is larger than eps
    a = line_search(x)
    x = x - a * grad(x)
    soln.append(x)
    error = np.linalg.norm(grad(x))

soln  # print the search trajectory