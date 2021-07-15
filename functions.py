def add_numbers(a, b):
    print("a:", a)
    print("b:", b)
    return a + b

apple = 5
banana = 10

print(add_numbers(banana, 10))

# def get_name():
#     return 'Alice'

# # name = get_name()
# # print(name)

# name = get_name()

# print(get_name)

# def add_numbers(a, b, c):
#     return a + b + c

# result = add_numbers(1, 2)
# print(result)

# print("a", "b", "c", "d")

# def people_function(*people):
#     for person in people:
#         print(person)

# people_function("Alice", "Bob", "Charlie")

# def people_function():
#     people = ["Alice", "Bob", "Charlie"]
#     for person in people:
#         print(person)

# # people_function(["Alice", "Bob", "Charlie"])

# # people_list = ["Alice", "Bob", "Charlie"]

# # people_function(people_list)

# people_function()

# def concatenate(**kwargs):
#     print(kwargs)
#     # return result

# print(concatenate(first="Real", second="Python", c="Is", d="Great", e="!"))

# def connect_to_db(**kwargs):
#     if kwargs.get('username'):
#         user = kwargs.get('username')
#     else:
#         user = 'default'
#     print(user)

# connect_to_db(username='Ben')

# def concatenate(**kwargs):
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     for arg in kwargs.values():
#         result = result + arg
#     print (result)

# concatenate(a="Real", b="Python", c="Is", d="Great", e="!")

# def my_function(a, *args, **kwargs):
#     print("Hello")

# my_function("a", "args", kwargs="b")

def add_numbers(*nums):
    value = 0
    for num in nums:
        print(num)
        value += num
    return value
    # return a + b + c + d

# print(add_numbers(1, 2, 3, 4))
# print(add_numbers(1, 2))
# print(add_numbers(1, 2, 3, 4, 5, 6, 7))

# def concatenate(**kwargs):
#     for arg in kwargs.keys():
#         print(arg)

# concatenate(french="fries", arbitrary=2)

def multiply(a, b, **options):
    result = a*b
    if options['print'] == True:
        print(result)
    return(result)


multiply(10, 2, print=True)
