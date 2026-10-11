# -*- coding: utf-8 -*-
"""Day 4 专项练习：把 Selenium 五个动作刷到不用想。

【怎么练】
  每道题只需要写 1~3 行，写在「你的代码」下面。
  写完就 Ctrl+S 保存，双击 run_practice.bat。
  每题自带自动批改，跑完立刻知道哪题对、哪题错。

【卡住了看哪】
  docs/Selenium最小知识卡.md —— 五个动作全在里面

【重要】
  不要一次做完 20 题。做完一题就跑一次，看到 ✅ 再往下。
  错了也正常，报错信息会告诉你差在哪。
"""

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://www.saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
ADD_TO_CART = "button[data-test^='add-to-cart']"


def 登录(driver):
    """辅助函数：完整走一遍登录，并等商品列表加载出来。

    后面的练习可以直接调用它，不用自己写登录。
    """
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    # 等页面真的跳过去、按钮真的出现，否则后面的操作会找不到元素
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("inventory"))
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ADD_TO_CART)))


def 加购(driver, 件数):
    """辅助函数：把前 N 件商品加入购物车。

    ⚠️ 注意里面的写法：每点一次都【重新查找】一次按钮。
       因为点完之后页面会重新渲染，之前找到的元素会"失效"
       （学名叫 stale element，是 Selenium 最经典的坑之一，
         B5 那题就是专门练这个的）。
    """
    for _ in range(件数):
        buttons = driver.find_elements(By.CSS_SELECTOR, ADD_TO_CART)
        buttons[0].click()


def 读取文字列表(driver, class名, 超时=10):
    """辅助函数：等元素稳定后，读出它们显示的所有文字。返回一个列表。

    ⚠️ 为什么读个文字还要这么麻烦？

       页面刚跳转过去时，元素可能还在渲染中。
       你 find_elements 拿到元素、准备读 .text 的那一瞬间，
       页面把它替换掉了 —— 这时就会报
       StaleElementReferenceException（元素已失效）。

       解决办法：把"读取"整个动作包一层重试。
       读失败（元素失效）或还没渲染好，就重新找一遍再读，
       直到成功或超时。这是自动化测试里保证用例稳定的标准手法之一。
    """

    def _读(d):
        try:
            elements = d.find_elements(By.CLASS_NAME, class名)
            if not elements:
                return False
            return [e.text for e in elements]
        except StaleElementReferenceException:
            return False

    return WebDriverWait(driver, 超时).until(_读)


def 进购物车(driver, 超时=10):
    """辅助函数：点购物车图标进购物车，并等商品真的渲染出来。

    ⚠️ 为什么不能只判断网址？

       网址变成 .../cart.html 了，**不代表页面内容已经渲染完**。
       这时候马上去数商品，很可能数到 0 —— 用例就会时好时坏（flaky）。

       Selenium 里这条经验非常值钱：
       **网址变了 ≠ 页面加载完了。**
       永远要等"你要操作的那个元素真的出现"，而不是等网址。

       （这个辅助函数假设购物车里有商品；空购物车会超时，这是故意的。）
    """
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 超时).until(EC.url_contains("cart"))
    WebDriverWait(driver, 超时).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
    )


# ================================================================
# A 组：基础动作（6 题）—— 在登录页上练
# ================================================================


def test_A1_打开登录页(driver):
    """A1：让浏览器打开 saucedemo 登录页。写 1 行。"""
    # ======== 你的代码写在这行下面 ========
    driver.get(BASE_URL)

    # ======== 下面是自动批改，不要动 ========
    assert "saucedemo.com" in driver.current_url, (
        f"❌ 没有打开 saucedemo，当前地址是 {driver.current_url!r}\n"
        f"   提示：让浏览器访问网址用 driver.get(网址)"
    )


