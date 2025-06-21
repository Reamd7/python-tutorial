"""
测试第15章：高级装饰器 (Advanced Decorators)
Tests for Chapter 15: Advanced Decorator Patterns and Applications
"""

import pytest
import time
import asyncio
from unittest.mock import patch, MagicMock
import threading

# 导入要测试的模块
try:
    from exercises.chapter15_advanced_decorators import (
        simple_timer, retry, log_calls, PerformanceMonitor, monitor,
        performance_monitor, simple_cache, timed_cache, lru_cache_with_stats,
        User, current_user, require_auth, require_roles, validate_types,
        singleton, add_logging, auto_property, DataClassLike,
        conditional_decorator, debug_mode_only, environment_specific,
        async_retry, async_timer, rate_limit, trace_calls, deprecated,
        memoize_disk, compose_decorators, DecoratorChain,
        api_endpoint
    )
except ImportError:
    pytest.skip("Chapter 15 module not found", allow_module_level=True)


class TestBasicDecorators:
    """测试基础装饰器"""
    
    def test_simple_timer(self):
        """测试简单计时装饰器"""
        try:
            @simple_timer
            def slow_function():
                time.sleep(0.1)
                return "done"
            
            result = slow_function()
            assert result == "done"
            # 函数元数据应该被保持
            assert slow_function.__name__ == "slow_function"
        except NotImplementedError:
            pytest.skip("simple_timer not implemented yet")
    
    def test_retry_decorator(self):
        """测试重试装饰器"""
        try:
            call_count = 0
            
            @retry(max_attempts=3, delay=0.01)
            def unreliable_function():
                nonlocal call_count
                call_count += 1
                if call_count < 3:
                    raise ValueError("Simulated failure")
                return "success"
            
            result = unreliable_function()
            assert result == "success"
            assert call_count == 3
        except NotImplementedError:
            pytest.skip("retry decorator not implemented yet")
    
    def test_log_calls_decorator(self):
        """测试日志装饰器"""
        try:
            @log_calls(include_args=True, include_result=True)
            def add_numbers(a, b):
                return a + b
            
            result = add_numbers(2, 3)
            assert result == 5
        except NotImplementedError:
            pytest.skip("log_calls decorator not implemented yet")


class TestPerformanceMonitoring:
    """测试性能监控装饰器"""
    
    def test_performance_monitor_class(self):
        """测试性能监控类"""
        try:
            monitor_instance = PerformanceMonitor()
            
            @monitor_instance.monitor
            def test_function():
                time.sleep(0.1)
                return "test"
            
            result = test_function()
            assert result == "test"
            
            stats = monitor_instance.get_stats("test_function")
            assert stats['call_count'] == 1
            assert stats['total_time'] >= 0.1
        except NotImplementedError:
            pytest.skip("PerformanceMonitor not implemented yet")
    
    def test_global_performance_monitor(self):
        """测试全局性能监控器"""
        try:
            @performance_monitor
            def monitored_function():
                time.sleep(0.05)
                return 42
            
            result = monitored_function()
            assert result == 42
            
            stats = monitor.get_stats("monitored_function")
            assert 'call_count' in stats
        except NotImplementedError:
            pytest.skip("performance_monitor not implemented yet")


class TestCachingDecorators:
    """测试缓存装饰器"""
    
    def test_simple_cache(self):
        """测试简单缓存装饰器"""
        try:
            call_count = 0
            
            @simple_cache
            def expensive_function(x):
                nonlocal call_count
                call_count += 1
                return x * x
            
            # 第一次调用
            result1 = expensive_function(5)
            assert result1 == 25
            assert call_count == 1
            
            # 第二次调用同样参数，应该使用缓存
            result2 = expensive_function(5)
            assert result2 == 25
            assert call_count == 1  # 没有增加
            
            # 不同参数
            result3 = expensive_function(3)
            assert result3 == 9
            assert call_count == 2
        except NotImplementedError:
            pytest.skip("simple_cache not implemented yet")
    
    def test_timed_cache(self):
        """测试带过期时间的缓存装饰器"""
        try:
            call_count = 0
            
            @timed_cache(expiry_seconds=1)
            def cached_function(x):
                nonlocal call_count
                call_count += 1
                return x * 2
            
            # 第一次调用
            result1 = cached_function(10)
            assert result1 == 20
            assert call_count == 1
            
            # 立即第二次调用，使用缓存
            result2 = cached_function(10)
            assert result2 == 20
            assert call_count == 1
            
            # 等待缓存过期
            time.sleep(1.1)
            result3 = cached_function(10)
            assert result3 == 20
            assert call_count == 2  # 缓存过期，重新计算
        except NotImplementedError:
            pytest.skip("timed_cache not implemented yet")
    
    def test_lru_cache_with_stats(self):
        """测试带统计的LRU缓存"""
        try:
            @lru_cache_with_stats(maxsize=2)
            def fibonacci(n):
                if n < 2:
                    return n
                return fibonacci(n-1) + fibonacci(n-2)
            
            result = fibonacci(5)
            assert result == 5  # fibonacci(5) = 5
            
            # 检查是否有统计信息
            assert hasattr(fibonacci, 'cache_info')
        except NotImplementedError:
            pytest.skip("lru_cache_with_stats not implemented yet")


