# def add(a, b):
#     print(f"Adding {a} and {b}")
#     return a+b

def add(*nums):
    value = 0
    for num in nums:
        value += num
    return value

# def divide(a, b):
#     print(f"Dividing {a} by {b}")
#     return a/b

def divide(*nums):
    value = nums[0]
    # for n in range(len(nums)):
    #     if n != 0:
    #         value = value/nums[n]
    for num in nums[1:]:
        value = value/num
    return value

def area_of_circle(radius):
    print(f"Calculating area of a circle of radius {radius}")
    return radius*radius*3.14

def calculator():
    print("Welcome to our brilliant calculator")
    print("Enter (1) to add, (2) to divide, (3) to calc area of circle")
    choice = input()
    if choice == "1":
        num1 = int(input("Please enter your first number: "))
        num2 = int(input("Please enter your second number: "))
        print(add(num1, num2))
    if choice == "2":
        num1 = int(input("Please enter your first number: "))
        num2 = int(input("Please enter your second number: "))
        print(divide(num1, num2))
    if choice == "3":
        rad = int(input("Please enter the radius of your circle: "))
        print(area_of_circle(rad))

calculator()