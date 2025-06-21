"""
第8章：错误和异常 - 练习题

本章节练习基于 Python 官方教程第8章：错误和异常
参考：https://docs.python.org/zh-cn/3/tutorial/errors.html

涵盖内容：
- 语法错误与异常
- 处理异常
- 抛出异常
- 用户自定义异常
- 定义清理操作
- 预定义的清理操作
"""

import sys
import traceback
from pathlib import Path


class CustomError(Exception):
    """自定义异常基类"""
    pass


class ValidationError(CustomError):
    """验证错误异常"""
    def __init__(self, message, field=None):
        super().__init__(message)
        self.field = field


class CalculationError(CustomError):
    """计算错误异常"""
    def __init__(self, message, operation=None, operands=None):
        super().__init__(message)
        self.operation = operation
        self.operands = operands


def basic_exception_handling(numbers):
    """
    练习 8.3: 基本异常处理
    
    Args:
        numbers (list): 数字列表，可能包含各种类型
    
    Returns:
        dict: 异常处理的结果
    """
    # TODO: 处理各种可能的异常，返回：
    # 'results': 成功处理的数字结果列表
    # 'errors': 遇到的错误信息列表
    # 'type_errors': TypeError 的数量
    # 'value_errors': ValueError 的数量  
    # 'zero_division_errors': ZeroDivisionError 的数量
    # 'other_errors': 其他错误的数量
    
    # 对每个数字尝试以下操作：
    # 1. 转换为 float
    # 2. 计算平方根
    # 3. 除以 (数字-5)
    pass


def multiple_exception_types(data):
    """
    练习 8.3: 处理多种异常类型
    
    Args:
        data (list): 混合数据列表
    
    Returns:
        dict: 处理结果和异常统计
    """
    # TODO: 处理多种异常类型，对每个数据项：
    # 1. 尝试转换为 int
    # 2. 尝试访问字典的 'value' 键
    # 3. 尝试调用 upper() 方法
    # 
    # 返回：
    # 'successful_operations': 成功操作的数量
    # 'type_error_count': TypeError 数量
    # 'key_error_count': KeyError 数量
    # 'attribute_error_count': AttributeError 数量
    # 'value_error_count': ValueError 数量
    # 'error_details': 每个错误的详细信息列表
    pass


def exception_propagation_demo():
    """
    练习 8.3: 异常传播演示
    
    Returns:
        dict: 异常传播的演示结果
    """
    def level_3():
        raise ValueError("这是来自第3层的错误")
    
    def level_2():
        level_3()
    
    def level_1():
        level_2()
    
    # TODO: 演示异常传播，返回：
    # 'caught_at_level_1': 在 level_1 捕获异常的结果
    # 'caught_at_level_2': 在 level_2 捕获异常的结果  
    # 'caught_at_top': 在顶层捕获异常的结果
    # 'traceback_info': 异常的回溯信息
    # 'exception_type': 异常的类型名称
    pass


def try_except_else_finally_demo(filename="test_file.txt"):
    """
    练习 8.4, 8.7: try-except-else-finally 完整演示
    
    Args:
        filename (str): 要操作的文件名
    
    Returns:
        dict: 各个子句的执行结果
    """
    # TODO: 演示完整的异常处理结构，返回：
    # 'try_executed': try 子句是否执行
    # 'except_executed': except 子句是否执行
    # 'else_executed': else 子句是否执行  
    # 'finally_executed': finally 子句是否执行
    # 'file_content': 文件内容（如果成功读取）
    # 'error_message': 错误信息（如果有）
    # 'cleanup_performed': 清理操作是否执行
    pass


def raise_exception_examples():
    """
    练习 8.4: 抛出异常示例
    
    Returns:
        dict: 抛出异常的各种方式
    """
    # TODO: 演示抛出异常的不同方式，返回：
    # 'raise_simple': 抛出简单异常的结果
    # 'raise_with_message': 带消息抛出异常的结果
    # 'raise_custom': 抛出自定义异常的结果
    # 'reraise_exception': 重新抛出异常的结果
    # 'raise_from': 使用 raise...from 的结果
    pass


def custom_exception_usage():
    """
    练习 8.5: 自定义异常的使用
    
    Returns:
        dict: 自定义异常的使用示例
    """
    # TODO: 使用自定义异常，返回：
    # 'validation_error': ValidationError 的使用示例
    # 'calculation_error': CalculationError 的使用示例
    # 'exception_hierarchy': 异常继承层次的演示
    # 'exception_attributes': 异常自定义属性的使用
    
    # 示例场景：
    # 1. 验证用户输入（年龄、邮箱等）
    # 2. 数学计算错误（除零、平方根负数等）
    # 3. 业务逻辑错误
    pass


