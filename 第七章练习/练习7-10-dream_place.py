results = {}
while True:
    name = input("\nWhat is your name?")
    dreamed_place = input("If you could visit one place in the world, where would you like go?")
    results[name] = dreamed_place
    repeat = input("Would you like to let another person respond?(yes or no)")
    if repeat == "no":
        break
for name, place in results.items():
    print(f"{name} would like to travel to {place}.")