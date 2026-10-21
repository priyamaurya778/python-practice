#Find all elements that appear in either set, but not in both.
#s1 = {1, 2, 3, 4}
#s2 = {3, 4, 5, 6}
#new = set()
#for i in s1:
#    if i not in s2:
#        new.add(i)
#for i in s2:
#    if i not in s1:
#        new.add(i)
#print(new)


#Check whether all elements of one set are present in another set.
s1 = {1, 2, 5}
s2 = {1, 2, 3, 4}
print(s1.issubset(s2))