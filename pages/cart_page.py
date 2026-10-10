# -*- coding: utf-8 -*-
"""购物车页的页面对象（Page Object）。

【这个文件是骨架，要你自己填】
定位器全是 "???"，请打开浏览器按 F12，自己找出真实的属性值。

【怎么做】
1. 手动登录 saucedemo，随便加 2 件商品，点进购物车页
2. 按 F12，用左上角的箭头点页面上的元素
3. 看 HTML 里的 id / class / data-test 属性
4. 按 docs/Day3-任务书.md 里的「定位器优先级」挑一个写进来
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    """saucedemo 购物车页。"""

    # URL 里出现这一段，就说明在购物车页
    URL_KEYWORD = "cart"

    # ---------- TODO 5：补全下面 3 个定位器 ----------
    # 自己用 F12 找，不要猜

    CART_ITEM = (By.CLASS_NAME, "???")      # 购物车里的一个"条目"（一整行）
    ITEM_NAME = (By.CLASS_NAME, "???")      # 条目里商品名称的文字
    CHECKOUT_BUTTON = (By.ID, "???")        # 结账按钮

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ---------- 这个我帮你写好了，当参考 ----------

    def wait_until_loaded(self, timeout=10):
        """等待购物车页真正加载出来。"""
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(self.URL_KEYWORD)
        )
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(self.CART_ITEM)
        )
        return self

    # ---------- TODO 6：购物车里有几件商品 ----------
    @property
    def item_count(self):
        """返回购物车里的商品条数（int）。

        提示：跟 InventoryPage.item_count 是一个写法。
        """
        raise NotImplementedError("TODO 6 还没写")

    # ---------- TODO 7：所有商品名称 ----------
    @property
    def item_names(self):
        """返回购物车里所有商品名称组成的列表（list[str]）。

        提示：用列表推导式，参考 InventoryPage.item_names。
        """
        raise NotImplementedError("TODO 7 还没写")

    # ---------- TODO 8：点击结账按钮 ----------
    def click_checkout(self):
        """点击 Checkout 按钮。

        提示：先 find_element，再 .click()，最后 return self。
        """
        raise NotImplementedError("TODO 8 还没写")
