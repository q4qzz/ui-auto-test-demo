# -*- coding: utf-8 -*-
"""Day 2 演示：列表、字典、函数。

【怎么看这个文件】
先双击 run_day02.bat 看它跑出什么结果，
再回过头来一行一行看代码。看不懂没关系，先建立感觉。
"""

print("=" * 55)
print("第 1 部分：列表 list —— 用来装一排东西")
print("=" * 55)

# 列表就是"一排格子"，每个格子里放一样东西，用 [] 包起来
products = ["背包", "自行车灯", "T恤", "保温杯"]
print("商品列表:", products)
print("一共有", len(products), "件商品")

# 遍历：把列表里的东西一个一个拿出来
for p in products:
    print("  商品:", p)

print()
print("=" * 55)
print("第 2 部分：字典 dict —— 用来装一条完整的信息")
print("=" * 55)

# 字典是"键值对"，用 {} 包起来，格式是  名字: 内容
user = {
    "username": "standard_user",
    "password": "secret_sauce",
    "expected": "登录成功",
}
print("用户名:", user["username"])
print("密码:", user["password"])
print("期望结果:", user["expected"])

print()
print("=" * 55)
print("第 3 部分：列表里装字典 —— 这就是「测试数据」")
print("=" * 55)

# 一条用例 = 一个字典；一堆用例 = 一个列表
# 这个写法你要记住，后面整个项目都是这么组织测试数据的
test_cases = [
    {"username": "standard_user",   "password": "secret_sauce", "expected": "进入商品页"},
    {"username": "locked_out_user", "password": "secret_sauce", "expected": "提示账号被锁定"},
    {"username": "",                "password": "secret_sauce", "expected": "提示用户名必填"},
    {"username": "standard_user",   "password": "",             "expected": "提示密码必填"},
    {"username": "standard_user",   "password": "wrong_pass",   "expected": "提示用户名或密码错误"},
]

for i, case in enumerate(test_cases, start=1):
    u = case["username"] or "(空)"
    p = case["password"] or "(空)"
    print(f"  用例{i}: {u} / {p}   ->   期望: {case['expected']}")

print()
print("=" * 55)
print("第 4 部分：函数 def —— 把一段逻辑打包，起个名字")
print("=" * 55)


def check_login(username, password):
    """判断登录结果。

    这就是「被测功能」的简化版：
    给它用户名和密码，它告诉你会发生什么。
    """
    if username == "standard_user" and password == "secret_sauce":
        return "登录成功"
    elif password == "":
        return "密码不能为空"
    elif username == "":
        return "用户名不能为空"
    else:
        return "用户名或密码错误"


print(check_login("standard_user", "secret_sauce"))
print(check_login("standard_user", ""))
print(check_login("hacker", "123"))

print()
print("=" * 55)
print("第 5 部分：数据驱动 —— 你已经会跑「自动化」了")
print("=" * 55)

# 关键思想：数据和代码分开。
# 以后要加用例，只改数据列表，不用碰逻辑代码。
real_cases = [
    {"username": "standard_user", "password": "secret_sauce"},
    {"username": "standard_user", "password": ""},
    {"username": "hacker",        "password": "123"},
]

for case in real_cases:
    result = check_login(case["username"], case["password"])
    u = case["username"] or "(空)"
    p = case["password"] or "(空)"
    print(f"  输入 {u} / {p}   =>   {result}")

print()
print("演示结束。现在去看 day02_exercise.py，轮到你自己写了。")
