#defining a function that returs maximum of any three numbers

def maximum(x1,x2,x3):
    return max(x1,x2,x3)

x1 = int(input("Enter the first number:"))
x2 = int(input("Enter the second number:"))
x3 = int(input("Enter the third number:"))

max_num = maximum(x1,x2,x3)

print("The maximum number is:" + str (max_num))