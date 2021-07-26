class Test:
    def __init__(self, integer):
        self.integer = integer

    def get_integer(self):
        return (self.integer)

    def double_int(self):
        self.integer = self.integer * 2    


def test_Test():
    obj = Test(5)
    obj.double_int()
    assert obj.integer == 10

test_Test()