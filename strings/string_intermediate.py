#find longest word in a sentence
#s = input("Enter a sentence : ")
#words = s.split(" ") 
#res = ""
#count = 0
#for i in words:
#    if len(i) > count:
#        count = len(i)
#        res = i
#print("Longest word : ", res)


#Replace consecutive repeated characters with the character followed by its count
s = input("Enter a word : ")
c = 1
res = ""
sorted(s)
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        c += 1
    else:
        res += s[i - 1] + str(c)
        c = 1
if s:
    res += s[-1] + str(c)
print(res)
    