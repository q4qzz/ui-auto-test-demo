# ui-auto-test-demo

基于 pytest + Selenium 的 Web UI 自动化测试项目，被测对象为公开测试练习站点
[Sauce Demo](https://www.saucedemo.com)。

本项目用于系统练习软件测试的完整流程：**测试用例设计 → 手工测试 → 自动化实现 → 测试报告 → 持续集成**。

---

## 项目目标

| 阶段 | 产出 |
|---|---|
| 测试设计 | 30+ 条测试用例，覆盖等价类、边界值、判定表、场景法 |
| 自动化实现 | 基于 PO（Page Object）分层的可维护测试框架 |
| 测试报告 | 自动生成 HTML 测试报告，失败自动截图 |
| 持续集成 | GitHub Actions 每次提交自动执行全量用例 |
| 接口测试 | 基于 requests 的接口自动化用例 |

---

## 技术栈

| 分类 | 选型 |
|---|---|
| 语言 | Python 3.14 |
| 测试框架 | pytest |
| Web 自动化 | Selenium 4 |
| 接口测试 | requests |
| 报告 | pytest-html |
| 测试数据 | Faker |
| 浏览器 | Microsoft Edge |
| 持续集成 | GitHub Actions |

---

## 目录结构

```
ui-auto-test-demo/
├── pages/              # 页面对象（PO 模式），只放元素定位和页面操作
├── tests/              # 测试用例，只放断言和业务逻辑
├── data/               # 测试数据
├── docs/               # 文档：测试用例表、缺陷报告、开工指南
├── reports/            # 测试报告（运行后自动生成，不提交仓库）
├── pytest.ini          # pytest 配置
└── requirements.txt    # 依赖清单
```

---

## 环境准备与运行

```powershell
# 1. 进入项目目录
cd ui-auto-test-demo

# 2. 激活虚拟环境（每次打开终端都要执行）
.\.venv\Scripts\Activate.ps1

# 3. 安装依赖（如果换了一台机器）
pip install -r requirements.txt

# 4. 运行全部测试
pytest
```

运行结束后，打开 `reports/report.html` 查看测试报告。

---

## 测试用例设计

用例设计文档见 `docs/`，覆盖的测试类型包括：

- **等价类划分**：登录用户名/密码的合法与非法输入
- **边界值分析**：密码长度、商品数量、金额的边界
- **场景法**：完整下单流程（登录 → 加购 → 结算 → 下单成功）
- **错误推测**：SQL 注入式输入、空输入、超长输入

---

## 作者

（待填写）

---

## 更新记录

- **Day 1**：项目初始化，环境搭建完成，冒烟测试通过
