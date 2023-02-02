with open("/Users/user/Desktop/my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)

with open("../../../Desktop/my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)

