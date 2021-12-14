# while True:
#     age = input("请输入您的年龄，我将告诉您需要支付的电影票的票价：")
#     age = int(age)
#     if age < 3:
#         print("您不需要支付电影票费用，免费")
#     elif age > 12:
#         print("您需要支付电影票15美元")
#     else:
#         print("您需要支付电影票10美元")

while True:
    age = input("请输入您的年龄，我将告诉您需要支付的电影票的票价：")
    age = int(age)
    if age < 3:
        price = 0
    elif age > 12:
        price = 15
    else:
        price = 10
    print(f"您需要支付电影票{price}美元")
