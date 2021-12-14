# 方法一
age = ""
while age != "quit":
    age = input("请输入您的年龄，我将告诉您需要支付的电影票的票价：")
    age = int(age)
    if age < 3:
        price = 0
    elif age > 12:
        price = 15
    else:
        price = 10
    print(f"您需要支付电影票{price}美元")


# # 方法二
# active = True
# while active:
#     age = input("请输入您的年龄，我将告诉您需要支付的电影票的票价：")
#     if age!="quit":
#         age = int(age)
#         if age < 3:
#             price = 0
#         elif age > 12:
#             price = 15
#         else:
#             price = 10
#         print(f"您需要支付电影票{price}美元")
#     else:
#         active = False


# # 方法三
# while True:
#     age = input("请输入您的年龄，我将告诉您需要支付的电影票的票价：")
#     if age!="quit":
#         age = int(age)
#         if age < 3:
#             price = 0
#         elif age > 12:
#             price = 15
#         else:
#             price = 10
#         print(f"您需要支付电影票{price}美元")
#     else:
#         break