def exception_chaining_demo():
    """
    练习 8.4: 异常链演示
    
    Returns:
        dict: 异常链的演示结果
    """
    # TODO: 演示异常链，返回：
    # 'original_exception': 原始异常信息
    # 'chained_exception': 链接的异常信息
    # 'suppressed_exception': 抑制的异常信息
    # 'chain_details': 异常链的详细信息
    
    # 演示场景：
    # 1. 在处理一个异常时抛出另一个异常
    # 2. 使用 raise...from 显式链接异常
    # 3. 在 finally 中抛出异常（抑制原异常）
    pass


def context_manager_with_exceptions():
    """
    练习 8.7: 上下文管理器与异常
    
    Returns:
        dict: 上下文管理器处理异常的演示
    """
    class MyContextManager:
        def __enter__(self):
            return "资源已获取"
        
        def __exit__(self, exc_type, exc_value, traceback):
            # TODO: 实现异常处理逻辑
            pass
    
    # TODO: 演示上下文管理器如何处理异常，返回：
    # 'normal_execution': 正常执行的结果
    # 'exception_suppressed': 异常被抑制的结果  
    # 'exception_not_suppressed': 异常未被抑制的结果
    # 'cleanup_executed': 清理操作是否执行
    pass


def exception_performance_test():
    """
    练习 8: 异常性能测试
    
    Returns:
        dict: 异常对性能的影响测试
    """
    import time
    
    # TODO: 测试异常对性能的影响，返回：
    # 'normal_operation_time': 正常操作的时间
    # 'exception_operation_time': 包含异常处理的时间
    # 'performance_ratio': 性能比率
    # 'recommendations': 性能优化建议
    
    # 测试场景：
    # 1. 大量正常操作 vs 大量异常操作
    # 2. EAFP vs LBYL 模式的性能对比
    pass


def defensive_programming_examples():
    """
    练习 8: 防御性编程示例
    
    Returns:
        dict: 防御性编程的示例
    """
    # TODO: 演示防御性编程技巧，返回：
    # 'input_validation': 输入验证的示例
    # 'type_checking': 类型检查的示例
    # 'boundary_checking': 边界检查的示例
    # 'resource_management': 资源管理的示例
    # 'error_recovery': 错误恢复的示例
    pass


def exception_best_practices():
    """
    练习 8: 异常处理最佳实践
    
    Returns:
        dict: 异常处理的最佳实践示例
    """
    # TODO: 演示异常处理最佳实践，返回：
    # 'specific_exceptions': 捕获特定异常而非通用异常
    # 'exception_logging': 异常日志记录
    # 'graceful_degradation': 优雅降级处理
    # 'user_friendly_messages': 用户友好的错误消息
    # 'cleanup_resources': 资源清理
    # 'dont_ignore_exceptions': 不忽略异常的重要性
    pass


def advanced_exception_features():
    """
    练习 8: 高级异常特性
    
    Returns:
        dict: 高级异常特性的演示
    """
    # TODO: 演示高级异常特性，返回：
    # 'exception_groups': 异常组（Python 3.11+）
    # 'exception_notes': 异常注释
    # 'traceback_manipulation': 回溯信息操作
    # 'custom_traceback': 自定义回溯格式
    # 'exception_hooks': 异常钩子的使用
    pass


if __name__ == "__main__":
    print("第8章：错误和异常 - 练习题")
    print("=" * 45)
    
    # 测试基本异常处理
    print("8.3 基本异常处理测试：")
    test_data = [1, 2, "hello", 5, 0, "world", -1, 10]
    try:
        result = basic_exception_handling(test_data)
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  基本异常处理函数尚未实现: {e}")
    
    # 测试多种异常类型
    print("\n8.3 多种异常类型测试：")
    mixed_data = [1, {"value": 10}, "hello", [1, 2, 3], None, {"key": "value"}]
    try:
        result = multiple_exception_types(mixed_data)
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  多种异常类型函数尚未实现: {e}")
    
    # 测试异常传播
    print("\n8.3 异常传播测试：")
    try:
        result = exception_propagation_demo()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  异常传播演示函数尚未实现: {e}")
    
    # 测试自定义异常
    print("\n8.5 自定义异常测试：")
    try:
        result = custom_exception_usage()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  自定义异常函数尚未实现: {e}")
    
    # 测试异常最佳实践
    print("\n8 异常最佳实践测试：")
    try:
        result = exception_best_practices()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  异常最佳实践函数尚未实现: {e}")
    
    print("\n请实现上述函数，然后运行 pytest tests/ 验证实现！")
    print("注意：异常处理是 Python 中非常重要的概念，请仔细理解每种场景。") 