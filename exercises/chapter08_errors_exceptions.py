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


def basic_exception_handling(numbers: list[int | float]) -> dict:
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

    result: list[int | float] = []
    errors: list[str] = []
    type_errors: int = 0
    value_errors: int = 0
    zero_division_errors: int = 0
    other_errors: int = 0

    import math

    for number in numbers:
        try:
            float_number = float(number)
            math.sqrt(float_number)
            float_number / (float_number - 5)
            result.append(float_number)
        except TypeError as e:
            type_errors += 1
            errors.append(f"{e}")
        except ValueError as e:
            value_errors += 1
            errors.append(f"{e}")
        except ZeroDivisionError as e:
            zero_division_errors += 1
            errors.append(f"{e}")
        except:
            other_errors += 1
            errors.append(f"Unexpected error: {sys.exc_info()[0]}")
    return {
        "results": result,
        "errors": errors,
        "type_errors": type_errors,
        "value_errors": value_errors,
        "zero_division_errors": zero_division_errors,
        "other_errors": other_errors,
    }


def multiple_exception_types(data: list[int | float | dict | list | None]) -> dict:
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
    successful_operations: int = 0
    type_error_count: int = 0
    key_error_count: int = 0
    attribute_error_count: int = 0
    value_error_count: int = 0
    error_details: list[str] = []

    for item in data:
        try:
            # 尝试转换为int
            int_result = int(item)
            # 尝试访问字典的value键
            value = item['value']
            # 尝试调用upper()方法
            upper_result = item.upper()
            successful_operations += 1
        except TypeError as e:
            type_error_count += 1
            error_details.append(f"TypeError: {e}")
        except KeyError as e:
            key_error_count += 1
            error_details.append(f"KeyError: {e}")
        except AttributeError as e:
            attribute_error_count += 1
            error_details.append(f"AttributeError: {e}")
        except ValueError as e:
            value_error_count += 1
            error_details.append(f"ValueError: {e}")
        except Exception as e:
            error_details.append(f"Unexpected error: {type(e).__name__}: {e}")
    return {
        "successful_operations": successful_operations,
        "type_error_count": type_error_count,
        "key_error_count": key_error_count,
        "attribute_error_count": attribute_error_count,
        "value_error_count": value_error_count,
        "error_details": error_details,
    }

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
    
    # 演示异常传播的不同捕获方式
    results = {}
    
    # 1. 在 level_1 捕获异常
    def level_1_with_catch():
        try:
            level_2()
        except ValueError as e:
            return f"在 level_1 捕获到异常: {e}"
    
    results['caught_at_level_1'] = level_1_with_catch()
    
    # 2. 在 level_2 捕获异常
    def level_2_with_catch():
        try:
            level_3()
        except ValueError as e:
            return f"在 level_2 捕获到异常: {e}"
    
    def level_1_calling_level_2_with_catch():
        return level_2_with_catch()
    
    results['caught_at_level_2'] = level_1_calling_level_2_with_catch()
    
    # 3. 在顶层捕获异常
    try:
        level_1()
    except ValueError as e:
        results['caught_at_top'] = f"在顶层捕获到异常: {e}"
        results['exception_type'] = type(e).__name__
        
        # 获取回溯信息
        tb_lines = traceback.format_exc().split('\n')
        results['traceback_info'] = [line for line in tb_lines if line.strip()]
    
    return results


def try_except_else_finally_demo(filename="test_file.txt"):
    """
    练习 8.4, 8.7: try-except-else-finally 完整演示
    
    Args:
        filename (str): 要操作的文件名
    
    Returns:
        dict: 各个子句的执行结果
    """
    results = {
        'try_executed': False,
        'except_executed': False,
        'else_executed': False,
        'finally_executed': False,
        'file_content': None,
        'error_message': None,
        'cleanup_performed': False
    }
    
    # 创建一个测试文件
    Path(filename).write_text("这是测试文件的内容\n第二行内容")
    
    try:
        results['try_executed'] = True
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            results['file_content'] = content
    except FileNotFoundError as e:
        results['except_executed'] = True
        results['error_message'] = f"文件未找到: {e}"
    except IOError as e:
        results['except_executed'] = True
        results['error_message'] = f"IO错误: {e}"
    else:
        results['else_executed'] = True
        print("文件读取成功，执行else子句")
    finally:
        results['finally_executed'] = True
        results['cleanup_performed'] = True
        # 清理测试文件
        try:
            Path(filename).unlink()
        except:
            pass
    
    return results


