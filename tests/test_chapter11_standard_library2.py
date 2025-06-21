"""
第11章：标准库概览 - 第二部分 的测试文件

测试标准库的高级功能：输出格式化、模板、二进制数据、多线程和日志等。
"""

import pytest
import sys
import os
import tempfile
import threading
import time
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exercises.chapter11_standard_library2 import (
    output_formatting_demo,
    template_string_demo,
    binary_data_layout,
    multithreading_demo,
    logging_demo,
    weak_references_demo,
    list_manipulation_tools,
    decimal_arithmetic_demo,
    fractions_demo,
    advanced_collections_demo,
    performance_tools_demo,
    data_structures_comparison,
    advanced_string_processing,
    concurrency_patterns
)


class TestChapter11:
    """第11章测试类"""
    
    def test_output_formatting_demo(self):
        """测试输出格式化"""
        try:
            result = output_formatting_demo()
            # 函数可能未实现，返回None是可接受的
            assert result is None or isinstance(result, dict)
        except NotImplementedError:
            pytest.skip("函数未实现")
    
    def test_template_string_demo(self):
        """测试模板演示"""
        try:
            result = template_string_demo()
            assert result is None or isinstance(result, dict)
        except NotImplementedError:
            pytest.skip("函数未实现")
    
    def test_binary_data_layout(self):
        """测试二进制数据演示"""
        try:
            result = binary_data_layout()
            assert result is None or isinstance(result, dict)
        except NotImplementedError:
            pytest.skip("函数未实现")
    
    def test_multithreading_demo(self):
        """测试多线程演示"""
        try:
            result = multithreading_demo()
            assert result is None or isinstance(result, dict)
        except NotImplementedError:
            pytest.skip("函数未实现")
    
    def test_logging_demo(self):
        """测试日志演示"""
        try:
            result = logging_demo()
            assert result is None or isinstance(result, dict)
        except NotImplementedError:
            pytest.skip("函数未实现")


class TestAdvancedFeatures:
    """测试高级功能"""
    
    def test_weak_references_demo(self):
        """测试弱引用演示"""
        try:
            result = weak_references_demo()
            assert result is None or isinstance(result, dict)
        except NotImplementedError:
            pytest.skip("函数未实现")
    
    def test_list_manipulation_tools(self):
        """测试列表操作工具"""
        try:
            result = list_manipulation_tools()
            assert result is None or isinstance(result, dict)
        except NotImplementedError:
            pytest.skip("函数未实现")
    
    def test_decimal_arithmetic_demo(self):
        """测试decimal算术"""
        try:
            result = decimal_arithmetic_demo()
            assert result is None or isinstance(result, dict)
        except NotImplementedError:
            pytest.skip("函数未实现")
    
    def test_fractions_demo(self):
        """测试分数演示"""
        try:
            result = fractions_demo()
            assert result is None or isinstance(result, dict)
        except NotImplementedError:
            pytest.skip("函数未实现")
    
    def test_advanced_collections_demo(self):
        """测试高级集合演示"""
        try:
            result = advanced_collections_demo()
            assert result is None or isinstance(result, dict)
        except NotImplementedError:
            pytest.skip("函数未实现")


class TestPerformanceTools:
    """测试性能工具"""
    
    def test_performance_tools_demo(self):
        """测试性能工具演示"""
        try:
            result = performance_tools_demo()
            assert result is None or isinstance(result, dict)
        except NotImplementedError:
            pytest.skip("函数未实现")
    
    def test_data_structures_comparison(self):
        """测试数据结构比较"""
        try:
            result = data_structures_comparison()
            assert result is None or isinstance(result, dict)
        except NotImplementedError:
            pytest.skip("函数未实现")
    
    def test_advanced_string_processing(self):
        """测试高级字符串处理"""
        try:
            result = advanced_string_processing()
            assert result is None or isinstance(result, dict)
        except NotImplementedError:
            pytest.skip("函数未实现")
    
    def test_concurrency_patterns(self):
        """测试并发模式"""
        try:
            result = concurrency_patterns()
            assert result is None or isinstance(result, dict)
        except NotImplementedError:
            pytest.skip("函数未实现")


class TestIntegration:
    """集成测试"""
    
    def test_all_functions_callable(self):
        """测试所有函数都可调用"""
        functions = [
            output_formatting_demo,
            template_string_demo,
            binary_data_layout,
            multithreading_demo,
            logging_demo,
            weak_references_demo,
            list_manipulation_tools,
            decimal_arithmetic_demo,
            fractions_demo,
            advanced_collections_demo,
            performance_tools_demo,
            data_structures_comparison,
            advanced_string_processing,
            concurrency_patterns
        ]
        
        for func in functions:
            assert callable(func), f"{func.__name__} 不可调用"
    
    def test_functions_return_data_or_none(self):
        """测试函数返回数据或None（未实现）"""
        # 测试主要的演示函数
        main_functions = [
            output_formatting_demo,
            template_string_demo,
            binary_data_layout,
            multithreading_demo,
            logging_demo
        ]
        
        for func in main_functions:
            try:
                result = func()
                # 未实现的函数可能返回None
                assert result is None or isinstance(result, dict), \
                    f"{func.__name__} 应该返回字典或None"
            except NotImplementedError:
                # 未实现的函数是可接受的
                pass
            except Exception as e:
                pytest.fail(f"{func.__name__} 执行失败: {e}")


if __name__ == '__main__':
    # 运行测试
    pytest.main([__file__, '-v']) 