import mymath
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
operation = input("choose operation - add(+), subtract(-), multiply(*), divide(/): ").strip()
try:
    if operation == '+':
        result = mymath.add(num1, num2)
    elif operation == '-':
        result = mymath.subtract(num1, num2)
    elif operation == '*':
        result = mymath.multiply(num1, num2)
    elif operation == '/':
        result = mymath.divide(num1, num2)
    else:
        print("invalid operation")
        exit()
    print(f"the result of {num1} {operation} {num2} is: {result}")
except ValueError as e:
    print(e)

