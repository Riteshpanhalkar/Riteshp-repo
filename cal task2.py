def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

print("Select operation:")
print("+. Addition")
print("-. Subtraction")
print("*. Multiply")
print("/. Divide")

while True:
    choice = input("Enter choice (+,-,*,/): ")

    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print("Result:", addition(num1, num2))
        elif choice == '-':
            print("Result:", subtraction(num1, num2))
        elif choice == '*':
            print("Result:", multiply(num1, num2))
        elif choice == '/':
            print("Result:", divide(num1, num2))
        break
    else:
        print("Invalid input")
