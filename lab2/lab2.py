# 1 задание:
def greet(name):
    return f"wsup, {name}!"
name = input("enter name: ")
print(greet(name))

# 2 задание:
def square(number: int) -> int:
    return number ** 2
number = int(input("enter number: "))
print("square of number:", square(number))

# 3 задание:
def max_of_two(x,y):
    if x > y:
        return x
    else:
        return y
number1 = int(input("enter first num: "))
number2 = int(input("enter second num: "))
result = max_of_two(number1, number2)
print("biggest num: ", result)


# 4 задание:
def describe_person(name:str, age: int=30)-> None:
    return f"Мmy name is {name}, im {age} yo"

username = input("enter name: ") or name
user_age = input("enter age: ")
if user_age:
    print(describe_person(username, user_age))
else:
    print(describe_person(username))


    print("name:", username)
    print("age:", user_age)


# 5 задание:
def prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
number = int(input("enter num: "))
if prime(number):
    print("number is simple")
else:
    print("number is not simple")