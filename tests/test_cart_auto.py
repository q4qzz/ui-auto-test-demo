# -*- coding: utf-8 -*-
"""购物车自动化测试用例 —— 全部是填空题。

【流程】
    登录 -> 加 2 件商品 -> 检查角标显示 2 -> 进购物车 -> 检查里面有 2 件商品

【前提】
先把 pages/inventory_page.py 和 pages/cart_page.py 的填空做完。

【填空说明】
每个 ★ 只需要写一行，照着上面注释里的提示写就行。
"""

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def test_add_two_items_and_check_cart(login_page):
    """登录后加 2 件商品，角标显示 2，购物车里正好有这 2 件。"""

    # ---------- 第 1 步：登录（我写好了）----------
    login_page.login(USERNAME, PASSWORD)
    inventory = InventoryPage(login_page.driver).wait_until_loaded()

    # ---------- TODO 9：把前 2 件商品加入购物车 ----------
    # 调用你在 inventory_page.py 里写好的那个方法。
    # 方法名：add_first_n_to_cart
    # 参数  ：要加几件
    inventory.add_first_n_to_cart(2)

    # ---------- TODO 10：断言购物车角标显示 2 ----------
    # 提示：assert inventory.cart_badge_count == 2
    #       记得在断言后面加一句说明，失败了才知道原因：
    #       assert 条件, f"期望角标是 2，实际是 {inventory.cart_badge_count}"
    assert inventory.cart_badge_count == 2, f"❌ 角标应该是 2，实际是 {inventory.cart_badge_count}"
    # ---------- TODO 11：进入购物车页 ----------
    # 提示：cart = CartPage(login_page.driver).wait_until_loaded()
    cart = CartPage(login_page.driver).wait_until_loaded()

    # ---------- TODO 12：断言购物车里有 2 件商品 ----------
    # 提示：assert cart.item_count == 2
    assert cart.item_count == 2, f"❌ 购物车里应该有 2 件，实际是 {cart.item_count}"

    # ---------- 加分题（选做，做完上面的再说）----------
    # 再断言：购物车里的商品名称，和商品列表页前两件完全一致
    # 提示：inventory.item_names[:2] == cart.item_names
