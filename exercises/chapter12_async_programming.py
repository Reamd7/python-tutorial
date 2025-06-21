"""
第12章：异步编程 (Asyncio)
Asynchronous Programming with asyncio

本章涵盖：
- async/await 基础语法
- 协程 (Coroutines) 的创建和使用
- 事件循环 (Event Loop)
- 并发任务执行
- 异步HTTP请求
- 异步文件操作
- 异步上下文管理器
- 同步和异步代码的集成
"""

import asyncio
import aiohttp
import aiofiles
import time
from typing import List, Dict, Any


# =============================================================================
# 1. 基础异步函数
# =============================================================================

async def hello_async():
    """
    TODO: 实现一个简单的异步函数
    - 使用 await asyncio.sleep(1) 暂停1秒
    - 返回字符串 "Hello, Async World!"
    """
    pass


async def fetch_data_with_delay(data: str, delay: float) -> str:
    """
    TODO: 模拟异步数据获取
    - 等待指定的延迟时间
    - 返回格式化的字符串: "Data: {data} (delayed {delay}s)"
    """
    pass


# =============================================================================
# 2. 并发任务执行
# =============================================================================

async def run_concurrent_tasks(tasks_data: List[tuple]) -> List[str]:
    """
    TODO: 并发执行多个任务
    - tasks_data 是包含 (data, delay) 元组的列表
    - 使用 asyncio.gather() 并发执行 fetch_data_with_delay
    - 返回所有结果的列表
    
    示例:
    tasks_data = [("task1", 1.0), ("task2", 0.5), ("task3", 1.5)]
    """
    pass


async def run_tasks_as_completed(tasks_data: List[tuple]) -> List[str]:
    """
    TODO: 使用 asyncio.as_completed() 处理任务
    - 按完成顺序收集结果
    - 返回结果列表（按完成顺序）
    """
    pass


# =============================================================================
# 3. 异步生成器
# =============================================================================

async def async_range(start: int, stop: int, delay: float = 0.1):
    """
    TODO: 实现异步生成器
    - 从 start 到 stop-1 逐个yield数字
    - 每次yield前等待指定延迟
    """
    pass


async def collect_async_generator(gen) -> List[int]:
    """
    TODO: 收集异步生成器的所有值
    - 使用 async for 遍历异步生成器
    - 返回所有值的列表
    """
    pass


# =============================================================================
# 4. 异步上下文管理器
# =============================================================================

class AsyncTimer:
    """
    TODO: 实现异步上下文管理器
    - 在进入时记录开始时间
    - 在退出时计算并存储执行时间
    """
    
    def __init__(self):
        self.start_time = None
        self.execution_time = None
    
    async def __aenter__(self):
        """异步进入上下文管理器"""
        pass
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """异步退出上下文管理器"""
        pass


# =============================================================================
# 5. 异步HTTP请求 (需要 aiohttp)
# =============================================================================

async def fetch_url(session: aiohttp.ClientSession, url: str) -> Dict[str, Any]:
    """
    TODO: 异步获取URL内容
    - 使用给定的 session 发送GET请求
    - 返回包含 url, status, content_length 的字典
    - 处理异常情况
    """
    pass


async def fetch_multiple_urls(urls: List[str]) -> List[Dict[str, Any]]:
    """
    TODO: 并发获取多个URL
    - 创建 aiohttp.ClientSession
    - 并发获取所有URL
    - 正确关闭session
    - 返回结果列表
    """
    pass


# =============================================================================
# 6. 异步文件操作 (需要 aiofiles)
# =============================================================================

async def async_write_file(filename: str, content: str) -> None:
    """
    TODO: 异步写入文件
    - 使用 aiofiles 写入文件
    - 确保文件正确关闭
    """
    pass


async def async_read_file(filename: str) -> str:
    """
    TODO: 异步读取文件
    - 使用 aiofiles 读取文件内容
    - 返回文件内容
    """
    pass


async def process_files_concurrently(file_operations: List[tuple]) -> List[str]:
    """
    TODO: 并发处理文件操作
    - file_operations 是 (operation, filename, content) 元组列表
    - operation 可以是 'read' 或 'write'
    - 对于 'write' 操作，使用 content 参数
    - 对于 'read' 操作，忽略 content 参数
    - 返回操作结果列表
    """
    pass


