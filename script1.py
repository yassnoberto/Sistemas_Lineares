import numpy as np
A = [
    [10, 7, 8, 7],
    [7, 5, 6, 5],
    [8, 6, 10, 9],
    [7, 5, 9, 10]
]
B = [32, 23, 33, 31]
x = np.dot(np.linalg.inv(A), B)

print(x)