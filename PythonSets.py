my_set = {"Chalk", "Duster", "Board"}
print(my_set)

for x in my_set:
    print(x)

my_set.add("Pen")
print(my_set)

my_set.update(["Pencil","Eraser"])
print(my_set)

print(len(my_set))

A = {'A','B',1,2,3}
B = {'B','C',3,4,5}

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)