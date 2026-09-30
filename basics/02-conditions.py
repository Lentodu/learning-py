#ternary operation in python
num = 6 

ternaryResult = "Yes" if num == 6 else "No" #using if and else in one single line
print(ternaryResult + "\n")

#identify is and is not
x = [3,4,5]
y = [3,4,5]
z = [1,2,3]

print("x = ", x)
print("y = ", y)
print("z = ", z)

print(x == y, "//this is output for x == y") #output true, because the values are same
print(x == z, "//this is output for x == z\n") #output false, because the values are different

print(x is y, "//this is output for x is y") #output false, because different objects, will be true if y=x instead make new object like y = []
print(x is not y, "//this is output for x is not y\n") #output true, because different objects

#membership operator (in & not in)
goat = ["messi", "ronaldo", "lebron", "gw"]

print(goat)
print("messi" in goat, "//this is output for \"messi\" in goat") #output true, because messi is in the list
print("gw" not in goat, "//this is output for \"gw\" not in goat") #output false, because gw is in the list
print("mbappe" not in goat, "//this is output for \"mbappe\" not in goat\n") #output true, because mbappe is not in the list