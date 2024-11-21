# Program to check if a no. is odd or even.
# If even, then the user adds 2 more nos.
#   ^-Then if the both of the nos. are odd they-^ 
#   ^-get added and squarerooted else if even they-^
#   ^-get multiplied and squarerooted.-^
# Else if odd, then the user adds 2 more nos.
#   ^-Then if the both of the nos. are odd they-^
#   ^-get subtracted and squared else if even they-^ 
#   ^-get diveded and squared.-^
  
import math

class OddEven:
    def __init__(self):
        self.f = 0.0  # To store the +, *, - or / sum
        self.g = 0.0  # To store the squarerooted or squared no.

    def even(self):
        print("You chose an even no. so now, add two more nos.")
        print("(They should both be the same, odd or even)")
        print("Enter the 1st no.\n")
        a = float(input())  # To store a no.
        print("Enter the 2nd no.(can not be 0)\n")
        b = int(input())  # To store a no.
        print("Now, if both of the nos. are odd they get added and squarerooted else if even they get multiplied and squarerooted")
        
        if a % 2 != 0 or b % 2 != 0:
            # Both of the nos. are odd they get added and squarerooted
            print("You put in odd nos.")
            self.f = a + b
            self.g = math.sqrt(self.f)
            print(f"Your nos. which got added and squarerooted gives the result of {self.g}")
        elif a % 2 == 0 or b % 2 == 0:
            # Both of the nos. are even they get multiplied and squarerooted
            print("You put in even nos.")
            self.f = a * b
            self.g = math.sqrt(self.f)
            print(f"Your nos. which got multiplied and squarerooted gives the result of {self.g}")

    def odd(self):
        print("You chose an odd no. so now, add two more nos.")
        print("(They should both be the same, odd or even)")
        print("Enter the 1st no.\n")
        a = float(input())  # To store a no.
        print("Enter the 2nd no.(can not be 0)\n")
        b = int(input())  # To store a no.
        print("Now, if both of the nos. are odd they get subtracted and squared else if even they get divided and squared.")
        
        if a % 2 != 0 or b % 2 != 0:
            # Both of the nos. are odd they get subtracted and squared
            print("You put in odd nos.")
            self.f = a - b
            self.g = math.pow(self.f, 2)
            print(f"Your nos. which got subtracted and squared gives the result of {self.g}")
        elif a % 2 == 0 or b % 2 == 0:
            # Both of the nos. are even they get divided and squared.
            print("You put in even nos.")
            self.f = a / b
            self.g = math.pow(self.f, 2)
            print(f"Your nos. which got divided and squared gives the result of {self.g}")

def main():
    print("Enter a no.\n")
    e = int(input())  # To store a no.
    print("Now, to check if a no. is odd or even.")
    h = OddEven()  # To call the above functions
    if e % 2 != 0:  # To check if a no. is odd or even.
        h.odd()
    elif e % 2 == 0:  # To check if a no. is odd or even.
        h.even()

if __name__ == "__main__":
    main()

