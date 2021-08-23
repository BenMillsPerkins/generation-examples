def multiply_by_two(integer):
    return integer*2

def add_one_to_a_number(integer):
    return integer+1

def capitalise_string(arbitrary_string):
    return arbitrary_string.upper()

def multiply_by_two_and_add_one(integer, add_one_to_a_number, multiply_by_two):
    integer_two = multiply_by_two(integer)
    integer_three = add_one_to_a_number(integer_two)
    return integer_three

# print(multiply_by_two(6))
# print(add_one_to_a_number(12))
print(multiply_by_two_and_add_one(10, add_one_to_a_number, multiply_by_two))
# print(capitalise_string("blahlbaduiwihuwaduih"))
# print(multiply_by_two("blahlbaduiwihuwaduih"))