def raise_exception_examples():
    """
    练习 8.4: 抛出异常示例
    
    Returns:
        dict: 抛出异常的各种方式
    """
    results = {}
    
    # 1. 抛出简单异常
    try:
        raise ValueError
    except ValueError as e:
        results['raise_simple'] = f"捕获到简单异常: {type(e).__name__}"
    
    # 2. 带消息抛出异常
    try:
        raise ValueError("这是一个带消息的异常")
    except ValueError as e:
        results['raise_with_message'] = f"捕获到带消息的异常: {e}"
    
    # 3. 抛出自定义异常
    try:
        raise ValidationError("用户输入无效", field="email")
    except ValidationError as e:
        results['raise_custom'] = f"捕获到自定义异常: {e}, 字段: {e.field}"
    
    # 4. 重新抛出异常
    try:
        try:
            raise ValueError("原始异常")
        except ValueError:
            # 重新抛出同样的异常
            raise
    except ValueError as e:
        results['reraise_exception'] = f"重新抛出的异常: {e}"
    
    # 5. 使用 raise...from 
    try:
        try:
            raise ValueError("原始异常")
        except ValueError as original_error:
            raise RuntimeError("处理过程中发生错误") from original_error
    except RuntimeError as e:
        results['raise_from'] = f"链式异常: {e}, 原因: {e.__cause__}"
    
    return results


def custom_exception_usage():
    """
    练习 8.5: 自定义异常的使用
    
    Returns:
        dict: 自定义异常的使用示例
    """
    results = {}
    
    # 1. ValidationError 的使用示例
    def validate_age(age):
        if age < 0:
            raise ValidationError("年龄不能为负数", field="age")
        if age > 150:
            raise ValidationError("年龄不能超过150", field="age")
        return age
    
    try:
        validate_age(-5)
    except ValidationError as e:
        results['validation_error'] = f"验证错误: {e}, 字段: {e.field}"
    
    # 2. CalculationError 的使用示例
    def safe_divide(a, b):
        if b == 0:
            raise CalculationError("除数不能为零", operation="division", operands=(a, b))
        return a / b
    
    try:
        safe_divide(10, 0)
    except CalculationError as e:
        results['calculation_error'] = f"计算错误: {e}, 操作: {e.operation}, 操作数: {e.operands}"
    
    # 3. 异常继承层次的演示
    try:
        raise ValidationError("测试异常继承", field="test")
    except CustomError:
        results['exception_hierarchy'] = "ValidationError 被 CustomError 捕获（继承关系）"
    except Exception:
        results['exception_hierarchy'] = "被 Exception 捕获"
    
    # 4. 异常自定义属性的使用
    class DetailedError(CustomError):
        def __init__(self, message, error_code=None, context=None):
            super().__init__(message)
            self.error_code = error_code
            self.context = context or {}
    
    try:
        raise DetailedError("详细错误信息", error_code="E001", context={"user_id": 123, "action": "login"})
    except DetailedError as e:
        results['exception_attributes'] = f"详细错误: {e}, 代码: {e.error_code}, 上下文: {e.context}"
    
    return results


def exception_chaining_demo():
    """
    练习 8.4: 异常链演示
    
    Returns:
        dict: 异常链的演示结果
    """
    results = {}
    
    # 1. 隐式异常链（在处理一个异常时抛出另一个异常）
    try:
        try:
            raise ValueError("原始异常")
        except ValueError:
            raise RuntimeError("处理异常时发生的新异常")
    except RuntimeError as e:
        results['original_exception'] = str(e.__context__)
        results['chained_exception'] = str(e)
    
    # 2. 显式异常链（使用 raise...from）
    try:
        try:
            raise ValueError("底层异常")
        except ValueError as original:
            raise RuntimeError("高层异常") from original
    except RuntimeError as e:
        results['chain_details'] = {
            'current_exception': str(e),
            'caused_by': str(e.__cause__),
            'context': str(e.__context__) if e.__context__ else None
        }
    
    # 3. 抑制异常链（使用 raise...from None）
    try:
        try:
            raise ValueError("要被抑制的异常")
        except ValueError:
            raise RuntimeError("新异常，抑制原异常") from None
    except RuntimeError as e:
        results['suppressed_exception'] = {
            'current_exception': str(e),
            'has_cause': e.__cause__ is not None,
            'has_context': e.__context__ is not None
        }
    
    # 4. 在 finally 中抛出异常（抑制原异常）
    try:
        try:
            raise ValueError("原始异常")
        finally:
            raise RuntimeError("finally中的异常")
    except RuntimeError as e:
        results['finally_suppression'] = {
            'current_exception': str(e),
            'suppressed_exceptions': [str(s) for s in getattr(e, '__suppressed__', [])]
        }
    
    return results


