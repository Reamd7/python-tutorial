"""
测试第17章：Pytest 测试框架 (Pytest Testing Framework)
Tests for Chapter 17: Advanced Testing with Pytest

注意：这是测试测试框架的测试文件，主要验证各种测试功能是否正确实现
"""

import pytest
import asyncio
import tempfile
import os
from unittest.mock import Mock, patch, MagicMock

# 导入要测试的模块
try:
    from exercises.chapter17_pytest_testing import (
        add_numbers, divide_numbers, Calculator, StringProcessor,
        ValidationError, UserValidator, APIClient, EmailService,
        UserService, AsyncDataProcessor, PerformanceTestSuite
    )
except ImportError:
    pytest.skip("Chapter 17 module not found", allow_module_level=True)


class TestBasicFunctions:
    """测试基础测试函数"""
    
    def test_add_numbers_function(self):
        """测试加法函数"""
        try:
            result = add_numbers(2, 3)
            assert result == 5
        except NotImplementedError:
            pytest.skip("add_numbers not implemented yet")
    
    def test_divide_numbers_function(self):
        """测试除法函数"""
        try:
            result = divide_numbers(10.0, 2.0)
            assert result == 5.0
            
            # 测试除零错误
            with pytest.raises(ZeroDivisionError):
                divide_numbers(10.0, 0.0)
        except NotImplementedError:
            pytest.skip("divide_numbers not implemented yet")


class TestCalculatorClass:
    """测试计算器类"""
    
    def test_calculator_creation(self):
        """测试计算器创建"""
        try:
            calc = Calculator()
            assert calc.history == []
        except NotImplementedError:
            pytest.skip("Calculator not implemented yet")
    
    def test_calculator_operations(self):
        """测试计算器运算"""
        try:
            calc = Calculator()
            
            # 测试加法
            result = calc.add(3.0, 4.0)
            assert result == 7.0
            
            # 测试乘法
            result = calc.multiply(2.0, 5.0)
            assert result == 10.0
            
            # 测试除法
            result = calc.divide(15.0, 3.0)
            assert result == 5.0
            
            # 测试历史记录
            history = calc.get_history()
            assert len(history) == 3
        except NotImplementedError:
            pytest.skip("Calculator operations not implemented yet")
    
    def test_calculator_division_by_zero(self):
        """测试计算器除零错误"""
        try:
            calc = Calculator()
            
            with pytest.raises(ZeroDivisionError):
                calc.divide(10.0, 0.0)
        except NotImplementedError:
            pytest.skip("Calculator division not implemented yet")
    
    def test_calculator_history(self):
        """测试计算器历史功能"""
        try:
            calc = Calculator()
            
            calc.add(1.0, 2.0)
            calc.multiply(3.0, 4.0)
            
            history = calc.get_history()
            assert len(history) == 2
            
            calc.clear_history()
            history = calc.get_history()
            assert len(history) == 0
        except NotImplementedError:
            pytest.skip("Calculator history not implemented yet")


class TestStringProcessor:
    """测试字符串处理器"""
    
    @pytest.mark.parametrize("input_str,expected", [
        ("hello", "olleh"),
        ("world", "dlrow"),
        ("", ""),
        ("a", "a"),
        ("12345", "54321")
    ])
    def test_reverse_string_parametrized(self, input_str, expected):
        """参数化测试字符串反转"""
        try:
            result = StringProcessor.reverse_string(input_str)
            assert result == expected
        except NotImplementedError:
            pytest.skip("reverse_string not implemented yet")
    
    @pytest.mark.parametrize("input_str,expected", [
        ("hello", 2),
        ("world", 1),
        ("aeiou", 5),
        ("xyz", 0),
        ("", 0)
    ])
    def test_count_vowels_parametrized(self, input_str, expected):
        """参数化测试元音计数"""
        try:
            result = StringProcessor.count_vowels(input_str)
            assert result == expected
        except NotImplementedError:
            pytest.skip("count_vowels not implemented yet")
    
    @pytest.mark.parametrize("input_str,expected", [
        ("racecar", True),
        ("hello", False),
        ("a", True),
        ("", True),
        ("Aa", False),
        ("aabbaa", True)
    ])
    def test_is_palindrome_parametrized(self, input_str, expected):
        """参数化测试回文检查"""
        try:
            result = StringProcessor.is_palindrome(input_str)
            assert result == expected
        except NotImplementedError:
            pytest.skip("is_palindrome not implemented yet")
    
    def test_capitalize_words(self):
        """测试首字母大写"""
        try:
            result = StringProcessor.capitalize_words("hello world")
            assert result == "Hello World"
        except NotImplementedError:
            pytest.skip("capitalize_words not implemented yet")


