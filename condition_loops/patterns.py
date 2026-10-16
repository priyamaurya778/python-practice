#*
#**
#***
#****
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

#1
#12
#123
#1234
for i in range(1, 5):
    for j in range(i):
        print(j+1, end="")
    print()

#   *
#  ***
# *****
#*******
for i in range(1, 5):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()