number = input("Please input a number, let mo tell you if it is 10's integer multiple: ")
number = int(number)
if number%10 == 0:
    print(f"{number} is 10's integer multiple")
else:
    print(f"{number} is not 10's integer multiple")