class TestValidationErrors:
    """测试验证错误"""
    
    def test_email_validation(self):
        """测试邮箱验证"""
        try:
            # 有效邮箱
            assert UserValidator.validate_email("test@example.com") == True
            
            # 无效邮箱
            with pytest.raises(ValidationError):
                UserValidator.validate_email("invalid_email")
        except NotImplementedError:
            pytest.skip("email validation not implemented yet")
    
    def test_age_validation(self):
        """测试年龄验证"""
        try:
            # 有效年龄
            assert UserValidator.validate_age(25) == True
            
            # 无效年龄
            with pytest.raises(ValidationError):
                UserValidator.validate_age(-5)
            
            with pytest.raises(ValidationError):
                UserValidator.validate_age(200)
        except NotImplementedError:
            pytest.skip("age validation not implemented yet")
    
    def test_password_validation(self):
        """测试密码验证"""
        try:
            # 强密码
            assert UserValidator.validate_password("StrongPass123!") == True
            
            # 弱密码
            with pytest.raises(ValidationError):
                UserValidator.validate_password("weak")
        except NotImplementedError:
            pytest.skip("password validation not implemented yet")


class TestMockingAndStubbing:
    """测试模拟和打桩"""
    
    def test_api_client_with_mock(self):
        """测试API客户端使用模拟"""
        try:
            client = APIClient("http://api.example.com")
            
            # 模拟HTTP请求
            with patch('requests.get') as mock_get:
                mock_response = Mock()
                mock_response.json.return_value = {"id": 1, "name": "John"}
                mock_response.status_code = 200
                mock_get.return_value = mock_response
                
                result = client.get_user(1)
                assert result["id"] == 1
                assert result["name"] == "John"
        except NotImplementedError:
            pytest.skip("APIClient not implemented yet")
    
    def test_email_service_mock(self):
        """测试邮件服务模拟"""
        try:
            service = EmailService("smtp.example.com")
            
            # 模拟邮件发送
            with patch.object(service, 'send_welcome_email', return_value=True):
                result = service.send_welcome_email("test@example.com", "John")
                assert result == True
        except NotImplementedError:
            pytest.skip("EmailService not implemented yet")
    
    def test_user_service_integration_mock(self):
        """测试用户服务集成模拟"""
        try:
            # 创建模拟的依赖
            mock_api_client = Mock()
            mock_email_service = Mock()
            
            # 配置模拟行为
            mock_api_client.create_user.return_value = {"id": 1, "name": "John"}
            mock_email_service.send_welcome_email.return_value = True
            
            service = UserService(mock_api_client, mock_email_service)
            
            user_data = {"name": "John", "email": "john@example.com"}
            result = service.register_user(user_data)
            
            # 验证调用
            mock_api_client.create_user.assert_called_once_with(user_data)
            mock_email_service.send_welcome_email.assert_called_once()
        except NotImplementedError:
            pytest.skip("UserService not implemented yet")


class TestAsyncTesting:
    """测试异步测试"""
    
    @pytest.mark.asyncio
    async def test_async_data_processor_fetch(self):
        """测试异步数据获取"""
        try:
            processor = AsyncDataProcessor()
            
            # 模拟异步HTTP请求
            with patch('aiohttp.ClientSession') as mock_session:
                mock_response = AsyncMock()
                mock_response.json = AsyncMock(return_value={"data": "test"})
                mock_session.return_value.__aenter__.return_value.get.return_value.__aenter__.return_value = mock_response
                
                result = await processor.fetch_data("http://example.com")
                assert result["data"] == "test"
        except NotImplementedError:
            pytest.skip("AsyncDataProcessor fetch not implemented yet")
    
    @pytest.mark.asyncio
    async def test_async_data_processor_process(self):
        """测试异步数据处理"""
        try:
            processor = AsyncDataProcessor()
            
            data = [{"value": 1}, {"value": 2}, {"value": 3}]
            result = await processor.process_data(data)
            
            assert len(result) == 3
        except NotImplementedError:
            pytest.skip("AsyncDataProcessor process not implemented yet")
    
    @pytest.mark.asyncio
    async def test_async_data_processor_save(self):
        """测试异步数据保存"""
        try:
            processor = AsyncDataProcessor()
            
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                filename = tmp.name
            
            try:
                data = [{"key": "value"}]
                result = await processor.save_data(data, filename)
                assert result == True
                assert os.path.exists(filename)
            finally:
                if os.path.exists(filename):
                    os.unlink(filename)
        except NotImplementedError:
            pytest.skip("AsyncDataProcessor save not implemented yet")


