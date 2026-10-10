# Selenium 最小知识卡

> **自动化测试里 99% 的代码，就是下面这 5 个动作的组合。**
> 背下来这 5 条，你就能读懂项目里所有的代码，也能自己写。

---

## 动作 1：找一个元素

```python
元素 = self.driver.find_element(用什么方式, "找什么")
```

**真实例子：**

```python
box = self.driver.find_element(By.ID, "user-name")
```

- 找到 → 返回**一个**元素
- **找不到 → 直接报错 `NoSuchElementException`**

---

## 动作 2：找一堆元素

```python
元素列表 = self.driver.find_elements(用什么方式, "找什么")
```

**真实例子：**

```python
buttons = self.driver.find_elements(By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
```

- 找到几个 → 返回**一个列表**，装了几个元素
- **找不到 → 返回空列表 `[]`（不报错！）**

> 📌 **这是最重要的区别**：
> 想判断"元素**不存在**"，必须用复数形式，否则程序直接崩溃。

---

## 动作 3：对元素做动作

对一个元素，你只会做 3 件事：

| 写法 | 意思 |
|---|---|
| `元素.click()` | **点击** |
| `元素.send_keys("文字")` | **输入文字** |
| `元素.clear()` | **清空输入框** |

**真实例子：**

```python
login_button.click()                    # 点登录按钮
username_box.send_keys("standard_user") # 在框里打字
username_box.clear()                    # 把框清空
```

---

## 动作 4：读元素的信息

| 写法 | 拿到什么 |
|---|---|
| `元素.text` | 元素上**显示的文字**（⚠️ **永远是字符串**） |
| `元素.get_attribute("id")` | 某个**属性的值** |

**真实例子：**

```python
badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
print(badge.text)          # "2"   ← 注意是字符串，不是数字 2
print(badge.get_attribute("class"))   # "shopping_cart_badge"
```

> 📌 **第二重要的坑**：`.text` 读回来**永远是字符串**。
> 页面上显示 `2`，读回来是 `"2"`。要当数字用，得 `int("2")`。

---

## 动作 5：返回

```python
return self       # 返回"页面对象"自己 → 这样可以链式调用
return 值          # 返回一个数据
```

**链式调用长这样：**

```python
login_page.login("a", "b").open_cart()      # ← 因为 login() 返回了 self
```

因为每个方法最后都 `return self`，所以可以一直往后接。

---

# 最后一块拼图：那个 `*` 是什么

你会看到代码里这样写：

```python
self.driver.find_element(*self.CART_LINK)
#                      ↑ 这个星号
```

## 拆开看就懂了

定位器是一个**元组**，里面装了两个东西：

```python
CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
#            ~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~~~~
#             第 1 个             第 2 个
```

而 `find_element` 需要**两个参数**：

```python
find_element(第1个, 第2个)
```

所以有两种写法，**效果完全一样**：

```python
# 写法一：手动拆开
self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")

# 写法二：用 * 自动拆开（推荐，改定位器时只改一处）
self.driver.find_element(*self.CART_LINK)
```

> **`*` 的意思就是"把这个元组拆成一个个参数，分别传进去"。**
> 记住这句话就够了，不用深究。

---

# 自查：现在你应该能读懂这行代码

```python
self.driver.find_element(*self.CHECKOUT_BUTTON).click()
```

**逐段翻译：**

| 片段 | 意思 |
|---|---|
| `self.driver` | 用这个页面对象持有的浏览器 |
| `.find_element(...)` | 找一个元素 |
| `*self.CHECKOUT_BUTTON` | 用结账按钮的定位器去找（`*` 把元组拆开） |
| `.click()` | 点它 |

**连起来：找到结账按钮，点一下。**

---

# 五分钟小测（做完再往下）

不看上面，自己说出下面这行的意思：

```python
count = len(self.driver.find_elements(*self.CART_ITEM))
```

<details>
<summary>点开看答案</summary>

1. `self.driver.find_elements(*self.CART_ITEM)` → 用购物车条目的定位器，找出**所有**条目，返回一个列表
2. `len(...)` → 数这个列表里有几个
3. `count = ` → 把数字存进变量 `count`

**连起来：数一数购物车里有几件商品。**
</details>
