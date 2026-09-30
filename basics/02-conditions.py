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

#if condition
isStudent = False
student = isStudent if isStudent else "Not a student"
print("Student is False = " + student + "\n")

Hp = 100
passiveSkill = Hp < 30
print("Hp = ", Hp)
if passiveSkill:
    print("Passive skill is active\n")
elif Hp < 50:
    print("Passive skill is almost active, need atleast <30 Hp\n")
else:
    print("Passive skill is not active\n") 
    

a = 1
b = 2
print("a = ", a)
print("b = ", b)
if a > b and a>=b:
    print("a is greater than b\n")
else:
    print("a is not greater than b\n")
    