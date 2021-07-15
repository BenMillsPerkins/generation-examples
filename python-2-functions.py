# 1

# def add_together(a, b):
#     return a+b

# print(add_together(5,8))

# 2

# def add_together(a, b, *args):
#     result = a + b
#     for num in args:
#         result+= num
#     return result

# print(add_together(3, 6, 8))

# 3 "key: {key}, value: {value}"

def print_dict(**kwargs):
    for key, value in kwargs.items():
        print(f'key: {key}, value: {value}')


print_dict(key1="value1", key2="value2")