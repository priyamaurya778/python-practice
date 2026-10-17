#count uppercase and lowercase separately
#s = input("Enter a word")
#upper = 0
#lower = 0
#for i in s:
#    if i.isupper():
#        upper += 1
#    if i.islower():
#        lower += 1
#print("Uppercase letters : ", upper)
#print("Lowercase letters : ", lower)


#remove vowels

#s = input("Enter a string: ")
#result = ""

#for ch in s:
#    if ch.lower() not in "aeiou":
#        result += ch
#print("String without vowels:", result)


#print duplicate characters
s = input("Enter a word : ")
res = ""
for i in s:
    if i not in res:
        res += i
    else: 
        print(i)