class TestAuthenticationDecorators:
    """测试认证和权限装饰器"""
    
    def test_require_auth_decorator(self):
        """测试认证装饰器"""
        try:
            @require_auth
            def protected_function():
                return "secret data"
            
            # 未认证用户
            global current_user
            current_user = None
            
            with pytest.raises(Exception):  # 应该抛出认证异常
                protected_function()
            
            # 已认证用户
            current_user = User("test_user", ["user"], True)
            result = protected_function()
            assert result == "secret data"
        except NotImplementedError:
            pytest.skip("require_auth not implemented yet")
    
    def test_require_roles_decorator(self):
        """测试角色权限装饰器"""
        try:
            @require_roles("admin", "moderator")
            def admin_function():
                return "admin data"
            
            # 普通用户
            global current_user
            current_user = User("user", ["user"], True)
            
            with pytest.raises(Exception):  # 权限不足
                admin_function()
            
            # 管理员用户
            current_user = User("admin", ["admin"], True)
            result = admin_function()
            assert result == "admin data"
        except NotImplementedError:
            pytest.skip("require_roles not implemented yet")
    
    def test_validate_types_decorator(self):
        """测试类型验证装饰器"""
        try:
            @validate_types(x=int, y=str)
            def typed_function(x, y):
                return f"{x}: {y}"
            
            # 正确类型
            result = typed_function(42, "hello")
            assert result == "42: hello"
            
            # 错误类型
            with pytest.raises(TypeError):
                typed_function("not_int", "hello")
        except NotImplementedError:
            pytest.skip("validate_types not implemented yet")


class TestClassDecorators:
    """测试类装饰器"""
    
    def test_singleton_decorator(self):
        """测试单例模式装饰器"""
        try:
            @singleton
            class Database:
                def __init__(self):
                    self.connection = "db_connection"
            
            db1 = Database()
            db2 = Database()
            
            # 应该是同一个实例
            assert db1 is db2
        except NotImplementedError:
            pytest.skip("singleton decorator not implemented yet")
    
    def test_add_logging_decorator(self):
        """测试添加日志功能的装饰器"""
        try:
            @add_logging
            class TestService:
                def public_method(self):
                    return "public"
                
                def _private_method(self):
                    return "private"
            
            service = TestService()
            result = service.public_method()
            assert result == "public"
        except NotImplementedError:
            pytest.skip("add_logging decorator not implemented yet")
    
    def test_dataclass_like_decorator(self):
        """测试类似dataclass的装饰器"""
        try:
            @DataClassLike
            class Point:
                def __init__(self, x, y):
                    self.x = x
                    self.y = y
            
            p1 = Point(1, 2)
            p2 = Point(1, 2)
            
            # 应该支持相等性比较和字符串表示
            assert p1 == p2
            assert "Point" in str(p1)
        except NotImplementedError:
            pytest.skip("DataClassLike decorator not implemented yet")


class TestConditionalDecorators:
    """测试条件装饰器"""
    
    def test_conditional_decorator(self):
        """测试条件装饰器"""
        try:
            def dummy_decorator(func):
                def wrapper(*args, **kwargs):
                    result = func(*args, **kwargs)
                    return f"decorated: {result}"
                return wrapper
            
            # 条件为真时应用装饰器
            @conditional_decorator(True, dummy_decorator)
            def function_with_decorator():
                return "test"
            
            result1 = function_with_decorator()
            assert "decorated:" in result1
            
            # 条件为假时不应用装饰器
            @conditional_decorator(False, dummy_decorator)
            def function_without_decorator():
                return "test"
            
            result2 = function_without_decorator()
            assert result2 == "test"
        except NotImplementedError:
            pytest.skip("conditional_decorator not implemented yet")
    
    def test_debug_mode_only(self):
        """测试调试模式装饰器"""
        try:
            @debug_mode_only
            def debug_function():
                return "debug info"
            
            # 根据__debug__变量的值来决定行为
            result = debug_function()
            # 在测试环境中通常__debug__为True
            if __debug__:
                assert result == "debug info"
        except NotImplementedError:
            pytest.skip("debug_mode_only not implemented yet")


