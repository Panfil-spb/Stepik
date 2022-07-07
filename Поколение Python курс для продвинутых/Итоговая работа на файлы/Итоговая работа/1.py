file_name = input()

with open(file_name) as file:
    print(len(file.readlines()))