def test_A2_在用户名框输入(driver):
    """A2：在【用户名】输入框里输入 standard_user。写 1 行。

    提示：分两步想——先找到那个框，再往里输入文字。
    """
    driver.get(BASE_URL)
    # ======== 你的代码写在这行下面 ========
    driver.find_element(By.ID, "user-name").send_keys("standard_user")


    # ======== 自动批改 ========
    value = driver.find_element(By.ID, "user-name").get_attribute("value")
    assert value == "standard_user", (
        f"❌ 用户名框里的内容是 {value!r}，应该是 'standard_user'\n"
        f"   提示：输入文字用 元素.send_keys(\"内容\")"
    )


def test_A3_在密码框输入(driver):
    """A3：在【密码】框里输入 secret_sauce。写 1 行。

    提示：和 A2 一模一样，只是 id 换成 password。
    """
    driver.get(BASE_URL)
    # ======== 你的代码写在这行下面 ========
    driver.find_element(By.ID, "password").send_keys("secret_sauce")



    # ======== 自动批改 ========
    value = driver.find_element(By.ID, "password").get_attribute("value")
    assert value == "secret_sauce", (
        f"❌ 密码框里是 {value!r}，应该是 'secret_sauce'"
    )


def test_A4_先清空再输入(driver):
    """A4：用户名框里现在有一串错的内容，请你【清空】它，再输入 standard_user。

    提示：写 2 行。知识卡【动作 3】表格里第三行就是"清空"。
    """
    driver.get(BASE_URL)
    box = driver.find_element(By.ID, "user-name")
    box.send_keys("这是错误的内容，请清掉")
    # ======== 你的代码写在这行下面（2 行）========


    # ======== 自动批改 ========
    value = box.get_attribute("value")
    assert value == "standard_user", (
        f"❌ 清空后输入的结果是 {value!r}，应该是 'standard_user'\n"
        f"   提示：先 元素.clear() 清空，再 元素.send_keys(...) 输入"
    )


def test_A5_完整登录(driver):
    """A5：完整登录。写 3 行：输用户名、输密码、点登录按钮。

    提示：第 3 步是"点击"，知识卡【动作 3】第一行。
    """
    driver.get(BASE_URL)
    # ======== 你的代码写在这行下面（3 行）========


    # ======== 自动批改 ========
    assert "inventory" in driver.current_url, (
        f"❌ 没有登录成功，当前地址是 {driver.current_url!r}\n"
        f"   提示：登录要三步——输用户名、输密码、点登录按钮"
    )


def test_A6_读取输入框里的内容(driver):
    """A6：先在用户名框里输入 standard_user，然后把它【读回来】存进变量 text。

    ⚠️ 这一题有个真实的坑：
       输入框（input 标签）里显示的内容，用 .text 是【读不到】的，
       必须用 .get_attribute("value") 读它的 value 属性。

    提示：读属性用 元素.get_attribute("属性名")
    """
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    # ======== 你的代码写在这行下面 ========


    # ======== 自动批改 ========
    assert text == "standard_user", (
        f"❌ 读到的内容是 {text!r}，应该是 'standard_user'\n"
        f"   提示：输入框用 .get_attribute(\"value\") 读，不要用 .text"
    )


# ================================================================
# B 组：找一堆元素（5 题）—— 需要先登录
# ================================================================


def test_B1_数一数有几个加购按钮(driver):
    """B1：数一数商品列表页有几个「Add to cart」按钮，存进 count。

    提示：先把所有加购按钮找出来放一个变量（例如 buttons），
          再数一数它有几个，存进 count。
    """
    登录(driver)
    # ======== 你的代码写在这行下面（2 行）========


    # ======== 自动批改 ========
    assert count == 6, (
        f"❌ 你数出来是 {count}，应该是 6\n"
        f"   提示：len(列表) 就是个数"
    )


def test_B2_取出所有商品名(driver):
    """B2：把所有商品名称取出来，存进列表 names。

    提示：先找出所有商品名元素（class 是 inventory_item_name），
          再用列表推导式把它们的 .text 收集起来。
    """
    登录(driver)
    # ======== 你的代码写在这行下面 ========


    # ======== 自动批改 ========
    assert len(names) == 6, f"❌ 应该取到 6 个商品名，你取到 {len(names)} 个"
    assert names[0] == "Sauce Labs Backpack", (
        f"❌ 第一个商品名是 {names[0]!r}，应该是 'Sauce Labs Backpack'"
    )


