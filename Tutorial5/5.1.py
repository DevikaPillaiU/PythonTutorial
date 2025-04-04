import numpy as np

def matrix_operations(matrix1, matrix2):
    try:
        array1 = np.array(matrix1)
        array2 = np.array(matrix2)
        
        if array1.shape != array2.shape:
            raise ValueError("Dimensions must be the same")
        
        sum_matrix = array1 + array2
        transposed_matrix = sum_matrix.T
        
        return sum_matrix, transposed_matrix
    except Exception as error:
        return str(error)

data_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

sum_result, transpose_result = matrix_operations(data_a, data_b)
print("Matrix Sum:")
print(sum_result)
print("\nTransposed Sum:")
print(transpose_result)
