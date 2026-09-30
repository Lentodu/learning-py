#type data
name = "Yu" #this is string variable type

age = 20 #this is integer variable type

saldo = 21.99 #this is float variable type

isStudent = True #this is boolean variable type, using True or False // using capitalize first letter

print(f"Hi, my name is: {name}, im {age} years old, and i only have {saldo} on my walllet because I'm Student\n")

#input
userName = input("Enter your username: ") #this is input string variable type, using input() function to get user input
print(f"Your username is: {userName} \n") #call the input string to print

#other input tyoe
intNumber = int(input("Enter your number: ")) #this is input int variable type
floatNumber = float(input("Enter your decimal number (01.00): ")) #this is input float variable type
print(f"Your int number is: {intNumber}, and your decimal number is: {floatNumber}\n")

#test
x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))

def add(a, b):
    return a+b

result = add(x, y)
print("The result for the sum is: ", result)

#scope variable
globalVariable = "This is global variable" #outside function, can be accessed anywhere

def funcLocalVariable():
    localVariable = "This is local variable" #inside function, can only be accessed inside the function
    print(localVariable)

print(globalVariable)
funcLocalVariable()