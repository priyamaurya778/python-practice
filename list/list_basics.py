#sum of even numbers in a list
#n = int(input("Enter the number of elements : "))
#l = []
#for i in range(n):
#    num = int(input("Enter a number : "))
#    l.append(num)
#c = 0
#for i in l:
#    if i % 2 == 0:
#        c += i
#print(c)


#Count Numbers Greater Than a Value
n = int(input("Enter the number of elements in the list : "))
l = []
for i in range(n):
    num = int(input("Enter number : "))
    l.append(num)
num = int(input("Enter number to be compared : "))
c = 0
for i in l:
    if i > num:
        c += 1
print("Count : ", c)