def test_B3_取出所有价格(driver):
    """B3：把所有商品价格取出来，存进列表 prices。

    提示：class 是 inventory_item_price。和 B2 一个套路。
    """
    登录(driver)
    # ======== 你的代码写在这行下面 ========


    # ======== 自动批改 ========
    assert len(prices) == 6, f"❌ 应该取到 6 个价格，你取到 {len(prices)} 个"
    assert prices[0] == "$29.99", f"❌ 第一个价格是 {prices[0]!r}，应该是 '$29.99'"


def test_B4_点击第一个加购按钮(driver):
    """B4：点击【第一个】加购按钮。写 2 行。

    提示：先找出所有加购按钮，再取出第 1 个点它（列表下标从 0 开始）。
    """
    登录(driver)
    # ======== 你的代码写在这行下面（2 行）========


    # ======== 自动批改 ========
    badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(badge) == 1 and badge[0].text == "1", (
        "❌ 购物车角标没有变成 1，说明第一个按钮没被点到"
    )


def test_B5_加购两件并处理失效元素(driver):
    """B5（重点题）：把前 2 件商品加入购物车，让角标变成 2。

    ⚠️ 这一题有个真实的坑，也是面试高频考点：

       你找到的按钮列表，在你点击之后会【失效】。
       因为点完一个，页面会重新渲染（按钮从 Add to cart 变成 Remove），
       之前拿到的元素引用就作废了。再点它就会报
       StaleElementReferenceException。

       正确做法：**每点一次，就重新查找一次**。

    提示：循环体里写 2 行——
          第 1 行：重新查找所有加购按钮，存进 buttons
          第 2 行：点击 buttons[0]（这时候的第 0 个，就是还没加购的第一件）
    """
    登录(driver)
    for _ in range(2):
        # ======== 你的代码写在这行下面（2 行）========
        pass

    # ======== 自动批改 ========
    badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(badge) == 1 and badge[0].text == "2", (
        "❌ 购物车角标不是 2，说明没成功加购两件\n"
        "   提示：每次点击前都要重新 find_elements 一次"
    )


# ================================================================
# C 组：读信息 + 断言（5 题）
# ================================================================


def test_C1_读角标文字(driver):
    """C1：加购 1 件商品后，把购物车角标上的文字读出来，存进 badge_text。

    提示：class 是 shopping_cart_badge
    """
    登录(driver)
    driver.find_elements(By.CSS_SELECTOR, ADD_TO_CART)[0].click()
    # ======== 你的代码写在这行下面 ========


    # ======== 自动批改 ========
    assert badge_text == "1", (
        f"❌ 读到的是 {badge_text!r}，应该是 '1'（字符串，带引号）"
    )


def test_C2_读角标并断言(driver):
    """C2：加购 1 件后，写出 2 行：
        第 1 行：把角标文字存进变量 badge_text
        第 2 行：assert 断言 badge_text 等于 "1"

    注意 "1" 要带引号（字符串）。
    """
    登录(driver)
    driver.find_elements(By.CSS_SELECTOR, ADD_TO_CART)[0].click()
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    # ======== 你的代码写在这行下面（2 行）========


    # ======== 自动批改 ========
    assert badge_text == "1", f"❌ badge_text 是 {badge_text!r}，应该是 '1'"


def test_C3_转成数字再断言(driver):
    """C3：加购 1 件后，写出 2 行：
        第 1 行：把角标文字【转成数字】后存进变量 n
        第 2 行：assert 断言 n 等于 1（这次是数字 1，不带引号）

    提示：字符串转数字用 int(...)
    """
    登录(driver)
    driver.find_elements(By.CSS_SELECTOR, ADD_TO_CART)[0].click()
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    # ======== 你的代码写在这行下面（2 行）========


    # ======== 自动批改 ========
    assert n == 1, f"❌ n 是 {n!r}，应该是数字 1"
    assert isinstance(n, int), f"❌ n 的类型是 {type(n).__name__}，应该是 int"


