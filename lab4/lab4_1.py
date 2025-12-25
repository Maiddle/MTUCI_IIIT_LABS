import math
import datetime
def square_root(x):
    """Returns the square root of x."""
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(x)
number = float(input("Enter a number to compute its square root: "))
try:
    result = square_root(number)
    print(f"The square root of {number} is {result}")
except ValueError as e:
    print(e)

print("\nCurrent date and time:")
now = datetime.datetime.now()   
print(now.strftime("%Y-%m-%d %H:%M:%S"))
