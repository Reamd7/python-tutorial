"""
第4章：更多控制流工具 - 练习题

本章节练习基于 Python 官方教程第4章：更多控制流工具
参考：https://docs.python.org/zh-cn/3/tutorial/controlflow.html

涵盖内容：
- if 语句
- for 语句和 range() 函数
- break 和 continue 语句
- 函数定义
- 默认参数、关键字参数
- Lambda 表达式
"""


def grade_classifier(score):
    """
    练习 4.1: if 语句 - 成绩分类器
    
    Args:
        score (int): 考试分数 (0-100)
    
    Returns:
        str: 等级 ('A', 'B', 'C', 'D', 'F')
    """
    # TODO: 使用 if-elif-else 实现成绩分类
    # 90-100: A, 80-89: B, 70-79: C, 60-69: D, 0-59: F
    pass


def number_analysis(numbers):
    """
    练习 4.2: for 语句 - 数字列表分析
    
    Args:
        numbers (list): 数字列表
    
    Returns:
        dict: 包含分析结果的字典
    """
    # TODO: 使用 for 循环分析数字列表，返回：
    # 'even_count': 偶数个数
    # 'odd_count': 奇数个数
    # 'positive_count': 正数个数
    # 'negative_count': 负数个数
    # 'zero_count': 零的个数
    pass


def range_experiments():
    """
    练习 4.3: range() 函数实验
    
    Returns:
        dict: 包含不同 range 用法的结果
    """
    # TODO: 返回包含以下键的字典：
    # 'range_10': list(range(10))
    # 'range_5_15': list(range(5, 15))
    # 'range_0_20_2': list(range(0, 20, 2))
    # 'range_20_0_minus2': list(range(20, 0, -2))
    pass


def find_primes(limit):
    """
    练习 4.4: break 和 continue - 素数查找
    
    Args:
        limit (int): 查找素数的上限
    
    Returns:
        list: 小于 limit 的所有素数
    """
    # TODO: 实现素数查找算法
    # 使用 continue 跳过非素数，break 优化内层循环
    pass


def factorial_function(n):
    """
    练习 4.8: 函数定义 - 阶乘计算
    
    Args:
        n (int): 非负整数
    
    Returns:
        int: n 的阶乘
    """
    # TODO: 实现阶乘函数
    # 处理边界情况：0! = 1
    pass


def power_with_default(base, exponent=2):
    """
    练习 4.9.1: 默认参数 - 幂运算
    
    Args:
        base (float): 底数
        exponent (float): 指数，默认为 2
    
    Returns:
        float: base 的 exponent 次方
    """
    # TODO: 实现幂运算函数
    pass


def person_info(name, age, city="未知", **kwargs):
    """
    练习 4.9.2: 关键字参数 - 个人信息
    
    Args:
        name (str): 姓名
        age (int): 年龄
        city (str): 城市，默认为 "未知"
        **kwargs: 其他信息
    
    Returns:
        dict: 包含所有个人信息的字典
    """
    # TODO: 创建包含所有信息的字典并返回
    pass


def apply_operation(numbers, operation):
    """
    练习 4.9.6: Lambda 表达式应用
    
    Args:
        numbers (list): 数字列表
        operation (function): 要应用的操作函数
    
    Returns:
        list: 应用操作后的结果列表
    """
    # TODO: 对列表中的每个数字应用 operation 函数
    pass


def create_multiplier(factor):
    """
    练习 4.9.6: 闭包和 Lambda - 创建乘法器
    
    Args:
        factor (int): 乘法因子
    
    Returns:
        function: 返回一个将输入乘以 factor 的函数
    """
    # TODO: 返回一个 lambda 函数，该函数将输入乘以 factor
    pass


def validate_input(value, min_val=0, max_val=100, value_type=int):
    """
    练习 4.9: 复合参数类型 - 输入验证
    
    Args:
        value: 要验证的值
        min_val: 最小值，默认 0
        max_val: 最大值，默认 100
        value_type: 期望的类型，默认 int
    
    Returns:
        dict: 验证结果 {'valid': bool, 'message': str}
    """
    # TODO: 验证输入值的类型和范围
    pass


def loop_with_else_demo(numbers, target):
    """
    练习 4.5: 循环的 else 子句
    
    Args:
        numbers (list): 数字列表
        target (int): 目标值
    
    Returns:
        dict: 搜索结果
    """
    # TODO: 在列表中查找目标值
    # 使用 for-else 结构
    # 返回 {'found': bool, 'index': int or None, 'message': str}
    pass


def match_statement_demo(value):
    """
    练习 4.7: match 语句（Python 3.10+）
    
    Args:
        value: 要匹配的值
    
    Returns:
        str: 匹配结果描述
    """
    # TODO: 使用 match 语句处理不同类型的值
    # 如果 Python 版本不支持，可以用 if-elif 替代
    pass


if __name__ == "__main__":
    print("第4章：更多控制流工具 - 练习题")
    print("=" * 50)
    
    # 测试成绩分类
    print("4.1 成绩分类测试：")
    test_scores = [95, 87, 72, 65, 45]
    for score in test_scores:
        try:
            grade = grade_classifier(score)
            print(f"分数 {score}: {grade}")
        except:
            print(f"分数 {score}: 函数尚未实现")
    
    # 测试数字分析
    print("\n4.2 数字分析测试：")
    try:
        result = number_analysis([-2, -1, 0, 1, 2, 3, 4, 5])
        print(f"数字分析结果: {result}")
    except:
        print("数字分析函数尚未实现")
    
    # 测试 range 实验
    print("\n4.3 range 实验测试：")
    try:
        result = range_experiments()
        for key, value in result.items():
            print(f"{key}: {value}")
    except:
        print("range 实验函数尚未实现")
    
    # 测试素数查找
    print("\n4.4 素数查找测试：")
    try:
        primes = find_primes(30)
        print(f"小于30的素数: {primes}")
    except:
        print("素数查找函数尚未实现")
    
    # 测试阶乘
    print("\n4.8 阶乘测试：")
    for n in [0, 1, 5, 10]:
        try:
            result = factorial_function(n)
            print(f"{n}! = {result}")
        except:
            print(f"{n}! = 函数尚未实现")
    
    # 测试默认参数
    print("\n4.9.1 默认参数测试：")
    try:
        print(f"power_with_default(3): {power_with_default(3)}")
        print(f"power_with_default(3, 3): {power_with_default(3, 3)}")
    except:
        print("默认参数函数尚未实现")
    
    # 测试 Lambda
    print("\n4.9.6 Lambda 测试：")
    try:
        numbers = [1, 2, 3, 4, 5]
        # 测试平方操作
        squared = apply_operation(numbers, lambda x: x ** 2)
        print(f"平方结果: {squared}")
        
        # 测试乘法器
        times_3 = create_multiplier(3)
        print(f"乘以3的函数: times_3(4) = {times_3(4)}")
    except:
        print("Lambda 相关函数尚未实现")
    
    print("\n请实现上述函数，然后运行 pytest tests/ 验证实现！") 