#CTI-110
#P4HW2 - BasicMath
#Sinclair Robinson
#06-22-2020

# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function subtracts two numbers
def multiply(x, y):
    return x - y


print("Menu.")
print("1.Add Numbers")
print("2.Multiply Numbers")
print("3.Subtract Numbers")
print("4.Exit")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3','4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '3':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '4':
            print('the program will terminate')
        break
    else:
        print("Invalid Input")

