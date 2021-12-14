sandwich_orders = ["pastrami", "onion", "pastrami", "banana", "apple", "pastrami"]
finished_sandwich = []
print("不好意思，店里的五香熏牛肉(pastrami)卖完了")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
finished_sandwich = sandwich_orders
print(finished_sandwich)
