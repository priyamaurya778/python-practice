#Access Dictionary Values, add a key, replace a key and delete a key
#d = {"name": "shikha", "age": 22, "in_clg": False}
#print(d["in_clg"])
#print(d.get("name"))
#print(d.get("city", "Not found"))
#for key, value in d.items():
#    print(key)

#d["email"] = "shikha@gmail.com"
#print(d)

#d["name"] = "piya"
#print(d)

#del d["age"]
#print(d)


#Count Dictionary Items
#d = {"a": 1, "b": 2, "c": 3}
#count = 0
#for key in d:
#    count += 1
#print("Total dictionary items : ", count)


#Calculate the Sum of Values
d = {"maths": 80, "phy": 70, "chem": 89}
sum = 0
for value in d.values():
    sum +=  value
print("Sum of values : ", sum)