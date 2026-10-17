#largest digit in an integer
#num = int(input("Enter a number"))
#min = 0
#while num > 0:
#    d = num % 10
#    num = num // 10
#    if d > min:
#        min = d
#print(min)


#print all divisors
#num = int(input("Enter a number"))
#for i in range(1, num + 1):
#    if num % i == 0:
#        print(i)


#armstrong number
n = int(input("Enter a number : "))
dup = n
sum = 0
while n > 0:
    d = n % 10
    n = n // 10
    sum =  sum + d * d *d
if sum == dup:
    print("Armstrong")
else:
    print("Not armstrong")