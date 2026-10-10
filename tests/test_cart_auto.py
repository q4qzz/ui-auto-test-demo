# -*- coding: utf-8 -*-
"""购物车自动化测试用例 —— 要你自己写。

【流程】
    登录 -> 加 2 件商品 -> 检查角标显示 2 -> 进购物车 -> 检查里面有那 2 件商品

【前提】
先完成 pages/inventory_page.py 的 TODO 1~4
和 pages/cart_page.py 的 TODO 5~8，
否则这个文件跑起来会一直报 NotImplementedError。
"""

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def test_add_two_items_and_check_cart(login_page):
    """登录后加 2 件商品，角标显示 2，购物车里正好有这 2 件。"""

    # ---------- 第 1 步：登录 ----------
    login_page.login(USERNAME, PASSWORD)
    inventory = InventoryPage(login_page.driver).wait_until_loaded()

    # ---------- TODO 9：把商品列表里的前 2 件加入购物车 ----------
    # 用你刚写的方法，一行就够

    # ---------- TODO 10：断言购物车角标显示 2 ----------
    # 提示：assert inventory.cart_badge_count == 2
    #       断言失败时最好带上提示信息，方便定位问题：
    #       assert x == 2, f"期望角标是 2，实际是 {x}"

    # ---------- TODO 11：进入购物车页 ----------
    # 提示：cart = CartPage(login_page.driver).wait_until_loaded()

    # ---------- TODO 12：断言购物车里有 2 件商品 ----------
    # 提示：assert cart.item_count == 2

    # ---------- 加分题（选做）----------
    # 再加一条断言：购物车里的两件商品名称，
    # 和商品列表页前两件商品的名称完全一致。
    # 提示：inventory.item_names[:2] 是列表页前两件
    #       cart.item_names 是购物车里的
    #       两个列表比较可以直接用 ==

    raise NotImplementedError("TODO 9~12 还没写完，加油")
