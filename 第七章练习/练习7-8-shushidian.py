sandwich_orders = ["onion", "banana", "apple"]
finished_sandwich = []
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"I made your {sandwich_order} sandwich.")
    finished_sandwich.append(sandwich_order)
for sandwich in finished_sandwich:
    print(sandwich)