class TestAsyncDecorators:
    """测试异步装饰器"""
    
    @pytest.mark.asyncio
    async def test_async_retry(self):
        """测试异步重试装饰器"""
        try:
            call_count = 0
            
            @async_retry(max_attempts=3, delay=0.01)
            async def unreliable_async_function():
                nonlocal call_count
                call_count += 1
                if call_count < 3:
                    raise ValueError("Async failure")
                return "async success"
            
            result = await unreliable_async_function()
            assert result == "async success"
            assert call_count == 3
        except NotImplementedError:
            pytest.skip("async_retry not implemented yet")
    
    @pytest.mark.asyncio
    async def test_async_timer(self):
        """测试异步计时装饰器"""
        try:
            @async_timer
            async def slow_async_function():
                await asyncio.sleep(0.1)
                return "async done"
            
            result = await slow_async_function()
            assert result == "async done"
        except NotImplementedError:
            pytest.skip("async_timer not implemented yet")
    
    @pytest.mark.asyncio
    async def test_rate_limit(self):
        """测试异步限流装饰器"""
        try:
            @rate_limit(calls_per_second=10.0)
            async def limited_function():
                return "limited"
            
            # 快速连续调用
            start_time = time.time()
            results = []
            for _ in range(3):
                result = await limited_function()
                results.append(result)
            end_time = time.time()
            
            assert all(r == "limited" for r in results)
            # 应该有一定的延迟
            assert end_time - start_time >= 0.1
        except NotImplementedError:
            pytest.skip("rate_limit not implemented yet")


class TestMetaprogrammingDecorators:
    """测试元编程装饰器"""
    
    def test_trace_calls(self):
        """测试调用跟踪装饰器"""
        try:
            @trace_calls
            def traced_function(x, y):
                return x + y
            
            result = traced_function(1, 2)
            assert result == 3
        except NotImplementedError:
            pytest.skip("trace_calls not implemented yet")
    
    def test_deprecated_decorator(self):
        """测试废弃警告装饰器"""
        try:
            @deprecated(reason="Use new_function instead", version="2.0")
            def old_function():
                return "old result"
            
            with pytest.warns(DeprecationWarning):
                result = old_function()
                assert result == "old result"
        except NotImplementedError:
            pytest.skip("deprecated decorator not implemented yet")
    
    def test_memoize_disk(self):
        """测试磁盘缓存装饰器"""
        try:
            import tempfile
            import os
            
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                cache_file = tmp.name
            
            try:
                call_count = 0
                
                @memoize_disk(cache_file)
                def disk_cached_function(x):
                    nonlocal call_count
                    call_count += 1
                    return x * x
                
                # 第一次调用
                result1 = disk_cached_function(5)
                assert result1 == 25
                assert call_count == 1
                
                # 第二次调用，应该从磁盘缓存读取
                result2 = disk_cached_function(5)
                assert result2 == 25
                assert call_count == 1
            finally:
                if os.path.exists(cache_file):
                    os.unlink(cache_file)
        except NotImplementedError:
            pytest.skip("memoize_disk not implemented yet")


class TestDecoratorComposition:
    """测试装饰器组合"""
    
    def test_compose_decorators(self):
        """测试装饰器组合器"""
        try:
            def decorator1(func):
                def wrapper(*args, **kwargs):
                    result = func(*args, **kwargs)
                    return f"dec1({result})"
                return wrapper
            
            def decorator2(func):
                def wrapper(*args, **kwargs):
                    result = func(*args, **kwargs)
                    return f"dec2({result})"
                return wrapper
            
            @compose_decorators(decorator1, decorator2)
            def test_function():
                return "test"
            
            result = test_function()
            # 装饰器应该按顺序应用
            assert "dec1" in result and "dec2" in result
        except NotImplementedError:
            pytest.skip("compose_decorators not implemented yet")
    
    def test_decorator_chain(self):
        """测试装饰器链"""
        try:
            def base_function():
                return "base"
            
            chain = DecoratorChain(base_function)
            decorated_func = (chain
                            .add_timer()
                            .add_cache()
                            .add_log()
                            .build())
            
            result = decorated_func()
            assert result == "base"
        except NotImplementedError:
            pytest.skip("DecoratorChain not implemented yet")


class TestPracticalApplications:
    """测试实际应用示例"""
    
    def test_api_endpoint_decorator(self):
        """测试API端点装饰器"""
        try:
            @api_endpoint(
                method="GET",
                path="/users",
                auth_required=True,
                cache_seconds=60,
                rate_limit_per_minute=100
            )
            def get_users():
                return {"users": []}
            
            result = get_users()
            assert "users" in result
        except NotImplementedError:
            pytest.skip("api_endpoint decorator not implemented yet")


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 