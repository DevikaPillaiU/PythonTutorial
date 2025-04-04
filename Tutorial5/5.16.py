import numpy as np

mat1 = np.random.randint(0, 21, (3, 3))
mat2 = np.random.randint(0, 21, (3, 3))

mat_sum = mat1 + mat2

mat_mul = np.dot(mat1, mat2)

mat_trans = mat_mul.T

print("Matrix 1:\n", mat1)
print("\nMatrix 2:\n", mat2)
print("\nMatrix Addition (Matrix 1 + Matrix 2):\n", mat_sum)
print("\nMatrix Multiplication (Matrix 1 * Matrix 2):\n", mat_mul)
print("\nTransposed Product Matrix:\n", mat_trans)
