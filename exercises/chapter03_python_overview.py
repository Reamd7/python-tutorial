"""
第3章：Python 速览 - 练习题

本章节练习基于 Python 官方教程第3章：Python 速览
参考：https://docs.python.org/zh-cn/3/tutorial/introduction.html

涵盖内容：
- Python 用作计算器（数字运算）
- 文本处理（字符串操作）
- 列表操作
- 编程第一步
"""


def calculator_basic_math(a, b) -> dict[str, float | None]:
    """
    练习 3.1.1: 基础数学运算
    
    Args:
        a (float): 第一个数字
        b (float): 第二个数字
    
    Returns:
        dict: 包含加减乘除结果的字典
    """
    # TODO: 返回包含 'add', 'subtract', 'multiply', 'divide' 键的字典
    return {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b if b != 0 else None,
    }


def calculator_power_and_modulo(base: int, exponent: int, divisor: int) -> dict[str, int | None]:
    """
    练习 3.1.1: 幂运算和取模运算
    
    Args:
        base (int): 底数
        exponent (int): 指数
        divisor (int): 除数
    
    Returns:
        dict: 包含幂运算和取模结果的字典
    """
    # TODO: 返回包含 'power', 'modulo' 键的字典
    return {
        'power': base ** exponent,
        'modulo': base % divisor if divisor != 0 else None,
    }


def string_concatenation_and_repetition(text: str, times: int) -> dict[str, str | int]:
    """
    练习 3.1.2: 字符串连接和重复
    
    Args:
        text (str): 要处理的字符串
        times (int): 重复次数
    
    Returns:
        dict: 包含处理结果的字典
    """
    # TODO: 返回包含 'repeated', 'length' 键的字典
    # repeated: 字符串重复 times 次
    # length: 重复后字符串的长度
    repeated = text * times
    return {
        'repeated': repeated,
        'length': len(repeated),
    }


def string_indexing_and_slicing(text: str) -> dict[str, str]:
    """
    练习 3.1.2: 字符串索引和切片
    
    Args:
        text (str): 要处理的字符串
    
    Returns:
        dict: 包含各种索引和切片结果的字典
    """
    # TODO: 返回包含以下键的字典：
    # 'first_char': 第一个字符
    # 'last_char': 最后一个字符
    # 'first_three': 前三个字符
    # 'last_three': 后三个字符
    # 'reverse': 反转的字符串
    return {
        'first_char': text[0],
        'last_char': text[-1],
        'first_three': text[:3],
        'last_three': text[-3:],
        'reverse': text[::-1],
    }


def list_operations(numbers: list[int]) -> dict[str, int | float | list[int]]:
    """
    练习 3.1.3: 列表基础操作
    
    Args:
        numbers (list): 数字列表
    
    Returns:
        dict: 包含列表操作结果的字典
    """
    # TODO: 返回包含以下键的字典：
    # 'length': 列表长度
    # 'sum': 列表元素之和
    # 'max': 最大值
    # 'min': 最小值
    # 'reversed': 反转的列表
    length = len(numbers)
    return {
        'length': length,
        'sum': sum(numbers),
        'max': max(numbers) if length > 0 else None,
        'min': min(numbers) if length > 0 else None,
        'reversed': numbers[::-1],
    }


def list_methods_demo(original_list: list[int]) -> dict[str, list[int]]:
    """
    练习 3.1.3: 列表方法演示
    
    Args:
        original_list (list): 原始列表
    
    Returns:
        dict: 演示各种列表方法的结果
    """
    # TODO: 对列表副本进行操作，返回包含以下键的字典：
    # 'appended': 添加元素 100 后的列表
    # 'extended': 扩展 [200, 300] 后的列表
    # 'inserted': 在索引 1 处插入 50 后的列表
    # 'sorted': 排序后的列表
    appended = original_list.copy()
    appended.append(100)
    extended = original_list.copy()
    extended.extend([200, 300])
    inserted = original_list.copy()
    inserted.insert(1, 50)
    sorted = original_list.copy()
    sorted.sort()
    return {
        'appended': appended,
        'extended': extended,
        'inserted': inserted,
        'sorted': sorted,
    }

def fibonacci_sequence(n):
    """
    练习 3.2: 编程第一步 - 斐波那契数列
    
    根据官方教程中的斐波那契例子，生成斐波那契数列
    
    Args:
        n (int): 生成数列的最大值（不超过此值）
    
    Returns:
        list: 不超过 n 的斐波那契数列
    """
    # TODO: 实现斐波那契数列生成
    # 提示：a, b = 0, 1
    # 使用 while 循环，当 a < n 时继续
    if n <= 0:
        return []
    if n == 1:
        return [0, 1]

    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b 
    return result


def print_number_series(start, end, step=1):
    """
    练习 3.2: 打印数字序列
    
    Args:
        start (int): 起始数字
        end (int): 结束数字（不包含）
        step (int): 步长
    
    Returns:
        list: 数字序列列表
    """
    # TODO: 生成从 start 到 end（不包含）步长为 step 的数字列表
    return list(range(start, end, step))


def string_formatting_demo(name: str, age: int, score: float) -> dict[str, str]:
    """
    练习 3.1.2: 字符串格式化
    
    Args:
        name (str): 姓名
        age (int): 年龄
        score (float): 分数
    
    Returns:
        dict: 包含不同格式化方法的字符串
    """
    # TODO: 返回包含以下键的字典：
    # 'f_string': 使用 f-string 格式化
    # 'format_method': 使用 .format() 方法
    # 'percent_style': 使用 % 格式化（如果你了解的话）
    # 格式："{name}今年{age}岁，考试得了{score:.1f}分"
    f_string = f"{name}今年{age}岁，考试得了{score:.1f}分"
    format_method = "{name}今年{age}岁，考试得了{score:.1f}分".format(name=name, age=age, score=score)
    percent_style = "%s今年%d岁，考试得了%.1f分" % (name, age, score)
    return {
        'f_string': f_string,
        'format_method': format_method,
        'percent_style': percent_style,
    }


if __name__ == "__main__":
    print("第3章：Python 速览 - 练习题")
    print("=" * 40)
    
    # 测试计算器功能
    print("3.1.1 数字运算测试：")
    try:
        result = calculator_basic_math(10, 3)
        print(f"基础运算结果: {result}")
    except:
        print("基础运算函数尚未实现")
    
    # 测试字符串操作
    print("\n3.1.2 字符串操作测试：")
    try:
        result = string_indexing_and_slicing("Python")
        print(f"字符串操作结果: {result}")
    except:
        print("字符串操作函数尚未实现")
    
    # 测试列表操作
    print("\n3.1.3 列表操作测试：")
    try:
        result = list_operations([1, 4, 9, 16, 25])
        print(f"列表操作结果: {result}")
    except:
        print("列表操作函数尚未实现")
    
    # 测试斐波那契数列
    print("\n3.2 斐波那契数列测试：")
    try:
        result = fibonacci_sequence(100)
        print(f"斐波那契数列(< 100): {result}")
    except:
        print("斐波那契函数尚未实现")
    
    print("\n请实现上述函数，然后运行 pytest tests/ 验证实现！") 