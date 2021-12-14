with open("pi_digits.txt") as file_object:
    contents0 = file_object.readlines()
    print(contents0)
for i in contents0:
    print(i.rstrip())