# Python 现代开发教程

这是一个全面的 Python 语言学习教程，使用 `uv` 构建，涵盖从基础语法到现代Python特性的完整内容。专注于Python语言本身的掌握，特别适合想要深入理解现代Python语言特性的学习者。

## 🌟 特色亮点

- **📚 完整覆盖**: Python 官方教程 + 现代开发特性
- **🎯 实践导向**: 每个概念都有对应的练习和测试
- **🧪 测试驱动**: 超过 600+ 测试用例确保学习质量
- **📝 交互式学习**: Jupyter notebooks 支持
- **⚡ 现代工具**: 使用 uv 包管理器，支持 Python 3.13

## 🚀 快速开始

### 1. 环境准备

```bash
# 确保已安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 克隆项目
git clone <your-repo-url>
cd python-tutorial

# 安装依赖并激活环境
uv sync
```

### 2. 开始学习

```bash
# 查看基础练习
uv run python exercises/basic_exercises.py

# 运行所有测试
uv run pytest tests/ -v

# 启动 Jupyter Notebook
uv run jupyter notebook
```

## 📁 完整项目结构

```
python-tutorial/
├── exercises/                          # 练习代码目录 (3000+ 行代码)
│   ├── basic_exercises.py             # 基础练习题
│   │
│   # === Python 官方教程章节 ===
│   ├── chapter03_python_overview.py   # 第3章：Python 速览
│   ├── chapter04_control_flow.py      # 第4章：更多控制流工具
│   ├── chapter05_data_structures.py   # 第5章：数据结构
│   ├── chapter06_modules.py           # 第6章：模块
│   ├── chapter07_input_output.py      # 第7章：输入与输出
│   ├── chapter08_errors_exceptions.py # 第8章：错误和异常
│   ├── chapter09_classes.py           # 第9章：类
│   ├── chapter10_standard_library.py  # 第10章：标准库简介
│   ├── chapter11_standard_library2.py # 第11章：标准库简介——第二部分
│   │
│   # === 现代 Python 特性 ===
│   ├── chapter12_async_programming.py     # 第12章：异步编程 (Asyncio)
│   ├── chapter13_type_hints.py           # 第13章：类型提示
│   ├── chapter14_dataclasses.py          # 第14章：数据类
│   ├── chapter15_advanced_decorators.py  # 第15章：高级装饰器
│   ├── chapter16_threading_multiprocessing.py # 第16章：并发编程
│   └── chapter17_pytest_testing.py       # 第17章：Pytest 测试框架
│
├── tests/                              # 测试目录 (2500+ 行测试代码)
│   ├── test_basic_exercises.py
│   ├── test_chapter03_python_overview.py
│   ├── test_chapter04_control_flow.py
│   ├── test_chapter05_data_structures.py
│   ├── test_chapter06_modules.py
│   ├── test_chapter07_input_output.py
│   ├── test_chapter08_errors_exceptions.py
│   ├── test_chapter09_classes.py
│   ├── test_chapter10_standard_library.py
│   ├── test_chapter11_standard_library2.py
│   ├── test_chapter12_async_programming.py
│   ├── test_chapter13_type_hints.py
│   ├── test_chapter14_dataclasses.py
│   ├── test_chapter15_advanced_decorators.py
│   ├── test_chapter16_threading_multiprocessing.py
│   └── test_chapter17_pytest_testing.py
│
├── notebooks/                          # 交互式学习材料
│   ├── chapter03_python_overview.ipynb
│   ├── chapter04_control_flow.ipynb
│   ├── chapter05_data_structures.ipynb
│   ├── chapter09_classes.ipynb
│   ├── chapter11_standard_library2.ipynb
│   ├── chapter12_async_programming.ipynb  # 异步编程演示
│   ├── chapter13_type_hints.ipynb        # 类型提示实践
│   ├── chapter14_dataclasses.ipynb       # 数据类使用
│   ├── chapter15_advanced_decorators.ipynb # 装饰器模式
│   ├── chapter16_threading_multiprocessing.ipynb # 并发编程
│   └── chapter17_pytest_testing.ipynb    # 测试实践
│
├── pyproject.toml                      # 项目配置和依赖
├── uv.lock                            # 依赖锁定文件
└── README.md                          # 本文档
```

## 📚 学习内容概览

