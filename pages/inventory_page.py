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
    # TODO 区域 —— 全部是「填空」，每个空只填一个词或一行
    #
    # 先读 docs/Selenium最小知识卡.md（5 分钟），再回来填。
    # 填空处都标了 ★
    # ==========================================================

    # ---------- TODO 1：抄 3 个 class 名 ----------
    # 双击 run_inspect.bat，看【第 2 页】输出的 class 列，
    # 把对应的内容抄进下面两个空里（不要抄引号）

    # 这个我写好了，当示范：
    # data-test 以 add-to-cart 开头的按钮，一次匹配全部 6 个
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test^='add-to-cart']")

    # ★ 空 1：购物车角标的 class（探针输出里找 shopping_cart_badge）
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    # ★ 空 2：购物车图标的 class（探针输出里找 shopping_cart_link）
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    # ---------- TODO 2：只填一行 ----------
    def add_first_n_to_cart(self, n):
        """把前 n 件商品加入购物车。

        下面代码我都写好了，只有一个空要你填。
        """
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        for b in buttons[:n]:
            b.click()
        return self

    # ---------- TODO 3：只填一行 ----------
    @property
    def cart_badge_count(self):
        """返回购物车角标上的数字；没有角标时返回 0。

        这个我也写好了大半，只有一个空。
        """
        badges = self.driver.find_elements(*self.CART_BADGE)
        if not badges:
            return 0
        # ★ 空 4：badges[0].text 读到的是字符串 "2"，
        #         要把它变成数字 2 再返回。想想用哪个内置函数？
        return int(badges[0].text)

    # ---------- TODO 4：照抄 TODO 2 的写法，自己写一个 ----------
    def open_cart(self):
        """点击右上角的购物车图标，进入购物车页。

        参照上面「动作 5」的示范：
            self.driver.find_element(*self.CART_LINK).click()
            return self
        """
        self.driver.find_element(*self.CART_LINK).click()
        return self
