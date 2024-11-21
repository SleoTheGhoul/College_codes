# To check if a no. is a buzz no.
# aka if a no. ends with 7 or Divisible by 7
# so 67, 77, 47, 42, 63, etc. are buzz no.s 
# 89, 31, 8, etc. are not buzz nos.

n=int(input("Enter a no. to see if its a buzz no. :"))
if(n % 10 == 7):
    print("Buzz no.")
elif(n % 7 == 0):
    print("Buzz no.")
else:
    print("Not a Buzz no.")

# Shorter method

# if(n % 10 == 7 or n % 7 == 0):
#     print("Buzz no.")
# else:
#     print("Not a Buzz no.")