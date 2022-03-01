import time
from random import Random

matrix_size=200
random=Random()

matrix_a =  [[0] * matrix_size for a in range(matrix_size)]
matrix_b =  [[0] * matrix_size for b in range(matrix_size)]
result = [[0] * matrix_size for r in range(matrix_size)]

def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            for i in range(matrix_size):
                matrix[row][col]=random.randint(-5, 5)

start=time.time()
for t in range(10):
    generate_random_matrix(matrix_a)
    generate_random_matrix(matrix_b)
    result = [[0] * matrix_size for r in range(matrix_size)]
    for row in range(matrix_size):
        for col in range(matrix_size):
            for i in range(matrix_size):
                result[row][col]+=matrix_a[row][i] * matrix_b[i][col]
end=time.time()
print("Done! Time taken: ", end-start)

# Execution time was 81 seconds.