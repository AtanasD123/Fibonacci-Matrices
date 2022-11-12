import numpy as np
from numpy.linalg import eig

# Source https://medium.com/@andrew.chamberlain/the-linear-algebra-view-of-the-fibonacci-sequence-4e81f78935a3

A = np.array([[1, 1], [1, 0]])
c = np.array([1, 0])        # Any two consecutive fib numbers                 

N = 5                      # Index of fib number to be computed (eg. n = 4 results in [8, 5] = [F6, F5])
eigen_values, S = eig(A)

diagonal_matrix = np.array([[eigen_values[0], 0], [0, eigen_values[1]]])

result = np.dot(np.dot(S, np.power(diagonal_matrix, N)), np.dot(np.linalg.inv(S), c)) # S * D * (S^-1 * u0)

print(result)


