"""
测试第13章：类型提示 (Type Hints)
Tests for Chapter 13: Type Hints and Static Typing
"""

import pytest
from typing import Dict, List, Any
import json

# 导入要测试的模块
try:
    from exercises.chapter13_type_hints import (
        greet_user, calculate_bmi, is_adult, process_numbers,
        group_by_length, merge_dictionaries, extract_coordinates,
        find_user_by_id, parse_number, safe_divide,
        create_user, calculate_distance, matrix_multiply,
        Stack, Cache, get_first_item, swap_elements,
        Circle, Rectangle, draw_shapes, total_area,
        create_person, update_person_email, validate_person,
        filter_products, get_config, update_status, get_api_info,
        type_safe_json_loads, type_safe_get, Product
    )
except ImportError:
    pytest.skip("Chapter 13 module not found", allow_module_level=True)


class TestBasicTypeAnnotations:
    """测试基础类型注解"""
    
    def test_greet_user(self):
        """测试问候用户函数"""
        try:
            result = greet_user("Alice", 25)
            assert result == "Hello Alice, you are 25 years old!"
        except NotImplementedError:
            pytest.skip("greet_user not implemented yet")
    
    def test_calculate_bmi(self):
        """测试BMI计算"""
        try:
            result = calculate_bmi(70.0, 1.75)
            expected = round(70.0 / (1.75 * 1.75), 2)
            assert result == expected
        except NotImplementedError:
            pytest.skip("calculate_bmi not implemented yet")
    
    def test_is_adult(self):
        """测试成年判断"""
        try:
            assert is_adult(18) == True
            assert is_adult(17) == False
            assert is_adult(25) == True
        except NotImplementedError:
            pytest.skip("is_adult not implemented yet")


class TestComplexTypes:
    """测试复合类型"""
    
    def test_process_numbers(self):
        """测试数字处理"""
        try:
            numbers = [1, 2, 3, 4, 5]
            result = process_numbers(numbers)
            
            assert result['sum'] == 15
            assert result['average'] == 3.0
            assert result['max'] == 5
            assert result['min'] == 1
        except NotImplementedError:
            pytest.skip("process_numbers not implemented yet")
    
    def test_group_by_length(self):
        """测试按长度分组"""
        try:
            words = ["cat", "dog", "elephant", "rat", "horse"]
            result = group_by_length(words)
            
            assert result[3] == ["cat", "dog", "rat"]
            assert result[8] == ["elephant"]
            assert result[5] == ["horse"]
        except NotImplementedError:
            pytest.skip("group_by_length not implemented yet")
    
    def test_merge_dictionaries(self):
        """测试字典合并"""
        try:
            dict1 = {"a": 1, "b": 2}
            dict2 = {"b": 3, "c": 4}
            result = merge_dictionaries(dict1, dict2)
            
            assert result["a"] == 1
            assert result["b"] == 5  # 2 + 3
            assert result["c"] == 4
        except NotImplementedError:
            pytest.skip("merge_dictionaries not implemented yet")
    
    def test_extract_coordinates(self):
        """测试坐标提取"""
        try:
            points = [(1.0, 2.0), (3.0, 4.0), (5.0, 6.0)]
            x_coords, y_coords = extract_coordinates(points)
            
            assert x_coords == [1.0, 3.0, 5.0]
            assert y_coords == [2.0, 4.0, 6.0]
        except NotImplementedError:
            pytest.skip("extract_coordinates not implemented yet")


class TestOptionalUnionTypes:
    """测试Optional和Union类型"""
    
    def test_find_user_by_id(self):
        """测试用户查找"""
        try:
            users = [
                {"id": 1, "name": "Alice"},
                {"id": 2, "name": "Bob"}
            ]
            
            result = find_user_by_id(1, users)
            assert result == {"id": 1, "name": "Alice"}
            
            result = find_user_by_id(999, users)
            assert result is None
        except NotImplementedError:
            pytest.skip("find_user_by_id not implemented yet")
    
    def test_parse_number(self):
        """测试数字解析"""
        try:
            assert parse_number("123") == 123.0
            assert parse_number(456) == 456.0
            assert parse_number("invalid") is None
        except NotImplementedError:
            pytest.skip("parse_number not implemented yet")
    
    def test_safe_divide(self):
        """测试安全除法"""
        try:
            assert safe_divide(10, 2) == 5.0
            assert safe_divide(10, 0) is None
        except NotImplementedError:
            pytest.skip("safe_divide not implemented yet")


class TestTypeAliases:
    """测试类型别名"""
    
    def test_create_user(self):
        """测试用户创建"""
        try:
            user = create_user(1, "Alice", "alice@example.com")
            assert isinstance(user, dict)
            assert user["id"] == 1
            assert user["name"] == "Alice"
            assert user["email"] == "alice@example.com"
        except NotImplementedError:
            pytest.skip("create_user not implemented yet")
    
    def test_calculate_distance(self):
        """测试距离计算"""
        try:
            point1 = (0.0, 0.0)
            point2 = (3.0, 4.0)
            distance = calculate_distance(point1, point2)
            assert distance == 5.0
        except NotImplementedError:
            pytest.skip("calculate_distance not implemented yet")
    
    def test_matrix_multiply(self):
        """测试矩阵乘法"""
        try:
            matrix1 = [[1, 2], [3, 4]]
            matrix2 = [[5, 6], [7, 8]]
            result = matrix_multiply(matrix1, matrix2)
            
            if result is not None:
                expected = [[19, 22], [43, 50]]
                assert result == expected
        except NotImplementedError:
            pytest.skip("matrix_multiply not implemented yet")


