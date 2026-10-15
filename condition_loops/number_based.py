#Fibonacci series - 0 1 1 2 3 5 8
limit = int(input("Enter limit for fibonacci series "))
a = 0
b = 1
for i in range(limit):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


#Palindrome number