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
