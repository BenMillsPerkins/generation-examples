from random import randint

# def get_random_number():
#     return random.randint(1, 10)

def add_number_with_random_number(a, random_number_func):
    return a + random_number_func()

def test_add_number_with_random_number():
    a = 5
    expected = 10

    def mock_random_num():
        return 5

    result = add_number_with_random_number(a, mock_random_num)
    print(result)
    assert result == expected

# test_add_number_with_random_number()
# print(add_number_with_random_number(5, get_random_number))

def add_two_random_numbers(random_num_func):
    return random_num_func() + random_num_func()

def test_add_two_random_numbers():
    def mock_random_num():
        return 10
    expected = 20

    result = add_two_random_numbers(mock_random_num)

    assert expected == result

# test_add_two_random_numbers()
# print(add_two_random_numbers(get_random_number))


def get_random_number(randint_override):
    return randint_override(1, 10)


def test_get_random_number():
    def mock_randint(a, b):
        return 7
    expected = 7

    result = get_random_number(mock_randint)

    assert expected == result

test_get_random_number()