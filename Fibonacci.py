import numpy as np
from numpy.linalg import eig
from scipy import interpolate
import matplotlib.pyplot as plt


# Source https://medium.com/@andrew.chamberlain/the-linear-algebra-view-of-the-fibonacci-sequence-4e81f78935a3

A = np.array([[1, 1], [1, 0]])
c = np.array([1, 0])        # Any two consecutive fib numbers                 

N = 1                      # Index of fib number to be computed (eg. n = 4 results in [8, 5] = [F6, F5])
eigen_values, S = eig(A)

diagonal_matrix = np.diag(eigen_values)

result_1 = np.dot(np.dot(S, np.power(diagonal_matrix, N)), np.dot(np.linalg.inv(S), c)) # S * D * (S^-1 * u0)
result_2 = np.dot(np.dot(S, np.power(diagonal_matrix, N+1)), np.dot(np.linalg.inv(S), c)) # S * D * (S^-1 * u0)
matrix = np.array([result_1, result_2])
N = N + 2

while N < 51:
    result_1 = np.dot(np.dot(S, np.power(diagonal_matrix, N)), np.dot(np.linalg.inv(S), c)) # S * D * (S^-1 * u0)
    matrix = np.vstack((matrix, result_1))
    N = N + 1

x = matrix[:, 0]
print(x)

golden_ratio_matrix = np.zeros((N, 2))
count = 0
state = 0
row = 1
while(count < N - 1):
    if(state == 0):
        golden_ratio_matrix[row][0] = golden_ratio_matrix[row - 1][0] - x[count]
        golden_ratio_matrix[row][1] = golden_ratio_matrix[row - 1][1] + x[count]
        state = state + 1
        count = count + 1
        row = row + 1
    elif(state == 1):
        golden_ratio_matrix[row][0] = golden_ratio_matrix[row - 1][0] - x[count]
        golden_ratio_matrix[row][1] = golden_ratio_matrix[row - 1][1] - x[count]
        state = state + 1
        count = count + 1
        row = row + 1
    elif(state == 2):
        golden_ratio_matrix[row][0] = golden_ratio_matrix[row - 1][0] + x[count]
        golden_ratio_matrix[row][1] = golden_ratio_matrix[row - 1][1] - x[count]
        state = state + 1
        count = count + 1
        row = row + 1
    elif(state == 3):
        golden_ratio_matrix[row][0] = golden_ratio_matrix[row - 1][0] + x[count]
        golden_ratio_matrix[row][1] = golden_ratio_matrix[row - 1][1] + x[count]
        state = state + 1
        count = count + 1
        row = row + 1
        state = 0
    
x = golden_ratio_matrix[:, 0]
y = golden_ratio_matrix[:, 1]


print(golden_ratio_matrix)

plt.plot(x, y, "-o")
plt.show()




