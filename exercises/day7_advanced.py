# -*- coding: utf-8 -*-
"""E 组加练：10 道进阶题（工程化写法）。

【和 A~D 组的区别】
  A~D 练的是"单个动作怎么写"。
  E 组练的是"专业的人怎么写"——等待、参数化、多重断言。

【三个新概念】
  1. 显式等待 WebDriverWait —— 不用 sleep 硬等，等元素真的出现
  2. 参数化 @pytest.mark.parametrize —— 一个函数跑 N 组数据
  3. 多重断言 —— 一条用例验证多个点

【怎么练】
  和之前一样：写在「你的代码」下面，Ctrl+S 保存，
  双击 run_one_practice.bat 输入题号（E1、E2 ...）。
"""

import pytest
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://www.saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
ADD_TO_CART = "button[data-test^='add-to-cart']"
BADGE = "shopping_cart_badge"


def 登录(driver):
    """辅助函数：完整登录并等商品列表出现。"""
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("inventory"))
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ADD_TO_CART)))


def 读取文字列表(driver, class名, 超时=10):
    """辅助函数：等元素稳定后，读出它们显示的所有文字（带重试，防 stale element）。"""

    def _读(d):
        try:
            elements = d.find_elements(By.CLASS_NAME, class名)
            if not elements:
                return False
            return [e.text for e in elements]
        except StaleElementReferenceException:
            return False

    return WebDriverWait(driver, 超时).until(_读)


# ================================================================
# E1~E3：显式等待（不用 sleep，等元素真的出现）
# ================================================================


def test_E1_用显式等待等元素出现(driver):
    """E1：打开登录页，用【显式等待】等到登录按钮出现，然后存进变量 btn。

    写法：
        wait = WebDriverWait(driver, 10)
        btn = wait.until(EC.presence_of_element_located((By.ID, "login-button")))

    注意：EC.presence_of_element_located 的括号里，要放一个【元组】，
         所以是双重括号 ((By.ID, "..."))。
    """
    driver.get(BASE_URL)
    # ======== 你的代码写在这行下面（2 行）========
    wait = WebDriverWait(driver, 10)
    btn = wait.until(EC.presence_of_element_located((By.ID, "login-button")))

    # ======== 自动批改 ========
    assert btn.get_attribute("value") == "Login", (
        f"❌ 等到的按钮文字是 {btn.get_attribute('value')!r}，应该是 'Login'"
    )


def test_E2_等待网址变化(driver):
    """E2：登录后，用【显式等待】等网址里出现 inventory，然后存进 url。

    写法：
        WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
    """
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
    # ======== 你的代码写在这行下面（1~2 行）========
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
    url = driver.current_url
    # ======== 自动批改 ========
    assert "inventory" in url, f"❌ url 是 {url!r}"


def test_E3_三条断言验证一次登录(driver):
    """E3：登录后，把三个值分别存进变量，每个各写一条 assert。

    写 6 行：
      1) url = 当前网址
      2) assert "inventory" in url, "不在商品页"
      3) 标题 = 标题元素的文字（class 是 title）
      4) assert 标题 == "Products", "标题不对"
      5) 数量 = 商品数量（用 len + find_elements，class 是 inventory_item）
      6) assert 数量 == 6, "商品数量不对"
    """
    登录(driver)
    # ======== 你的代码写在这行下面（6 行）========
    url = driver.current_url
    assert "inventory" in url, "不在商品页"
    标题 = driver.find_element(By.CLASS_NAME, "title").text
    assert 标题 == "Products", "标题不对"
    数量 = len(driver.find_elements(By.CLASS_NAME, "inventory_item"))
    assert 数量 == 6, "商品数量不对"
    # ======== 自动批改 ========
    assert "inventory" in url, f"❌ url 是 {url!r}"
    assert 标题 == "Products", f"❌ 标题是 {标题!r}，应该是 'Products'"
    assert 数量 == 6, f"❌ 商品数量是 {数量!r}，应该是 6"


# ================================================================
# E4~E5：参数化（一个函数跑 N 组数据）—— 面试高频考点
# ================================================================


@pytest.mark.parametrize(
    "username",
    ["standard_user", "problem_user", "error_user"],
)
def test_E4_多个账号都能登录(driver, username):
    """E4：下面 3 个账号都能成功登录。

    注意函数多了一个参数 username（由 parametrize 自动喂进来），
    你写代码时直接用它，一个字都不用改就能跑 3 遍。

    提示：直接在 driver 上操作，写 4 行——
          driver.get(BASE_URL)
          往用户名框输入 username      ← 注意这里用参数，不是字符串
          往密码框输入 PASSWORD
          点登录按钮
    """
    driver.get(BASE_URL)
    # ======== 你的代码写在这行下面（4 行）========
    driver.get(BASE_URL)
    driver.find.element(By.ID,"user-name").sent(username)
    driver.find.element(By.ID,"password").sent(PASSWORD)
    driver.find.element(By.ID,"button-login").click()

    # ======== 自动批改 ========
    # 点完登录按钮后网址不会立刻变，所以这里最多等 10 秒再看
    from time import sleep
    for _ in range(20):
        if "inventory" in driver.current_url:
            break
        sleep(0.5)
    assert "inventory" in driver.current_url, (
        f"❌ 账号 {username!r} 登录失败，当前地址是 {driver.current_url!r}"
    )


