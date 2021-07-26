a = {"test": "blah"}
b = []
b.append(a)
# b == [a]
print(b)
a["test"] = "different blah"
print(b)