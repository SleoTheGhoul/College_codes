import numpy as np

# Program to find the sum of all the rows in the matrix and the sum of both
# right and left diagonal

# Input matrix dimensions
a = int(input("Enter the number of rows: "))
b = int(input("Enter the number of columns: "))

# Input matrix elements
print("Now enter the elements row by row")
arr = np.array([input().split() for _ in range(a)], dtype=int)

# Print the matrix
print("The matrix is:")
print(arr)

# Calculate and print sum of rows
print("Sum of the rows are:")
for i, row_sum in enumerate(np.sum(arr, axis=1), 1):
    print(f"Row no. {i} is {row_sum}")

# Calculate and print sum of diagonals
print("The sums of the right and left diagonal are:")
left_diag_sum = np.trace(arr)
right_diag_sum = np.trace(np.fliplr(arr))

print(f"The sum of the right diagonal is {right_diag_sum}")
print(f"The sum of the left diagonal is {left_diag_sum}")