def context_manager_with_exceptions():
    """
    练习 8.7: 上下文管理器与异常
    
    Returns:
        dict: 上下文管理器处理异常的演示
    """
    results = {}
    
    class MyContextManager:
        def __init__(self, suppress_exceptions=False):
            self.suppress_exceptions = suppress_exceptions
            self.cleanup_executed = False
        
        def __enter__(self):
            return "资源已获取"
        
        def __exit__(self, exc_type, exc_value, traceback):
            self.cleanup_executed = True
            if exc_type is not None:
                print(f"处理异常: {exc_type.__name__}: {exc_value}")
            # 返回True表示抑制异常，False表示不抑制
            return self.suppress_exceptions
    
    # 1. 正常执行
    manager1 = MyContextManager()
    with manager1:
        result = "正常执行完成"
    results['normal_execution'] = result
    results['cleanup_executed'] = manager1.cleanup_executed
    
    # 2. 异常被抑制
    manager2 = MyContextManager(suppress_exceptions=True)
    try:
        with manager2:
            raise ValueError("测试异常")
        results['exception_suppressed'] = "异常被成功抑制"
    except ValueError:
        results['exception_suppressed'] = "异常未被抑制"
    
    # 3. 异常未被抑制
    manager3 = MyContextManager(suppress_exceptions=False)
    try:
        with manager3:
            raise ValueError("测试异常")
        results['exception_not_suppressed'] = "异常被意外抑制"
    except ValueError:
        results['exception_not_suppressed'] = "异常正确传播"
    
    return results


def exception_performance_test():
    """
    练习 8: 异常性能测试
    
    Returns:
        dict: 异常对性能的影响测试
    """
    import time
    
    results = {}
    iterations = 10000
    
    # 1. 正常操作时间测试
    start_time = time.time()
    for i in range(iterations):
        try:
            result = i / (i + 1)
        except ZeroDivisionError:
            result = 0
    normal_time = time.time() - start_time
    results['normal_operation_time'] = normal_time
    
    # 2. 异常操作时间测试
    start_time = time.time()
    for i in range(iterations):
        try:
            result = i / 0  # 故意引发异常
        except ZeroDivisionError:
            result = 0
    exception_time = time.time() - start_time
    results['exception_operation_time'] = exception_time
    
    # 3. 性能比率
    results['performance_ratio'] = exception_time / normal_time if normal_time > 0 else 0
    
    # 4. EAFP vs LBYL 比较
    test_data = [1, 2, 3, "hello", 5, None, 7]
    
    # EAFP (Easier to Ask for Forgiveness than Permission)
    start_time = time.time()
    eafp_results = []
    for item in test_data:
        try:
            eafp_results.append(int(item))
        except (ValueError, TypeError):
            eafp_results.append(0)
    eafp_time = time.time() - start_time
    
    # LBYL (Look Before You Leap)
    start_time = time.time()
    lbyl_results = []
    for item in test_data:
        if isinstance(item, (int, float)) or (isinstance(item, str) and item.isdigit()):
            lbyl_results.append(int(item))
        else:
            lbyl_results.append(0)
    lbyl_time = time.time() - start_time
    
    results['eafp_time'] = eafp_time
    results['lbyl_time'] = lbyl_time
    results['recommendations'] = [
        "异常处理比正常流程慢，避免用异常控制程序流程",
        "对于可能的错误，EAFP通常比LBYL更pythonic",
        "异常应该用于真正的异常情况，而不是常规控制流"
    ]
    
    return results


