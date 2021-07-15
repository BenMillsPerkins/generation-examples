file = open("file-open-example.txt", "r")
lines = file.readlines()
print(lines)
for line in lines:
    print(line)