# -*- coding: utf-8 -*-
"""页面元素探针（专业工具）。

【这是什么】
真实工作中，测试工程师拿到一个陌生页面时，会先跑一个这种"探针"，
把页面上所有可交互元素的真实属性打印出来，快速摸清结构。

【为什么比 F12 好用】
F12 要你自己在 HTML 树里找；探针直接把答案打在屏幕上。

【怎么用】
双击 run_inspect.bat

【重要】
这个工具是"辅助"，不是"替代"。
以后你自己遇到新页面，第一反应还是应该打开 F12 看一眼——
因为不是所有网站你都方便写脚本去探测。
"""

import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

root = Path(__file__).parent.parent
BASE_URL = "https://www.saucedemo.com"


def build_driver():
    options = Options()
    options.add_argument(f"--user-data-dir={root / '.edge-profile'}")
    options.add_argument("--window-size=1280,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    if os.environ.get("HEADLESS") == "1":
        options.add_argument("--headless=new")
    return webdriver.Edge(options=options)


def dump(driver, title):
    """打印当前页面上所有可交互元素的属性。"""
    print()
    print("=" * 78)
    print(f"  {title}")
    print(f"  当前地址: {driver.current_url}")
    print("=" * 78)

    rows = []
    for tag, selector in (("input", "input"),
                          ("button", "button"),
                          ("a", "a"),
                          ("select", "select")):
        for el in driver.find_elements(By.CSS_SELECTOR, selector):
            try:
                rows.append({
                    "tag": el.tag_name,
                    "id": el.get_attribute("id") or "",
                    "name": el.get_attribute("name") or "",
                    "class": (el.get_attribute("class") or "")[:40],
                    "data-test": el.get_attribute("data-test") or "",
                    "text": (el.text or el.get_attribute("value") or "").strip()[:24],
                })
            except Exception:
                continue

    if not rows:
        print("  （没有找到可交互元素）")
        return

    header = f"  {'标签':<7}{'id':<42}{'class':<30}{'data-test':<28}文字"
    print(header)
    print("  " + "-" * 108)
    for r in rows:
        if not (r["id"] or r["data-test"] or r["class"]):
            continue
        print(f"  {r['tag']:<7}{r['id']:<42}{r['class']:<30}{r['data-test']:<28}{r['text']}")


def main():
    driver = build_driver()
    wait = WebDriverWait(driver, 10)
    try:
        # ---------- 1. 登录页 ----------
        driver.get(BASE_URL)
        # 先清空上一次残留的 localStorage / cookie，
        # 否则购物车里的商品会一次次累积，探测结果就不准了
        driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
        driver.delete_all_cookies()
        driver.get(BASE_URL)
        wait.until(EC.presence_of_element_located((By.ID, "login-button")))
        dump(driver, "【第 1 页】登录页")

        # ---------- 2. 商品列表页 ----------
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        wait.until(EC.url_contains("inventory"))
        dump(driver, "【第 2 页】商品列表页（登录后）")

        # ---------- 3. 购物车页 ----------
        buttons = driver.find_elements(By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
        buttons[0].click()
        buttons[1].click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.url_contains("cart"))
        dump(driver, "【第 3 页】购物车页")

        # 购物车里的条目结构单独打印
        print()
        print("  —— 购物车里一个『条目』的完整 HTML ——")
        items = driver.find_elements(By.CLASS_NAME, "cart_item")
        if items:
            print("  " + items[0].get_attribute("outerHTML").replace("\n", "\n  ")[:600])
        print()
        print("  —— 商品名元素的 class ——")
        for e in driver.find_elements(By.CLASS_NAME, "inventory_item_name"):
            print("   ", repr(e.get_attribute("class")), "->", repr(e.text))
            break

    finally:
        driver.quit()

    print()
    print("=" * 78)
    print("  探针结束。把上面这些真实属性抄进你的定位器里。")
    print("=" * 78)


if __name__ == "__main__":
    main()
