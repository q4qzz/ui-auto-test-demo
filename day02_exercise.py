# -*- coding: utf-8 -*-
"""Day 2 练习：轮到你自己写。

【怎么做】
下面有 4 个 TODO，每个 TODO 上面都写了提示。
写完一个就保存，双击 run_day02.bat 看结果，慢慢来。
全部做完后，这个文件跑出来的每一行都应该是"对"的。
"""

print("=" * 55)
print("练习 1:列表")
print("=" * 55)

# 现在列表里只有 2 个商品
products = ["背包", "自行车灯"]
products.append("pen")
products.append("xiangpi")
products.append("book")

# TODO 1：再往列表里加 3 个商品（想加什么都行）
# 提示：products.append("商品名")
#       写 3 行，每行加一个


for p in products:
    print(" 商品:",p)   # TODO 2：把这行改成打印 "  商品: xxx"
    # 提示：print("  商品:", p)


print()
print("=" * 55)
print("练习 2:字典")
print("=" * 55)

user = {"username": "standard_user", "password": "secret_sauce"}
print(user["username"])

# TODO 3：把用户名打印出来
# 提示：print(user["username"])


print()
print("=" * 55)
print("练习 3:函数")
print("=" * 55)


def check_login(username, password):
    if username == "standard_user" and password == "secret_sauce":
        return"登录成功"
    else:
        return"登录失败"
    # TODO 4：补全这个函数
    #   如果 username 等于 "standard_user" 并且 password 等于 "secret_sauce"
    #       就返回 "登录成功"
    #   否则
    #       就返回 "登录失败"
    #
    # 提示：if username == "standard_user" and password == "secret_sauce":
    #           return "登录成功"
    #       else:
    #           return "登录失败"
    pass


print(check_login("standard_user", "secret_sauce"))   # 期望输出: 登录成功
print(check_login("standard_user", "wrong"))          # 期望输出: 登录失败

print()
print("如果上面两行还不是「登录成功 / 登录失败」，说明 TODO 4 还没写完。")
