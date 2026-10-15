#conditional statements - if, else, elif, nested if 

#Take marks out of 100 and print the grade

marks = int(input("Enter marks : "))
if marks > 90:
    print("A")
elif marks >= 80 and marks < 90:
    print("B") 
elif marks >= 70 and marks < 80:
    print("C")
elif marks >= 40 and marks < 70:
    print("D")
else:
    print("Fail")


#Triangle validity
a = int(input("Enter first side : "))
b = int(input("Enter first side : "))
c = int(input("Enter first side : "))

if a > 0 and b > 0 and c > 0:
    if (a + b) > c or (b + c) > a or (a + c) > b:
        print("Valid triangle")
    else:
        print("Not a valid triangle")
else: 
    print("Not valid")