# Day 1 开工指南

> 你不需要看懂所有东西。今天只有一个目标：**在终端里看到 `2 passed`**。

---

## 一、打开终端（唯一正确的方式）

1. 打开 **VS Code**
2. 菜单 `文件 → 打开文件夹`，选择：
   `C:\Users\19705\Documents\deepseek-harness\default-workspace\ui-auto-test-demo`
3. 按 `` Ctrl + ` ``（键盘左上角 Esc 下面那个键）打开终端

以后所有操作都在这个终端里做。

---

## 二、激活虚拟环境（每次打开终端都要做一次）

```powershell
.\.venv\Scripts\Activate.ps1
```

成功后，命令行最前面会出现 `(.venv)` 字样，像这样：

```
(.venv) PS C:\Users\...\ui-auto-test-demo>
```

> **为什么要这么做？**
> 虚拟环境是给这个项目单独隔离出来的一套 Python 和依赖库。
> 激活之后，你打 `python` 和 `pytest` 才指向正确的版本。
> 不激活的话，`python` 会打开微软商店——这是你这台机器现在的一个坑。

**如果报错「禁止运行脚本」**，执行下面这行，然后重新激活（只需要做一次）：

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

---

### ⚠️ 三种终端，命令不一样（新手最容易卡在这里）

先看你终端提示符长什么样：

| 终端类型 | 提示符样子 | 激活命令 |
|---|---|---|
| **PowerShell**（推荐） | `PS C:\...>` | `.\.venv\Scripts\Activate.ps1` |
| **CMD**（黑框） | `C:\...>` | `.venv\Scripts\activate.bat` |

> **判断口诀**：提示符以 `PS` 开头就是 PowerShell，用 `.ps1`；
> 不是 `PS` 开头就是 CMD，用 `.bat`。
> **两个命令不能混用**——在 CMD 里敲 `.ps1` 一定会失败，这就是最常见的"运行失败"。

**改默认终端为 PowerShell**：VS Code 里按 `Ctrl+Shift+P` → 输入
`Terminal: Select Default Profile` → 选 `PowerShell`。

---

### 🚑 终极防呆：双击就能跑

实在搞不定终端，直接用这个——**双击项目根目录下的 `run_tests.bat`**。

它会自动激活环境并运行测试，跑完窗口不会关，你能看到结果。
报告在 `reports\report.html`，双击就能用浏览器打开。

---

## 三、验证环境

```powershell
python --version
pytest
```

`python --version` 应该输出 `Python 3.14.3`。

`pytest` 应该输出：

```
tests/test_smoke.py::test_environment_is_ready PASSED
tests/test_smoke.py::test_python_version_is_modern PASSED
============================== 2 passed in 0.08s ==============================
```

看到 `2 passed`，你今天的环境任务就完成了。
同时 `reports\report.html` 会被生成——用浏览器打开它，这就是你未来要展示给面试官的"测试报告"的雏形。

---

## 四、今天真正要学的（别跳过）

环境是别人（我）帮你搭的，但**代码必须你自己敲**。今天做这三件事：

### 1. 手敲第一个脚本
在项目根目录新建 `day01.py`，自己敲一遍（不要复制粘贴）：

```python
# 我的第一个 Python 脚本
name = "我的名字"          # 改成你自己的名字
days = 30

print("你好，" + name)
print("我要用", days, "天拿到实习 offer")

# 循环：把每天的计划打印出来
for day in range(1, 6):
    print("第", day, "天：继续学")

# 条件判断
if days >= 30:
    print("时间够用")
else:
    print("时间紧张，要加速")
```

运行它：

```powershell
python day01.py
```

### 2. 把它改坏，再看报错
把 `days = 30` 改成 `days = "三十"`，再运行一次，**认真读那段红色的报错信息**。

> 读报错是程序员最重要的技能，比背语法重要。面试官不在乎你写不出 bug，在乎你能不能自己定位问题。

### 3. 加一条你自己的测试
打开 `tests/test_smoke.py`，在最后加一个函数：

```python
def test_my_first_case():
    """我自己写的第一条用例。"""
    assert "hello".upper() == "HELLO"
```

再跑一次 `pytest`，应该变成 `3 passed`。

---

## 五、今天结束前要做的事

```powershell
git add .
git commit -m "Day1: 环境搭建与第一个脚本"
```

> Git 目前还没装好。等装完之后，这条命令会成为你之后 30 天里**每天必做**的事。
> 你 GitHub 仓库里那 30 条提交记录，就是面试时唯一无法造假的证据。

---

## 六、今天不许做的事

- ❌ 不要去看"Python 从入门到精通"的完整教程，会淹死你
- ❌ 不要装一堆用不上的东西
- ❌ 不要因为报错就怀疑自己——今天你一定会遇到至少 3 个报错，这是正常的

---

## 卡住了怎么办

把**完整的报错信息**复制给我（不要只说"报错了"）。
我会告诉你：这个错在说什么、为什么会发生、怎么改、以及面试会怎么问它。
