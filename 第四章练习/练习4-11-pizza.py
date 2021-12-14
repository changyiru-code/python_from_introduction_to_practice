pizzas = ['fruit', 'vegetable', 'meat']
for pizza in pizzas:
    print(f"I like {pizza} pizza")
print(f"I like {pizzas[0]} pizza, {pizzas[1]} pizza, {pizzas[2]} pizza, I really love pizza!")
for pizza in pizzas:
    print(pizza + ' ', end='')

friend_pizzas = pizzas[:]
pizzas.append('banana')
friend_pizzas.append('apple')
print('my favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("my friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