### 🎯 基础篇 (第3-11章) - Python官方教程
基于 [Python 官方教程](https://docs.python.org/zh-cn/3/tutorial/index.html) 的完整实现：

#### 第3章：Python 速览
- 计算器功能和数学运算
- 字符串操作和格式化
- 列表基础操作
- 基础输入输出

#### 第4章：更多控制流工具  
- `if`/`elif`/`else` 条件语句
- `for` 和 `while` 循环
- `break`、`continue` 和 `else` 子句
- 函数定义、参数和作用域
- Lambda 表达式
- `match` 语句 (Python 3.10+)

#### 第5章：数据结构
- 列表方法和列表推导式
- 元组和序列
- 集合和字典
- 循环技巧和 `del` 语句

#### 第6章：模块
- 模块的创建和导入
- 包的概念和使用
- `from...import` 语句
- 模块搜索路径

#### 第7章：输入与输出
- 格式化输出和 f-strings
- 文件读写操作
- JSON 和 CSV 处理
- `pathlib` 路径操作

#### 第8章：错误和异常
- 异常处理基础
- `try`/`except`/`finally`
- 自定义异常类
- 异常链和上下文

#### 第9章：类
- 面向对象编程基础
- 类定义和实例化
- 继承和多态
- 特殊方法和运算符重载

#### 第10-11章：标准库
- 常用标准库模块
- 文件系统操作
- 数据处理和格式化
- 网络和并发模块

### 🚀 现代篇 (第12-17章) - 现代Python特性

#### 第12章：异步编程 (Asyncio) ⭐
- `async`/`await` 语法基础
- 协程和事件循环
- 并发任务管理
- 异步HTTP请求和文件操作
- 异步上下文管理器和生成器

**关键概念**: 异步编程、事件驱动、非阻塞IO

#### 第13章：类型提示 (Type Hints) ⭐  
- 基础类型注解语法
- `Optional`、`Union`、泛型
- `Protocol` 和结构化类型
- `TypedDict` 和字面量类型
- 静态类型检查 (mypy)

**关键概念**: 类型安全、IDE支持、代码可维护性

#### 第14章：数据类 (Dataclasses) ⭐
- `@dataclass` 装饰器
- 字段定义和默认值
- 数据验证和后处理
- 不可变数据类 (`frozen=True`)
- JSON序列化和反序列化

**关键概念**: 减少样板代码、数据容器、现代类设计

#### 第15章：高级装饰器 ⭐
- 装饰器工厂和参数化装饰器
- 性能监控和缓存装饰器
- 认证和权限控制装饰器
- 类装饰器和异步装饰器
- 装饰器组合和链式应用

**关键概念**: 元编程、横切关注点、代码复用

#### 第16章：线程和多进程 ⭐
- 多线程编程和线程同步
- 多进程编程和进程间通信
- 线程池和进程池
- 性能优化和并发模式
- GIL 和并发策略选择

**关键概念**: 并发编程、性能优化、系统资源利用

#### 第17章：Pytest 测试框架 ⭐
- pytest 基础用法和夹具系统
- 参数化测试和标记过滤
- Mock 和异步测试
- 测试覆盖率和性能测试
- 测试驱动开发 (TDD)

**关键概念**: 测试驱动开发、代码质量、持续集成

## 🎯 学习路径推荐

### 📈 按经验水平

#### 🌱 初学者路径 (4-6周)
1. **基础语法** → `basic_exercises.py`
2. **Python速览** → `chapter03_python_overview.py`
3. **控制流** → `chapter04_control_flow.py`
4. **数据结构** → `chapter05_data_structures.py`

#### 🌿 中级开发者路径 (3-4周)
1. **模块和包** → `chapter06_modules.py`
2. **文件操作** → `chapter07_input_output.py`
3. **异常处理** → `chapter08_errors_exceptions.py`
4. **面向对象** → `chapter09_classes.py`

#### 🌳 高级开发者路径 (4-5周)
1. **标准库** → `chapter10_standard_library.py`, `chapter11_standard_library2.py`
2. **异步编程** → `chapter12_async_programming.py` ⭐
3. **类型提示** → `chapter13_type_hints.py` ⭐
4. **现代特性** → `chapter14_dataclasses.py`, `chapter15_advanced_decorators.py` ⭐

#### 🏆 专业开发者路径 (2-3周)
1. **并发编程** → `chapter16_threading_multiprocessing.py` ⭐
2. **测试框架** → `chapter17_pytest_testing.py` ⭐
3. **项目实战** → 结合所学知识完成实际项目

### 💼 按学习重点

#### 🎯 语言基础强化
重点学习: 语法、数据结构、面向对象
```
chapter03 → chapter04 → chapter05 → chapter09
```

#### 🔧 工程实践技能
重点学习: 模块组织、异常处理、测试框架
```
chapter06 → chapter08 → chapter17 → chapter07
```

#### ⚡ 现代Python特性
重点学习: 异步编程、类型提示、装饰器、数据类
```
chapter12 → chapter13 → chapter15 → chapter14
```

#### 🚀 高级编程技能
重点学习: 并发编程、高级装饰器、测试框架
```
chapter16 → chapter15 → chapter17 → chapter13
```

## 🔧 开发工具和依赖

### 核心工具
- **Python 3.13** - 最新Python版本
- **uv** - 现代包管理器
- **pytest** - 现代测试框架
- **mypy** - 静态类型检查器

### 开发库
- **aiohttp** - 异步HTTP客户端
- **aiofiles** - 异步文件操作
- **typing-extensions** - 扩展类型提示

### 学习工具  
- **jupyter** - 交互式notebook环境
- **ipython** - 增强的Python shell

## 💡 实践建议

### 1. 测试驱动学习
每完成一个练习，立即运行对应测试：
```bash
# 单个章节测试
uv run pytest tests/test_chapter12_async_programming.py -v

# 全部测试
uv run pytest tests/ -v

# 查看测试覆盖率
uv run pytest --cov=exercises tests/
```

### 2. 交互式探索
使用 Jupyter notebook 进行实验：
```bash
# 启动 Jupyter
uv run jupyter notebook

# 打开对应章节的 notebook
# 例如：notebooks/chapter12_async_programming.ipynb
```

### 3. 类型检查
对于现代Python特性章节，使用 mypy 进行类型检查：
```bash
# 检查特定文件
uv run mypy exercises/chapter13_type_hints.py

# 检查所有练习文件
uv run mypy exercises/
```

### 4. 代码格式化
保持代码风格一致：
```bash
# 安装格式化工具
uv add black isort

# 格式化代码
uv run black exercises/
uv run isort exercises/
```

## 🎓 学习成果

完成本教程后，你将掌握：

### 基础能力
- ✅ Python 语法和标准库
- ✅ 面向对象编程
- ✅ 错误处理和调试

### 现代开发技能  
- ✅ 异步编程和并发处理
- ✅ 类型安全编程
- ✅ 测试驱动开发
- ✅ 现代代码组织模式

### 实战技能
- ✅ 现代Python语言特性运用
- ✅ 代码质量控制和测试
- ✅ 并发和异步编程实践
- ✅ 高质量代码组织和设计

## 📊 项目统计

- **📝 练习代码**: 17个章节，3000+ 行实践代码
- **🧪 测试覆盖**: 17个测试文件，600+ 测试用例  
- **📚 学习资料**: 15个交互式 notebook
- **⭐ 现代特性**: 6个现代Python特性专题
- **🎯 学习目标**: Python语言精通、现代开发技能、代码质量提升

## 🤝 贡献指南

欢迎改进和扩展此教程！

1. **添加练习**: 在对应章节文件中添加新练习
2. **编写测试**: 确保新练习有对应的测试用例
3. **更新文档**: 在 README 中记录新内容
4. **质量检查**: 运行测试和类型检查确保质量

```bash
# 运行完整检查
uv run pytest tests/ -v
uv run mypy exercises/
```

## 📞 支持和反馈

- 🐛 发现问题？请提交 Issue
- 💡 有建议？欢迎 Pull Request  
- 📧 需要帮助？联系维护者

---

## 🎉 开始你的现代Python学习之旅！

选择适合你的学习路径，从基础语法到现代开发特性，一步步成为Python专家！

**推荐开始方式**:
```bash
# 1. 运行基础练习熟悉环境
uv run python exercises/basic_exercises.py

# 2. 查看测试了解预期结果
uv run pytest tests/test_basic_exercises.py -v

# 3. 选择你感兴趣的现代特性章节
uv run jupyter notebook notebooks/chapter12_async_programming.ipynb
```

**快乐编程！🐍✨**
