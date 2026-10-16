#Fibonacci series - 0 1 1 2 3 5 8
#limit = int(input("Enter limit for fibonacci series "))
#a = 0
#b = 1
#for i in range(limit):
#    print(a, end=" ")
#    c = a + b
#    a = b
#    b = c


#Palindrome number
num = int(input("Enter a number : "))
rev = 0
dup = num
while num > 0:
    d = num % 10
    num = num // 10
    rev = rev * 10 + d 
if dup == rev:
    print("Palindrome")
else: 
    print("Not palindrome")