my_list = ["London", "NewYork", "Bangalore", "Chennai"]

print(my_list[2])

my_list[2] = "NewDelhi"

print(my_list)

my_list.append("Mumbai")

print(my_list)

for city in my_list:
    print(city)

print(len(my_list))
my_list.reverse()
print(my_list)

my_list1 = ["Apple", [1,2,3], ['a','b','c']]
print(my_list1[2][1])