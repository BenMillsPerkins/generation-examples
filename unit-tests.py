def add_two_numbers(a, b):
    if type(a) == str or type(b) == str:
        return "Can't add non numbers"
    return a + b

def test_add_two_integers():
    #Assemble
    a = 19
    b = 8
    expected = 27

    #Act
    result = add_two_numbers(a, b)

    #Assert
    assert result == expected

test_add_two_integers()

def test_add_pos_neg():
    #Assemble
    a = 19
    b = -8
    expected = 11

    #Act
    result = add_two_numbers(a, b)

    #Assert
    assert result == expected

test_add_pos_neg()

def test_add_floats():
    #Assemble
    a = 2.3
    b = 2.4
    expected = 4.699999999999999

    #Act
    result = add_two_numbers(a, b)
    #Assert
    assert result == expected

test_add_floats()

def test_add_string_and_int():
    #Assemble
    a = "String"
    b = 8
    expected = "Can't add non numbers"
    #Act
    result = add_two_numbers(a, b)

    #Assert
    assert result == expected

test_add_string_and_int()


def test_add_strings():
    #Assemble
    a = "String"
    b = "Another string"
    expected = "Can't add non numbers"
    #Act
    result = add_two_numbers(a, b)

    #Assert
    assert result == expected

test_add_strings()