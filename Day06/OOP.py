import math 
class calculator:
    def __init__(self,num_1,num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def addition(self):
        return self.num_1 + self.num_2
    
    def substraction(self):
        return self.num_1 - self.num_2

    def multiplication(self):
        return self.num_1 * self.num_2

    def divide(self):
        return self.num_1/self.num_2

    def square_root(self):
        return math.sqrt(self.num_1)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

sol = calculator(a, b)
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square_root")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",sol.addition())
    elif choice==2:
        print("Result: ",sol.substraction())
    elif choice==3:
        print("Result: ",sol.multiplication())
    elif choice==4:
        print("Result: ",round(sol.divide(),2))
    elif choice==5:
        print("Result: ",sol.square_root())
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
print()