def test_C4_读页面标题(driver):
    """C4：登录后，读出商品列表页上的标题文字（Products），存进 title。

    提示：那个标题元素的 class 是 title
    """
    登录(driver)
    # ======== 你的代码写在这行下面 ========


    # ======== 自动批改 ========
    assert title == "Products", f"❌ 读到的是 {title!r}，应该是 'Products'"


def test_C5_断言在商品页(driver):
    """C5：登录后，写出 2 行：
        第 1 行：把当前网址存进变量 url
        第 2 行：assert 断言 "inventory" 出现在 url 里

    提示：当前网址是 driver.current_url
          "包含" 用 in：  assert "abc" in 某字符串
    """
    登录(driver)
    # ======== 你的代码写在这行下面（2 行）========


    # ======== 自动批改 ========
    assert "inventory" in url, f"❌ url 是 {url!r}，里面应该有 inventory"


# ================================================================
# D 组：综合（4 题）
# ================================================================


def test_D1_加购两件并检查角标(driver):
    """D1：用辅助函数 加购(driver, 2) 加购两件，然后把角标【数字】存进 n。写 2 行。

    提示：加购 2 件直接写  加购(driver, 2)
          读角标转数字：int(角标元素.text)
    """
    登录(driver)
    # ======== 你的代码写在这行下面（2 行）========


    # ======== 自动批改 ========
    assert n == 2, f"❌ 角标数字是 {n!r}，应该是 2"


def test_D2_加购后进入购物车(driver):
    """D2：加购 2 件商品，然后点右上角购物车图标进入购物车页。写 2 行。

    提示：购物车图标的 class 是 shopping_cart_link
    """
    登录(driver)
    # ======== 你的代码写在这行下面（2 行）========
    # 第 1 行：加购(driver, 2)
    # 第 2 行：点购物车图标


    # ======== 自动批改 ========
    # 点完之后网址不会立刻变，所以这里最多等 10 秒再看结果
    from time import sleep
    for _ in range(20):
        if "cart" in driver.current_url:
            break
        sleep(0.5)
    assert "cart" in driver.current_url, (
        f"❌ 没有进入购物车页，当前地址是 {driver.current_url!r}\n"
        f"   提示：点购物车图标用 "
        f'driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()'
    )


def test_D3_断言购物车里有2件(driver):
    """D3：加购 2 件 → 进购物车 → 把购物车里的商品条数存进 n。写 3 行。

    提示：进购物车直接用辅助函数  进购物车(driver)
          （它已经帮你处理了"等页面真的渲染完"这件事）

          购物车里每个"条目"的 class 是 cart_item
    """
    登录(driver)
    # ======== 你的代码写在这行下面（3 行）========
    # 第 1 行：加购(driver, 2)
    # 第 2 行：进购物车(driver)
    # 第 3 行：n = 用 len 数出 cart_item 有几个


    # ======== 自动批改 ========
    assert n == 2, f"❌ 购物车里的条数是 {n!r}，应该是 2"


def test_D4_断言商品名一致(driver):
    """D4（最难）：加购前 2 件 → 进购物车 → 断言两边的商品名完全一致。

    写 5 行：
      1) 把列表页的商品名存进 inventory_names
         （提示：读取文字列表(driver, "inventory_item_name") 再取前两个 [:2]）
      2) 加购(driver, 2)
      3) 进购物车(driver)
      4) 把购物车里的商品名存进 cart_names
      5) assert 断言 inventory_names == cart_names

    ⚠️ 读文字必须用辅助函数 读取文字列表，
       不能直接写 [e.text for e in ...]。
       因为刚跳页面时元素还在渲染，直接读会报
       StaleElementReferenceException（元素已失效）。
    """
    登录(driver)
    # ======== 你的代码写在这行下面（5 行）========


    # ======== 自动批改 ========
    assert inventory_names == cart_names, (
        f"❌ 两边商品名不一致\n   列表页前两件：{inventory_names}\n   购物车里：{cart_names}"
    )
