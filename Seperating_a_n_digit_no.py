# To seperate a n digit no.
# Printing all digits of a no.
# Input: 189
# Output:
#         1
#         8
#         9

n = int(input("Enter a no.: "))
k = n
while(k != 0):
    dig=k%10
    print(dig)
    k= int(k / 10)
