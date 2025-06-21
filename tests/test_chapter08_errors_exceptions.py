"""
第8章：错误和异常 - 测试文件

测试 exercises/chapter08_errors_exceptions.py 中的练习函数
"""

import pytest
import sys
import os

# 添加 exercises 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from exercises.chapter08_errors_exceptions import (
    basic_exception_handling,
    multiple_exception_types,
    exception_propagation_demo,
    try_except_else_finally_demo,
    raise_exception_examples,
    custom_exception_usage,
    exception_chaining_demo,
    context_manager_with_exceptions,
    exception_performance_test,
    defensive_programming_examples,
    exception_best_practices,
    advanced_exception_features,
    CustomError,
    ValidationError,
    CalculationError
)


class TestErrorsExceptions:
    """第8章：错误和异常练习的测试类"""
    
    def test_basic_exception_handling(self):
        """测试基本异常处理"""
        test_data = [1, 2, "hello", 5, 0, "world", -1, 10]
        result = basic_exception_handling(test_data)
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'results', 'errors', 'type_errors', 'value_errors',
            'zero_division_errors', 'other_errors'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert isinstance(result['results'], list), "结果应该是列表"
        assert isinstance(result['errors'], list), "错误应该是列表"
        assert isinstance(result['type_errors'], int), "TypeError 数量应该是整数"
        assert isinstance(result['value_errors'], int), "ValueError 数量应该是整数"
        assert isinstance(result['zero_division_errors'], int), "ZeroDivisionError 数量应该是整数"
        assert isinstance(result['other_errors'], int), "其他错误数量应该是整数"
    
    def test_multiple_exception_types(self):
        """测试处理多种异常类型"""
        test_data = [1, {"value": 10}, "hello", [1, 2, 3], None, {"key": "value"}]
        result = multiple_exception_types(test_data)
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'successful_operations', 'type_error_count', 'key_error_count',
            'attribute_error_count', 'value_error_count', 'error_details'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert isinstance(result['successful_operations'], int), "成功操作数应该是整数"
        assert isinstance(result['error_details'], list), "错误详情应该是列表"
    
    def test_exception_propagation_demo(self):
        """测试异常传播演示"""
        result = exception_propagation_demo()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'caught_at_level_1', 'caught_at_level_2', 'caught_at_top',
            'traceback_info', 'exception_type'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert result['exception_type'] == 'ValueError', "异常类型应该是 ValueError"
    
    def test_try_except_else_finally_demo(self):
        """测试 try-except-else-finally 完整演示"""
        result = try_except_else_finally_demo("test_file.txt")
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'try_executed', 'except_executed', 'else_executed',
            'finally_executed', 'file_content', 'error_message', 'cleanup_performed'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert isinstance(result['try_executed'], bool), "try 执行状态应该是布尔值"
        assert isinstance(result['except_executed'], bool), "except 执行状态应该是布尔值"
        assert isinstance(result['else_executed'], bool), "else 执行状态应该是布尔值"
        assert isinstance(result['finally_executed'], bool), "finally 执行状态应该是布尔值"
    
    def test_raise_exception_examples(self):
        """测试抛出异常示例"""
        result = raise_exception_examples()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'raise_simple', 'raise_with_message', 'raise_custom',
            'reraise_exception', 'raise_from'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_custom_exception_usage(self):
        """测试自定义异常的使用"""
        result = custom_exception_usage()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'validation_error', 'calculation_error', 'exception_hierarchy',
            'exception_attributes'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_custom_exception_classes(self):
        """测试自定义异常类"""
        # 测试 ValidationError
        try:
            raise ValidationError("测试验证错误", field="email")
        except ValidationError as e:
            assert str(e) == "测试验证错误"
            assert e.field == "email"
        
        # 测试 CalculationError
        try:
            raise CalculationError("测试计算错误", operation="division", operands=[10, 0])
        except CalculationError as e:
            assert str(e) == "测试计算错误"
            assert e.operation == "division"
            assert e.operands == [10, 0]
        
        # 测试继承关系
        assert issubclass(ValidationError, CustomError)
        assert issubclass(CalculationError, CustomError)
        assert issubclass(CustomError, Exception)
    
    def test_exception_chaining_demo(self):
        """测试异常链演示"""
        result = exception_chaining_demo()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'original_exception', 'chained_exception', 'suppressed_exception',
            'chain_details'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_context_manager_with_exceptions(self):
        """测试上下文管理器与异常"""
        result = context_manager_with_exceptions()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'normal_execution', 'exception_suppressed', 'exception_not_suppressed',
            'cleanup_executed'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_exception_performance_test(self):
        """测试异常性能测试"""
        result = exception_performance_test()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'normal_operation_time', 'exception_operation_time',
            'performance_ratio', 'recommendations'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert isinstance(result['normal_operation_time'], (int, float)), "正常操作时间应该是数字"
        assert isinstance(result['exception_operation_time'], (int, float)), "异常操作时间应该是数字"
        assert isinstance(result['recommendations'], list), "建议应该是列表"
    
    def test_defensive_programming_examples(self):
        """测试防御性编程示例"""
        result = defensive_programming_examples()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'input_validation', 'type_checking', 'boundary_checking',
            'resource_management', 'error_recovery'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_exception_best_practices(self):
        """测试异常处理最佳实践"""
        result = exception_best_practices()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'specific_exceptions', 'exception_logging', 'graceful_degradation',
            'user_friendly_messages', 'cleanup_resources', 'dont_ignore_exceptions'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_advanced_exception_features(self):
        """测试高级异常特性"""
        result = advanced_exception_features()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'exception_groups', 'exception_notes', 'traceback_manipulation',
            'custom_traceback', 'exception_hooks'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"


if __name__ == "__main__":
    pytest.main([__file__]) 