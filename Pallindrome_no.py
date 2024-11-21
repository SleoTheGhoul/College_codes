# To see if the no. is a pallindrome
# aka the no. is equal to itself if reversed
# so 11, 121, 78987, 33, 989. etc. are palindromes
# 478, 231, 05, 78, 45, etc. are not palindromes

n = int(input("Enter a no. to Reverse it: "))
k = n
rev = 0
while(k != 0):
    dig = k % 10
    rev = (rev * 10) + dig
    k = int( k / 10 )
if(rev == n):
    print("No. is a pallindrome")
else:
    print("No. is not a pallindrome")