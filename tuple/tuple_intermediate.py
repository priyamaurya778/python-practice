#Find the Second-Largest Element
#t = (10, 20, 30, 40, -1, 100, 60)
#max1 = float("-inf")
#max2 = float("-inf")
#for i in t:
#    if i > max1:
#        max2 = max1
#        max1 = i
#    elif i > max2 and i != max1:
#        max2 = i
#print("Second largest element : ", max2)


#Find the elements common to two tuples.
#t1 = (1, 2, 3, 4)
#t2 = (3, 4, 5, 6)
#newt = []
#for i in t1:
#    if i in t2:
#        newt.append(i)
#print("Common elements : ", tuple(newt))


#Find the index of a given element without using the index() method.
t = (1, 2, 3, 4, 5)
tar = int(input("Enter the element whose index you want to know! "))
c = 0
found = False
for i in t:
    if i == tar:
        print("Index", c)
        found = True
        break
    c += 1
if not found:
    print("Element not present in tuple")
