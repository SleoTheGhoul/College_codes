
 # Program to allow the user to chose out of:- Automorphic no.,Armstrong no.,
 # Buzz no.,Perfect no.,Pronic no.,Happy no. and Emrip no.
 # And check if the no. inputed later is either the type of no. chosen
 
class WeirdNos:
    def b(self):  # To help print Automorphic no.
        n = int(input("Enter a number: \n"))  # To take input of a no.
        k = n  # To take a replacement of the original no.
        count = 0  # To help checking if it is a Automorphic no.
        while k > 0:  # To help print Automorphic no.
            k = k // 10
            count += 1
        k = (n * n) - n
        if n % 10 == 0:  # To help print Automorphic no.
            print(f"{n} is not an automorphic number")
        elif k % (10 * count) == 0:  # To help print Automorphic no.
            print(f"{n} is an automorphic number")
        else:  # To help print Automorphic no.
            print(f"{n} is not an automorphic number")

    def c(self):  # To help print Armstrong no.
        no = int(input("Enter a number: \n"))  # To take input of a no.
        k = no  # To take a replacement of the original no.
        sum = 0  # To help checking if it is a Armstrong no.
        while k > 0:  # To help print Armstrong no.
            dig = k % 10
            k = k // 10
            sum += dig ** 3
        if sum == no:  # To help print Armstrong no.
            print("It is an Armstrong number")
        else:  # To help print Armstrong no.
            print("It is not an Armstrong number")

    def d(self):  # To help print Buzz no.
        n = int(input("Enter a number:\n "))  # To take input of a no.
        if n % 10 == 7:  # To help print Buzz no.
            print(f"{n} is a buzz number.")
        elif n % 7 == 0:  # To help print Buzz no.
            print(f"{n} is a buzz number.")
        else:  # To help print Buzz no.
            print(f"{n} is not a buzz number.")

    def e(self):  # To help print Perfect no.
        n = int(input("Enter a number: \n"))  # To take input of a no.
        sum = 0  # To help checking if it is a Perfect no.
        for i in range(1, n):  # To help print Perfect no.
            if n % i == 0:  # To help print Perfect no.
                sum += i
        if sum == n:  # To help print Perfect no.
            print(f"{n} is a perfect number.")
        else:  # To help print Perfect no.
            print(f"{n} is not a perfect number.")

    def f(self):  # To help print Pronic no.
        x = int(input("Enter a number to find whether it's pronic or not: \n"))  # To take input of a no.
        for i in range(1, x + 1):  # To help print Pronic no.
            if x % i == 0:  # To help print Pronic no.
                if i * (i + 1) == x:  # To help print Pronic no.
                    print(f"{x} is a pronic number.")
                    return
        print(f"{x} is not a pronic number.")

    def g(self):  # To help print Happy no.
        n = int(input("Enter a number: \n"))  # To take input of a no.
        k = n  # To take a replacement of the original no.
        while True:  # To help print Happy no.
            sum = 0  # To help checking if it is a Happy no.
            while n > 0:  # To help print Happy no.
                dig = n % 10
                sum += dig * dig
                n //= 10
            n = sum
            if n == 1:  # To help print Happy no.
                print(f"{k} is a happy number")
                return
            if n == 4:  # To help print Happy no.
                print(f"{k} is not a happy number")
                return

    def h(self):  # To help print Emrip no.
        n = int(input("Enter a number to check if it is an emrip number or not:\n "))  # To take input of a no.
        temp = 0  # To store the reverse no.
        k = n  # To be a temporary no.
        while n > 0:  # To reverse the digit
            temp = temp * 10 + n % 10
            n //= 10
        count = 0  # To act as a counter
        for i in range(1, temp + 1):  # To check if it is prime no. or not
            if temp % i == 0:
                count += 1
        if count > 2:  # To help print the no.
            print(f"{k} is not an emrip number.")
        elif count == 2:
            print(f"{k} is an emrip number.")

    def i(self):  # To help print palindrome no.
        n = int(input("Enter a number to check whether it is a palindrome number: \n"))  # To store input of a no.
        rev = 0  # To store the reverse of a no.
        k = n  # To act as a temporary no.
        while k != 0:  # To reverse the digits
            digit = k % 10
            rev = rev * 10 + digit
            k //= 10
        if rev == n:  # To help print the no.
            print("It is a palindrome number.")
        else:
            print("It is not a palindrome number.")

if __name__ == "__main__":
    h = 0  # To check if the user wants to use the program again
    while True:  # To check if the user wants to use the program again or not
        print("What type of number do you want to check for")
        print("Automorphic number (=1), \n Armstrong number (=2),")
        print("Buzz number (=3), \n Perfect number (=4),")
        print("Pronic number (=5), \n Happy number (=6),")
        print("Emrip number (=7) or \n Palindrome number (=8).")
        a = int(input("Choose an option: "))  # To choose a case in the switch
        z = WeirdNos()  # Object created to call the functions
        if a == 1:
            z.b()
        elif a == 2:
            z.c()
        elif a == 3:
            z.d()
        elif a == 4:
            z.e()
        elif a == 5:
            z.f()
        elif a == 6:
            z.g()
        elif a == 7:
            z.h()
        elif a == 8:
            z.i()
        else:
            print("Why? Haven't you abided by the rules\n")
        
        h = int(input("Do you want to choose another weird number? If yes then press 1; Else press 2: \n"))  # To check if the user wants to use the program again
        if h != 1:
            break

