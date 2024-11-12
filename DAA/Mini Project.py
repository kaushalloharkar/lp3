import numpy as np
import threading
import time
import random

# Standard matrix multiplication
def matrix_multiply(A, B):
    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape
    
    if cols_A != rows_B:
        raise ValueError("Incompatible matrices for multiplication.")
    
    C = np.zeros((rows_A, cols_B))
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i, j] += A[i, k] * B[k, j]
    
    return C

# Multithreaded matrix multiplication (One Thread per Row)
def matrix_multiply_row(A, B, C, row):
    cols_B = B.shape[1]
    for j in range(cols_B):
        C[row, j] = sum(A[row, k] * B[k, j] for k in range(A.shape[1]))

def multithreaded_matrix_multiply_row(A, B):
    rows_A = A.shape[0]
    C = np.zeros((rows_A, B.shape[1]))
    threads = []

    for i in range(rows_A):
        thread = threading.Thread(target=matrix_multiply_row, args=(A, B, C, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return C

# Multithreaded matrix multiplication (One Thread per Cell)
def matrix_multiply_cell(A, B, C, row, col):
    C[row, col] = sum(A[row, k] * B[k, col] for k in range(A.shape[1]))

def multithreaded_matrix_multiply_cell(A, B):
    rows_A, cols_B = A.shape[0], B.shape[1]
    C = np.zeros((rows_A, cols_B))
    threads = []

    for i in range(rows_A):
        for j in range(cols_B):
            thread = threading.Thread(target=matrix_multiply_cell, args=(A, B, C, i, j))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    return C

# Function to measure execution time
def measure_time(func, *args):
    start = time.time()  # Record the start time
    result = func(*args)  # Execute the function
    end = time.time()  # Record the end time
    return end - start, result  # Return the elapsed time and the result

# Main function for testing
if __name__ == "__main__":
    # Generate random matrices for testing
    size = 5  # Adjust size for demonstration purposes
    A = np.random.randint(0, 10, (size, size))
    B = np.random.randint(0, 10, (size, size))

    # Print the generated matrices
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)

    # Measure time for standard matrix multiplication
    time_standard, C_standard = measure_time(matrix_multiply, A, B)
    print(f"\nStandard Matrix Multiply Time: {time_standard:.6f} seconds")
    print("Resultant Matrix (Standard):")
    print(C_standard)

    # Measure time for multithreaded (one thread per row) matrix multiplication
    time_thread_row, C_thread_row = measure_time(multithreaded_matrix_multiply_row, A, B)
    print(f"\nMultithreaded (One Thread per Row) Time: {time_thread_row:.6f} seconds")
    print("Resultant Matrix (Thread per Row):")
    print(C_thread_row)

    # Measure time for multithreaded (one thread per cell) matrix multiplication
    time_thread_cell, C_thread_cell = measure_time(multithreaded_matrix_multiply_cell, A, B)
    print(f"\nMultithreaded (One Thread per Cell) Time: {time_thread_cell:.6f} seconds")
    print("Resultant Matrix (Thread per Cell):")
    print(C_thread_cell)
