# Date 27-sep-2022
# Programmer : MD.Najeeb Uddin

# Function Definations 
def add(P,Q):
    return P + Q
def subtract(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q
def divide(P,Q):
    return P/Q

print("Please selcet the operation.")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")
# Taking Inputs
Choice = input("Please enter choice(a/b/c/d):")

num_1 = int(input("Please enter the first number :c"))
num_2 = int(input("Please enter the second number :"))
# Comparing the Choice 
if Choice == 'a':
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif Choice == 'b':
    print(num_1,"-",num_2,"=",subtract(num_1,num_2))
elif Choice == 'c':
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))
elif Choice == 'd':
    print(num_1,"/",num_2,"=",divide(num_1,num_2))
else:
    print("Invalid Input")