my_dict = {
    "class" : "Animal",
    "name"  : "Tiger",
    "age"   : 10
}

print(my_dict)
print(my_dict["class"])
print(my_dict.get("name"))

for x in my_dict:
    print(x,my_dict[x])