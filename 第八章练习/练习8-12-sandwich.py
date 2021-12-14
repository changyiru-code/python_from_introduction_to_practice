def show_sandwich(*ingredients):
    print(f"\nmaking your sandwich with the follwing ingredients: ")
    for ingredient in ingredients:
        print("\t"+ingredient)


show_sandwich("banana")
show_sandwich("banana", "onion")
show_sandwich("banana", "onion", "apple")
