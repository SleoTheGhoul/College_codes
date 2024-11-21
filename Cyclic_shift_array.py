import numpy as np

class CyclicShiftArray:
    def __init__(self):
        self.m = 0  # To store the no. of rows
        self.n = 0  # To store the no. of columns
        self.arr = None  # To store the elements

    def input_array(self):
        # To help input the elements
        print("Enter no. of rows and columns")
        self.m = int(input())
        self.n = int(input())
        self.arr = np.zeros((self.m, self.n), dtype=int)
        print("Enter elements")
        for i in range(self.m):
            # To input the elements
            for j in range(self.n):
                self.arr[i][j] = int(input())

    def shifting(self, x):
        # To help shifting the array rows
        if x > 0:
            # To help in recursion
            for i in range(self.m):
                # To cycle the elements
                self.arr[0], self.arr[i] = self.arr[i].copy(), self.arr[0].copy()
            self.shifting(x - 1)
        else:
            self.display()

    def display(self):
        # To display the array after being sorted
        for row in self.arr:
            # To print the array
            print(' '.join(map(str, row)))

if __name__ == "__main__":
    o = CyclicShiftArray()
    o.input_array()
    print("How many times would you like it to cycle")
    x = int(input())  # To store the amount of turns
    o.shifting(x)
    print()