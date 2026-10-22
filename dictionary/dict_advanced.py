#Count how many times each character appears in a string using a dictionary.
#s = input("Enter a word : ")
#d = {}
#for ch in s:
#    if ch in d:
#        d[ch] += 1
#    elif ch == ' ':
#        continue
#    else:
#        d[ch] = 1
#print(d)        


#Count Word Frequency
#s = input("Enter a sentence : ")
#d = {}
#words = s.split(" ")
#for word in words:
#    if word in d:
#        d[word] += 1
#    else:
#        d[word] = 1
#print(d)


#Find the keys that exist in both dictionaries.
#d1 = {"a": 1, "b": 2, "c": 3}
#d2 = {"b": 0, "c": 1, "d": 2, "e": 3}
#s = set()
#for i in d1:
#    if i in d2:
#        s.add(i)
#print(s)


#Invert a dictionary
d = {"a": 1, "b": 2, "c": 3}
inv = {}
for key, value in d.items():
    inv[value] = key

print(inv)