def defensive_programming_examples():
    """
    练习 8: 防御性编程示例
    
    Returns:
        dict: 防御性编程的示例
    """
    results = {}
    
    # 1. 输入验证
    def validate_input(data):
        if not isinstance(data, (int, float)):
            raise TypeError("输入必须是数字")
        if data < 0:
            raise ValueError("输入必须是非负数")
        return data ** 2
    
    try:
        results['input_validation'] = validate_input(5)
    except (TypeError, ValueError) as e:
        results['input_validation'] = f"验证失败: {e}"
    
    # 2. 类型检查
    def safe_divide(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("操作数必须是数字")
        if b == 0:
            raise ZeroDivisionError("除数不能为零")
        return a / b
    
    try:
        results['type_checking'] = safe_divide(10, 2)
    except (TypeError, ZeroDivisionError) as e:
        results['type_checking'] = f"类型检查失败: {e}"
    
    # 3. 边界检查
    def safe_list_access(lst, index):
        if not isinstance(lst, list):
            raise TypeError("第一个参数必须是列表")
        if not isinstance(index, int):
            raise TypeError("索引必须是整数")
        if index < 0 or index >= len(lst):
            raise IndexError(f"索引 {index} 超出范围 [0, {len(lst)-1}]")
        return lst[index]
    
    try:
        results['boundary_checking'] = safe_list_access([1, 2, 3], 1)
    except (TypeError, IndexError) as e:
        results['boundary_checking'] = f"边界检查失败: {e}"
    
    # 4. 资源管理
    def safe_file_read(filename):
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "文件未找到，使用默认内容"
        except PermissionError:
            return "权限不足，无法读取文件"
        except Exception as e:
            return f"读取文件时发生未知错误: {e}"
    
    results['resource_management'] = safe_file_read("nonexistent.txt")
    
    # 5. 错误恢复
    def resilient_calculation(data):
        results_list = []
        for item in data:
            try:
                results_list.append(item * 2)
            except (TypeError, ValueError):
                # 恢复策略：跳过错误项
                results_list.append(None)
        return results_list
    
    results['error_recovery'] = resilient_calculation([1, 2, "hello", 4, None])
    
    return results


def exception_best_practices():
    """
    练习 8: 异常处理最佳实践
    
    Returns:
        dict: 异常处理的最佳实践示例
    """
    import logging
    
    # 配置日志
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    results = {}
    
    # 1. 捕获特定异常而非通用异常
    def good_exception_handling(data):
        try:
            return int(data)
        except ValueError:
            return "输入不是有效数字"
        except TypeError:
            return "输入类型错误"
    
    results['specific_exceptions'] = good_exception_handling("abc")
    
    # 2. 异常日志记录
    def function_with_logging():
        try:
            raise ValueError("演示异常")
        except ValueError as e:
            logger.error(f"发生异常: {e}", exc_info=True)
            return "异常已记录"
    
    results['exception_logging'] = function_with_logging()
    
    # 3. 优雅降级处理
    def graceful_degradation():
        try:
            # 尝试主要功能
            result = 1 / 0
        except ZeroDivisionError:
            # 降级到备用功能
            result = "使用默认值"
        return result
    
    results['graceful_degradation'] = graceful_degradation()
    
    # 4. 用户友好的错误消息
    def user_friendly_error(age):
        try:
            if age < 0:
                raise ValueError("年龄不能为负数")
            return f"年龄: {age}"
        except ValueError as e:
            return f"输入错误: {e}"
    
    results['user_friendly_messages'] = user_friendly_error(-5)
    
    # 5. 资源清理
    def resource_cleanup():
        file_handle = None
        try:
            file_handle = open("nonexistent.txt", "r")
            return file_handle.read()
        except FileNotFoundError:
            return "文件未找到"
        finally:
            if file_handle:
                file_handle.close()
    
    results['cleanup_resources'] = resource_cleanup()
    
    # 6. 不忽略异常的重要性
    def dont_ignore_exceptions():
        try:
            raise ValueError("重要的异常")
        except ValueError as e:
            # 不要只是 pass，要处理或记录
            logger.warning(f"捕获到异常: {e}")
            return "异常已被适当处理"
    
    results['dont_ignore_exceptions'] = dont_ignore_exceptions()
    
    return results


def advanced_exception_features():
    """
    练习 8: 高级异常特性
    
    Returns:
        dict: 高级异常特性的演示
    """
    results = {}
    
    # 1. 异常注释（Python 3.11+）
    try:
        error = ValueError("基础错误")
        error.add_note("这是一个注释")
        error.add_note("这是另一个注释")
        raise error
    except ValueError as e:
        results['exception_notes'] = {
            'message': str(e),
            'notes': getattr(e, '__notes__', [])
        }
    except AttributeError:
        results['exception_notes'] = "异常注释功能需要Python 3.11+"
    
    # 2. 回溯信息操作
    def get_traceback_info():
        try:
            raise ValueError("测试异常")
        except ValueError:
            tb_info = traceback.format_exc()
            return tb_info
    
    results['traceback_manipulation'] = get_traceback_info()
    
    # 3. 自定义回溯格式
    def custom_traceback_format():
        try:
            raise ValueError("自定义格式测试")
        except ValueError:
            tb_lines = traceback.format_exc().split('\n')
            # 自定义格式：只保留关键信息
            custom_format = []
            for line in tb_lines:
                if 'File' in line or 'ValueError' in line:
                    custom_format.append(line.strip())
            return custom_format
    
    results['custom_traceback'] = custom_traceback_format()
    
    # 4. 异常钩子的使用
    original_excepthook = sys.excepthook
    
    def custom_exception_hook(exc_type, exc_value, exc_traceback):
        return f"自定义异常处理: {exc_type.__name__}: {exc_value}"
    
    # 临时设置自定义钩子
    sys.excepthook = custom_exception_hook
    results['exception_hooks'] = "异常钩子已设置"
    
    # 恢复原始钩子
    sys.excepthook = original_excepthook
    
    # 5. 异常组模拟（为了兼容性）
    def simulate_exception_group():
        exceptions = []
        for i in range(3):
            try:
                if i == 0:
                    raise ValueError(f"错误 {i}")
                elif i == 1:
                    raise TypeError(f"类型错误 {i}")
                else:
                    raise RuntimeError(f"运行时错误 {i}")
            except Exception as e:
                exceptions.append(e)
        return exceptions
    
    results['exception_groups'] = [str(e) for e in simulate_exception_group()]
    
    return results


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