#Find elements that appear in the first list but not in the second
#l1 = [1, 2, 3, 4, 9]
#l2 = [3, 4, 5, 6]
#newL = []
#for i in l1:
#    if i not in l2:
#        newL.append(i)
#print(newL)


#swap first and last element of the list
#l = [10 , 20, 30, 40]
#temp = 0
#temp = l[0]
#l[0] = l[-1]
#l[-1] = temp
#print(l)


#Move all zeros to the end while preserving the order of the other elements
#l = [0, 1, 0, 3, 12]
#newL = []
#for i in l:
#    if i == 0:
#        continue
#    else:
#        newL.append(i)
#for i in range(len(l) - len(newL)):
#    newL.append(0)
#print(newL)