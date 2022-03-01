matrix_size=3

matrix_a =  [[3, 1, -4], 
            [2, -3, 1], 
            [5, -2, 0]]

matrix_b =  [[1, -2, -1],
            [0, 5, 4], 
            [-1, -2, 3]]

result = [[0] * matrix_size for r in range(matrix_size)]

for row in range(matrix_size):
    for col in range(matrix_size):
        for i in range(matrix_size):
            result[row][col]+=matrix_a[row][i] * matrix_b[i][col]

for row in range(matrix_size):
    print(matrix_a[row], matrix_b[row], result[row])
print()