# -*- coding: utf-8 -*-
"""商品列表页的页面对象（Page Object）。

登录成功后就会来到这个页面，所以我们用它来判断"登录是否真的成功了"。
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    """saucedemo 商品列表页。"""

    # URL 里出现这一段，就说明在商品页
    URL_KEYWORD = "inventory"

    # ---------- 元素定位器 ----------
    PAGE_TITLE = (By.CLASS_NAME, "title")
    ITEM = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ---------- 操作 ----------

    def wait_until_loaded(self, timeout=10):
        """等待商品列表真正加载出来。"""
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(self.URL_KEYWORD)
        )
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(self.ITEM)
        )
        return self

    # ---------- 查询 ----------

    @property
    def title(self):
        """页面标题文字，正常应该是 Products。"""
        return self.driver.find_element(*self.PAGE_TITLE).text

    @property
    def item_count(self):
        """商品数量。"""
        return len(self.driver.find_elements(*self.ITEM))

    @property
    def item_names(self):
        """所有商品名称。"""
        return [e.text for e in self.driver.find_elements(*self.ITEM_NAME)]

    @property
    def item_prices(self):
        """所有商品价格。"""
        return [e.text for e in self.driver.find_elements(*self.ITEM_PRICE)]

    @property
    def is_loaded(self):
        """当前是否停在商品列表页。"""
        return self.URL_KEYWORD in self.driver.current_url

    # ==========================================================
    # TODO 区域 —— 这一整段要你自己写
    # 写之前先看 docs/Day3-任务书.md 的第一部分（F12 找元素）
    # ==========================================================

    # ---------- TODO 1：补全下面 3 个定位器 ----------
    # 打开 F12，把鼠标点到页面上的元素上，看它的 HTML 属性
    #
    # 提示：
    #   - 加购按钮有 6 个，data-test 都以 "add-to-cart" 开头
    #   - 购物车角标的 class 是 shopping_cart_ 开头
    #   - 购物车图标的 class 也是 shopping_cart_ 开头

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "???")   # ← 你自己填
    CART_BADGE = (By.CLASS_NAME, "???")             # ← 你自己填
    CART_LINK = (By.CLASS_NAME, "???")              # ← 你自己填

    # ---------- TODO 2：把前 n 件商品加入购物车 ----------
    def add_first_n_to_cart(self, n):
        """把商品列表里的前 n 件商品加入购物车。

        思路：
          1. 用 find_elements 找到所有加购按钮（注意是复数）
          2. 循环取前 n 个，逐个 .click()
          3. 记得返回 self，这样能链式调用

        提示：buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
             然后 buttons[:n] 就是前 n 个
        """
        raise NotImplementedError("TODO 2 还没写")

    # ---------- TODO 3：读取购物车角标数字 ----------
    @property
    def cart_badge_count(self):
        """返回购物车角标上的数字。

        重点：加购【之前】页面上根本没有角标这个元素。
              所以必须用 find_elements（复数），它找不到时返回空列表，
              而不是像 find_element 那样直接抛异常。

        返回：int，没有角标时返回 0
        """
        raise NotImplementedError("TODO 3 还没写")

    # ---------- TODO 4：进入购物车页 ----------
    def open_cart(self):
        """点击右上角的购物车图标，进入购物车页。"""
        raise NotImplementedError("TODO 4 还没写")