class TestGenerics:
    """测试泛型"""
    
    def test_stack_operations(self):
        """测试泛型栈操作"""
        try:
            stack = Stack[int]()
            
            assert stack.is_empty() == True
            assert stack.size() == 0
            assert stack.peek() is None
            
            stack.push(1)
            stack.push(2)
            
            assert stack.size() == 2
            assert stack.peek() == 2
            assert stack.pop() == 2
            assert stack.size() == 1
        except NotImplementedError:
            pytest.skip("Stack not implemented yet")
    
    def test_cache_operations(self):
        """测试泛型缓存操作"""
        try:
            cache = Cache[str, int](max_size=2)
            
            cache.set("a", 1)
            cache.set("b", 2)
            
            assert cache.get("a") == 1
            assert cache.get("b") == 2
            assert cache.get("c") is None
            
            cache.clear()
            assert cache.get("a") is None
        except NotImplementedError:
            pytest.skip("Cache not implemented yet")
    
    def test_generic_functions(self):
        """测试泛型函数"""
        try:
            # 测试get_first_item
            items = [1, 2, 3]
            assert get_first_item(items) == 1
            assert get_first_item([]) is None
            
            # 测试swap_elements
            swapped = swap_elements([1, 2, 3], 0, 2)
            assert swapped == [3, 2, 1]
        except NotImplementedError:
            pytest.skip("Generic functions not implemented yet")


class TestProtocols:
    """测试协议"""
    
    def test_drawable_shapes(self):
        """测试可绘制形状"""
        try:
            circle = Circle(5.0)
            rectangle = Rectangle(4.0, 3.0)
            
            # 测试单个形状
            assert "circle" in circle.draw().lower()
            assert abs(circle.area() - 78.54) < 0.1  # π * 5^2
            
            assert "rectangle" in rectangle.draw().lower()
            assert rectangle.area() == 12.0  # 4 * 3
            
            # 测试形状列表
            shapes = [circle, rectangle]
            descriptions = draw_shapes(shapes)
            assert len(descriptions) == 2
            
            total = total_area(shapes)
            assert abs(total - 90.54) < 0.1
        except NotImplementedError:
            pytest.skip("Drawable protocol not implemented yet")


class TestTypedDict:
    """测试TypedDict"""
    
    def test_person_operations(self):
        """测试人员操作"""
        try:
            person = create_person("Alice", 25, "alice@example.com")
            
            assert person["name"] == "Alice"
            assert person["age"] == 25
            assert person["email"] == "alice@example.com"
            assert person["is_active"] == True
            
            updated = update_person_email(person, "newemail@example.com")
            assert updated["email"] == "newemail@example.com"
        except NotImplementedError:
            pytest.skip("PersonDict operations not implemented yet")
    
    def test_validate_person(self):
        """测试人员数据验证"""
        try:
            valid_data = {
                "name": "Alice",
                "age": 25,
                "email": "alice@example.com",
                "is_active": True
            }
            assert validate_person(valid_data) == True
            
            invalid_data = {"name": "Alice"}  # 缺少字段
            assert validate_person(invalid_data) == False
        except NotImplementedError:
            pytest.skip("validate_person not implemented yet")


class TestAdvancedTypeFeatures:
    """测试高级类型特性"""
    
    def test_filter_products(self):
        """测试产品过滤"""
        try:
            products = [
                Product(1, "Laptop", 1000.0, "Electronics"),
                Product(2, "Book", 20.0, "Education"),
                Product(3, "Phone", 800.0, "Electronics")
            ]
            
            electronics = filter_products(
                products, 
                lambda p: p.category == "Electronics"
            )
            assert len(electronics) == 2
        except NotImplementedError:
            pytest.skip("filter_products not implemented yet")
    
    def test_get_config_overload(self):
        """测试配置获取重载"""
        try:
            # 测试不同的重载签名
            debug_value = get_config("debug")
            assert debug_value == "false"
            
            port_value = get_config("port")
            assert port_value == "8080"
            
            default_value = get_config("unknown", 42)
            assert default_value == 42
        except NotImplementedError:
            pytest.skip("get_config not implemented yet")
    
    def test_literal_types(self):
        """测试字面量类型"""
        try:
            result = update_status(123, "pending")
            assert result["id"] == 123
            assert result["status"] == "pending"
        except NotImplementedError:
            pytest.skip("update_status not implemented yet")
    
    def test_final_types(self):
        """测试Final类型"""
        try:
            info = get_api_info()
            assert "version" in info
            assert "max_retry_count" in info
        except NotImplementedError:
            pytest.skip("get_api_info not implemented yet")


class TestTypeUtilities:
    """测试类型工具函数"""
    
    def test_type_safe_json_loads(self):
        """测试类型安全的JSON解析"""
        try:
            valid_json = '{"name": "Alice", "age": 25}'
            result = type_safe_json_loads(valid_json)
            assert result == {"name": "Alice", "age": 25}
            
            invalid_json = "invalid json"
            result = type_safe_json_loads(invalid_json)
            assert result == {}
        except NotImplementedError:
            pytest.skip("type_safe_json_loads not implemented yet")
    
    def test_type_safe_get(self):
        """测试类型安全的字典取值"""
        try:
            data = {"name": "Alice", "age": 25, "score": 95.5}
            
            name = type_safe_get(data, "name", str)
            assert name == "Alice"
            
            age = type_safe_get(data, "age", int)
            assert age == 25
            
            # 类型不匹配的情况
            wrong_type = type_safe_get(data, "age", str)
            assert wrong_type is None
            
            # 键不存在的情况
            missing = type_safe_get(data, "missing", str)
            assert missing is None
        except NotImplementedError:
            pytest.skip("type_safe_get not implemented yet")


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 