# =============================================================================
# 7. 任务管理和取消
# =============================================================================

async def cancellable_task(task_id: int, duration: float) -> str:
    """
    TODO: 可取消的任务
    - 尝试等待指定的持续时间
    - 如果被取消，捕获 asyncio.CancelledError
    - 返回任务状态信息
    """
    pass


async def task_with_timeout(coro, timeout: float):
    """
    TODO: 带超时的任务执行
    - 使用 asyncio.wait_for() 执行协程
    - 处理 asyncio.TimeoutError
    - 返回结果或超时信息
    """
    pass


# =============================================================================
# 8. 同步和异步代码集成
# =============================================================================

def sync_function(x: int) -> int:
    """同步函数：计算平方"""
    time.sleep(0.1)  # 模拟耗时操作
    return x * x


async def run_sync_in_async(numbers: List[int]) -> List[int]:
    """
    TODO: 在异步环境中运行同步代码
    - 使用 asyncio.to_thread() 或 loop.run_in_executor()
    - 并发处理所有数字
    - 返回结果列表
    """
    pass


async def async_function(x: int) -> int:
    """异步函数：计算立方"""
    await asyncio.sleep(0.1)  # 模拟异步耗时操作
    return x * x * x


def run_async_from_sync(numbers: List[int]) -> List[int]:
    """
    TODO: 从同步代码运行异步函数
    - 使用 asyncio.run() 或获取事件循环
    - 处理所有数字
    - 返回结果列表
    """
    pass


# =============================================================================
# 9. 异步队列
# =============================================================================

class AsyncProducerConsumer:
    """
    TODO: 实现异步生产者-消费者模式
    """
    
    def __init__(self, queue_size: int = 10):
        self.queue = asyncio.Queue(maxsize=queue_size)
        self.results = []
    
    async def producer(self, items: List[Any]) -> None:
        """
        TODO: 生产者协程
        - 将所有items放入队列
        - 最后放入一个特殊的结束标记 None
        """
        pass
    
    async def consumer(self, consumer_id: int) -> None:
        """
        TODO: 消费者协程
        - 从队列中获取items直到遇到 None
        - 处理每个item（可以简单地加上consumer_id）
        - 将结果存储到 self.results
        """
        pass
    
    async def run(self, items: List[Any], num_consumers: int = 2) -> List[Any]:
        """
        TODO: 运行生产者-消费者系统
        - 启动一个生产者和多个消费者
        - 等待所有任务完成
        - 返回处理结果
        """
        pass


# =============================================================================
# 10. 性能比较
# =============================================================================

async def async_performance_test(num_tasks: int, delay: float) -> Dict[str, float]:
    """
    TODO: 异步性能测试
    - 测试并发执行 num_tasks 个任务的时间
    - 每个任务等待 delay 秒
    - 返回包含任务数量、总时间、平均时间的字典
    """
    pass


def sync_performance_test(num_tasks: int, delay: float) -> Dict[str, float]:
    """
    TODO: 同步性能测试（用于对比）
    - 顺序执行 num_tasks 个任务
    - 每个任务等待 delay 秒（使用 time.sleep）
    - 返回包含任务数量、总时间、平均时间的字典
    """
    pass


# =============================================================================
# 主程序示例
# =============================================================================

async def main():
    """主异步函数示例"""
    print("=== 异步编程示例 ===")
    
    # 基础异步函数示例
    print("\n1. 基础异步函数:")
    try:
        result = await hello_async()
        print(f"结果: {result}")
    except Exception as e:
        print(f"未实现: {e}")
    
    # 并发任务示例
    print("\n2. 并发任务:")
    try:
        tasks = [("任务1", 0.5), ("任务2", 0.3), ("任务3", 0.7)]
        results = await run_concurrent_tasks(tasks)
        print(f"并发结果: {results}")
    except Exception as e:
        print(f"未实现: {e}")
    
    print("\n=== 运行 'python -m exercises.chapter12_async_programming' 查看更多示例 ===")


if __name__ == "__main__":
    try:
        # 检查是否已安装必要的包
        import aiohttp
        import aiofiles
        print("所需包已安装，可以完整测试异步功能")
    except ImportError as e:
        print(f"缺少包: {e}")
        print("请运行: uv add aiohttp aiofiles")
    
    # 运行主程序
    asyncio.run(main()) 