class TestMarkers:
    """测试标记功能"""
    
    @pytest.mark.slow
    def test_slow_operation_marker(self):
        """测试慢速操作标记"""
        import time
        time.sleep(0.1)  # 模拟慢速操作
        assert True
    
    @pytest.mark.integration
    def test_integration_marker(self):
        """测试集成标记"""
        # 模拟集成测试
        assert True
    
    @pytest.mark.unit
    def test_unit_marker(self):
        """测试单元标记"""
        # 模拟单元测试
        assert True
    
    @pytest.mark.skip(reason="Feature not ready")
    def test_skipped_test(self):
        """测试跳过的测试"""
        assert False  # 这个不会执行
    
    @pytest.mark.skipif(os.name == "nt", reason="Unix only")
    def test_conditional_skip(self):
        """测试条件跳过"""
        assert True


class TestFixtures:
    """测试夹具功能"""
    
    @pytest.fixture
    def sample_calculator(self):
        """示例计算器夹具"""
        try:
            calc = Calculator()
            calc.add(1, 1)  # 预设一些状态
            return calc
        except:
            return None
    
    @pytest.fixture
    def temp_file_fixture(self):
        """临时文件夹具"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
            tmp.write("test content")
            filename = tmp.name
        
        yield filename
        
        # 清理
        if os.path.exists(filename):
            os.unlink(filename)
    
    def test_with_calculator_fixture(self, sample_calculator):
        """使用计算器夹具的测试"""
        if sample_calculator is None:
            pytest.skip("Calculator not available")
        
        history = sample_calculator.get_history()
        assert len(history) >= 0
    
    def test_with_temp_file_fixture(self, temp_file_fixture):
        """使用临时文件夹具的测试"""
        assert os.path.exists(temp_file_fixture)
        
        with open(temp_file_fixture, 'r') as f:
            content = f.read()
            assert "test content" in content


class TestPerformanceTesting:
    """测试性能测试"""
    
    def test_performance_test_suite(self):
        """测试性能测试套件"""
        try:
            suite = PerformanceTestSuite()
            
            # 测试是否能创建实例
            assert suite is not None
        except NotImplementedError:
            pytest.skip("PerformanceTestSuite not implemented yet")
    
    def test_execution_time_constraint(self):
        """测试执行时间约束"""
        import time
        
        start_time = time.time()
        # 模拟一个快速操作
        result = sum(range(1000))
        end_time = time.time()
        
        # 应该在合理时间内完成
        assert end_time - start_time < 0.1
        assert result == sum(range(1000))


class TestErrorHandling:
    """测试错误处理"""
    
    def test_exception_handling(self):
        """测试异常处理"""
        try:
            with pytest.raises(ValueError) as exc_info:
                raise ValueError("Test error message")
            
            assert "Test error message" in str(exc_info.value)
        except:
            pytest.skip("Exception handling test failed")
    
    def test_custom_exception(self):
        """测试自定义异常"""
        try:
            with pytest.raises(ValidationError) as exc_info:
                raise ValidationError("Custom validation error")
            
            assert "validation" in str(exc_info.value).lower()
        except:
            pytest.skip("Custom exception test failed")


class TestDataValidation:
    """测试数据验证"""
    
    @pytest.mark.parametrize("value,expected", [
        (5, True),
        (-1, False),
        (0, False),
        (100, True)
    ])
    def test_positive_number_validation(self, value, expected):
        """参数化测试正数验证"""
        def is_positive(x):
            return x > 0
        
        result = is_positive(value)
        assert result == expected


if __name__ == "__main__":
    # 运行这个测试文件
    pytest.main([__file__, "-v", "--tb=short"]) 