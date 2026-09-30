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
print(x is not y, "//this is output for x is not y") #output true, because different objects