@pytest.mark.parametrize(
    "username, password, 关键字",
    [
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("standard_user", "wrong", "do not match"),
        ("locked_out_user", "secret_sauce", "locked out"),
    ],
    ids=["用户名为空", "密码为空", "密码错误", "账号被锁定"],
)
def test_E5_错误输入应报错(driver, username, password, 关键字):
    """E5：4 组错误数据，都应该登录失败，且报错信息里含对应关键字。

    提示：写 4 行——
          driver.get(BASE_URL)
          往用户名框输入 username
          往密码框输入 password
          点登录按钮
          然后用 find_elements 找报错元素，断言里面含关键字

    报错元素的写法：driver.find_elements(By.CSS_SELECTOR, "[data-test='error']")
    """
    driver.get(BASE_URL)
    # ======== 你的代码写在这行下面（4~6 行）========
    driver.get(BASE_URL)
    driver.find_element(By.ID,"user-name").sent_keys(username)
    driver.find_element(By.ID,"password").sent_keys(PASSWORD)
    driver.find_element(By.ID,"login-button").click()
    # ======== 自动批改 ========
    # 报错提示要等一会儿才出现，所以这里最多等 10 秒
    from time import sleep
    errors = []
    for _ in range(20):
        errors = driver.find_elements(By.CSS_SELECTOR, "[data-test='error']")
        if errors:
            break
        sleep(0.5)
    assert len(errors) == 1, "❌ 没有出现错误提示"
    assert 关键字.lower() in errors[0].text.lower(), (
        f"❌ 报错信息是 {errors[0].text!r}，应该含 {关键字!r}"
    )


# ================================================================
# E6~E8：确认"不存在" + 批量校验
# ================================================================


def test_E6_确认角标不存在(driver):
    """E6：登录后（还没加购），确认购物车角标【不存在】。

    要点：不能用 find_element，因为它找不到会直接抛异常。
         必须用 find_elements（复数），找不到时返回空列表。

    提示：写 1 行，把找出来的东西存进 badges
    """
    登录(driver)
    # ======== 你的代码写在这行下面（1 行）========
    badges = driver.find.elements(By.CLASS,"shopping-cart")
    # ======== 自动批改 ========
    assert badges == [], f"❌ 还没加购，不该有角标，但找到了 {len(badges)} 个"


def test_E7_所有价格都以美元符开头(driver):
    """E7：登录后，验证【所有】商品价格都以 "$" 开头。

    提示：分 2 步——
          1. 用列表推导式取出所有价格文字，存进 prices
          2. 用 for 循环逐个检查，每个都要以 "$" 开头
             （判断"以某字开头"用 .startswith("$")）

    注意：如果某个价格不以 $ 开头，要让它断言失败。
    """
    登录(driver)
    # ======== 你的代码写在这行下面（3~4 行）========

    # ======== 自动批改 ========
    assert len(prices) == 6, f"❌ 应该取到 6 个价格，你取到 {len(prices)} 个"
    for p in prices:
        assert p.startswith("$"), f"❌ 价格 {p!r} 不以 $ 开头"


def test_E8_所有商品名都不为空(driver):
    """E8：登录后，验证【所有】商品名称都不为空字符串。

    提示：取出所有商品名存进 names，然后逐个断言 len(名称) > 0
    """
    登录(driver)
    # ======== 你的代码写在这行下面（3~4 行）========


    # ======== 自动批改 ========
    assert len(names) == 6, f"❌ 应该取到 6 个商品名，你取到 {len(names)} 个"
    for n in names:
        assert len(n) > 0, "❌ 有商品名是空的"


# ================================================================
# E9~E10：综合
# ================================================================


def test_E9_加购后按钮文字变成Remove(driver):
    """E9：加购第 1 件商品后，验证那个按钮的文字从 "Add to cart" 变成了 "Remove"。

    提示：分 3 步——
          1. 找出所有加购按钮，点第 1 个
          2. 用 find_elements 找出所有【移除】按钮
             （CSS 选择器 "button[data-test^='remove']"，和加购按钮一个思路）
          3. 断言移除按钮的数量是 1
    """
    登录(driver)
    # ======== 你的代码写在这行下面（3 行）========


    # ======== 自动批改 ========
    assert len(remove_buttons) == 1, (
        f"❌ 期望有 1 个 Remove 按钮，实际找到 {len(remove_buttons)} 个"
    )
    assert remove_buttons[0].text == "Remove", (
        f"❌ 按钮文字是 {remove_buttons[0].text!r}，应该是 'Remove'"
    )


def test_E10_端到端综合(driver):
    """E10（最难）：一条完整用例，验证 5 个点。

    按顺序写 7 行：
      1. assert 网址含 inventory
      2. assert 商品数量是 6（find_elements + len）
      3. 记录前两件商品的名字 → 变量 记录的名字
         （用 读取文字列表(driver, "inventory_item_name")[:2]）
      4. 加购前 2 件（for 循环，每次重新查找按钮）
      5. assert 角标数字是 2
      6. 点购物车图标进购物车（class 是 shopping_cart_link），等 cart_item 出现
      7. 读出购物车里的商品名 → 变量 购物车名字
         （用 读取文字列表(driver, "inventory_item_name")）

    提示：这一题要用到 A~D 组的全部技能。
    """
    登录(driver)
    # ======== 你的代码写在这行下面（7 行）========


    # ======== 自动批改 ========
    assert 记录的名字 == 购物车名字, (
        f"❌ 不一致\n   记录：{记录的名字}\n   购物车：{购物车名字}"
    )
