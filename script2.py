import numpy as np

# Dados de entrada
X = np.array([[1, -2], [1, -2], [1, -1], [1, -1], [1, 0], [1, 0], [1, 1], [1, 1], [1, 2], [1, 2]])
y = np.array([0, 0, 2, 3, 4, 4, 5, 6, 8, 8]).reshape(-1, 1)

# Fórmula matricial condensada em uma única linha: beta = (X^T * X)^-1 * X^T * y
beta = np.linalg.inv(X.T @ X) @ X.T @ y

print("Coeficientes (Beta):")
print(beta)