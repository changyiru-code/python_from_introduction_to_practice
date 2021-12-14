## 方法一
# while True:
#     pizza = input("请输入一系列披萨配料：")
#     if pizza != "quit":
#         print(f"我们会在pizza中添加{pizza}配料")
#     else:
#         break

# ## 方法二
# flag = True
# while flag:
#     pizza = input("请输入一系列披萨配料：")
#     if pizza != "quit":
#         print(f"我们会在pizza中添加{pizza}配料")
#     else:
#         flag = False


## 方法二
pizza = ""
while pizza != "quit":
    pizza = input("请输入一系列披萨配料：")
    print(f"我们会在pizza中添加{pizza}配料")
