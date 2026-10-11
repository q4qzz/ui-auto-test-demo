# -*- coding: utf-8 -*-
"""购物车页的页面对象（Page Object）—— 全部是填空题。

【先做什么】
1. 读 docs/Selenium最小知识卡.md（5 分钟）
2. 双击 run_inspect.bat，把输出留在屏幕上当"答案纸"

【填空说明】
每个空都标了 ★，只需要填一个词或一行，不用写整个方法。
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    """saucedemo 购物车页。"""

    URL_KEYWORD = "cart"

    # ==========================================================
    # 填空区
    # ==========================================================

    # ---------- TODO 5：抄 3 个属性 ----------
    # 跑 run_inspect.bat，看【第 3 页】购物车页的输出

    # ★ 空 5：购物车里"一个条目"（一整行）的 class
    #   提示：探针会额外打印「购物车里一个条目的完整 HTML」，
    #        看最外层 <div class="..."> 里的内容
    CART_ITEM = (By.CLASS_NAME, "★这里填★")

    # ★ 空 6：条目里"商品名称"的 class
    #   提示：探针最后会打印「商品名元素的 class」，直接抄
    ITEM_NAME = (By.CLASS_NAME, "★这里填★")

    # ★ 空 7：结账按钮的 id
    #   提示：【第 3 页】的表格里，找文字是 Checkout 的那一行，看它的 id 列
    CHECKOUT_BUTTON = (By.ID, "★这里填★")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ---------- 这个我写好了，当参考，不用改 ----------
    def wait_until_loaded(self, timeout=10):
        """等待购物车页真正加载出来。"""
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(self.URL_KEYWORD)
        )
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(self.CART_ITEM)
        )
        return self

    # ---------- TODO 6：只填一行 ----------
    @property
    def item_count(self):
        """购物车里有几件商品。

        find_elements 找出所有条目，返回列表。
        ★ 空 8：怎么数出这个列表里有几个？用哪个内置函数？
        （看 docs/Selenium最小知识卡.md 最下面的「五分钟小测」）
        """
        items = self.driver.find_elements(*self.CART_ITEM)
        return ★这里填★(items)

    # ---------- TODO 7：只填一行 ----------
    @property
    def item_names(self):
        """购物车里所有商品的名称，返回列表。

        下面这行"列表推导式"的意思是：
          把每个条目的名称文字，收集成一个新列表

        ★ 空 9：从每个条目里把商品名称元素找出来，再取它的 .text
               提示：条目.find_element(*self.ITEM_NAME).text
        """
        items = self.driver.find_elements(*self.CART_ITEM)
        return [★这里填★ for item in items]

    # ---------- TODO 8：照抄示范，自己写 ----------
    def click_checkout(self):
        """点击 Checkout 按钮。

        照着 inventory_page.py 里 open_cart() 的写法来：
            self.driver.find_element(*self.某定位器).click()
            return self
        """
        ★这一整行你自己写★
