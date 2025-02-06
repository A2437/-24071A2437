import numpy as np

# Define two matrices
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Matrix Addition
add_result = A + B
print("Matrix Addition:\n", add_result)

# Matrix Subtraction
sub_result = A - B
print("\nMatrix Subtraction:\n", sub_result)

# Matrix Multiplication (Element-wise)
mul_elementwise = A * B
print("\nElement-wise Multiplication:\n", mul_elementwise)

# Matrix Multiplication (Dot Product)
mul_dot = np.dot(A, B)
print("\nMatrix Multiplication (Dot Product):\n", mul_dot)

# Transpose of a Matrix
transpose_A = np.transpose(A)
print("\nTranspose of Matrix A:\n", transpose_A)
