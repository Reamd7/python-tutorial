"""
第16章：线程和多进程 (Threading & Multiprocessing)
Threading and Multiprocessing for Concurrent Programming

本章涵盖：
- threading 模块基础
- 线程同步：Lock, RLock, Semaphore, Condition
- 线程池 (ThreadPoolExecutor)
- multiprocessing 模块基础
- 进程间通信：Queue, Pipe, Manager
- 进程池 (ProcessPoolExecutor)
- concurrent.futures 统一接口
- GIL 的影响和解决方案
"""

import threading
import multiprocessing
import time
import queue
import concurrent.futures
from typing import List, Any, Callable, Optional
from dataclasses import dataclass
import json
import os


# =============================================================================
# 1. 基础线程操作
# =============================================================================

class SimpleThread:
    """
    TODO: 简单线程类
    - 封装线程创建和管理
    - 支持线程参数传递
    - 提供线程状态查询
    """
    
    def __init__(self, target: Callable, args: tuple = (), name: str = ""):
        self.target = target
        self.args = args
        self.name = name
        self.thread: Optional[threading.Thread] = None
        self.result = None
        self.exception = None
    
    def start(self) -> None:
        """TODO: 启动线程"""
        pass
    
    def join(self, timeout: Optional[float] = None) -> None:
        """TODO: 等待线程完成"""
        pass
    
    def is_alive(self) -> bool:
        """TODO: 检查线程是否还在运行"""
        pass


def cpu_bound_task(n: int) -> int:
    """
    TODO: CPU密集型任务
    - 计算前n个数字的平方和
    - 用于测试多线程和多进程性能差异
    """
    pass


def io_bound_task(delay: float, task_id: int) -> str:
    """
    TODO: IO密集型任务
    - 模拟网络请求或文件操作
    - 使用 time.sleep 模拟延迟
    - 返回任务完成信息
    """
    pass


def run_sequential(tasks: List[tuple], task_func: Callable) -> List[Any]:
    """
    TODO: 顺序执行任务
    - 依次执行所有任务
    - 记录总执行时间
    - 返回结果列表
    """
    pass


def run_threaded(tasks: List[tuple], task_func: Callable) -> List[Any]:
    """
    TODO: 多线程执行任务
    - 为每个任务创建线程
    - 收集所有线程结果
    - 返回结果列表
    """
    pass


# =============================================================================
# 2. 线程同步机制
# =============================================================================

class Counter:
    """
    TODO: 线程安全计数器
    - 演示线程同步的必要性
    - 提供加锁和不加锁的版本
    """
    
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    
    def increment_unsafe(self) -> None:
        """TODO: 不安全的递增操作"""
        pass
    
    def increment_safe(self) -> None:
        """TODO: 线程安全的递增操作"""
        pass
    
    def get_value(self) -> int:
        """TODO: 获取当前值"""
        pass


class BoundedBuffer:
    """
    TODO: 有界缓冲区
    - 使用 Condition 实现生产者-消费者模式
    - 支持多个生产者和消费者
    """
    
    def __init__(self, capacity: int):
        self.buffer: List[Any] = []
        self.capacity = capacity
        self.condition = threading.Condition()
    
    def put(self, item: Any) -> None:
        """TODO: 添加项目到缓冲区"""
        pass
    
    def get(self) -> Any:
        """TODO: 从缓冲区获取项目"""
        pass
    
    def size(self) -> int:
        """TODO: 获取缓冲区当前大小"""
        pass


class ConnectionPool:
    """
    TODO: 连接池
    - 使用 Semaphore 控制资源访问
    - 模拟数据库连接池
    """
    
    def __init__(self, max_connections: int):
        self.semaphore = threading.Semaphore(max_connections)
        self.connections = [f"Connection-{i}" for i in range(max_connections)]
        self.available = queue.Queue()
        for conn in self.connections:
            self.available.put(conn)
    
    def acquire_connection(self) -> str:
        """TODO: 获取连接"""
        pass
    
    def release_connection(self, connection: str) -> None:
        """TODO: 释放连接"""
        pass


# =============================================================================
# 3. 线程池执行器
# =============================================================================

def demonstrate_thread_pool():
    """
    TODO: 演示线程池的使用
    - 使用 ThreadPoolExecutor 执行IO密集型任务
    - 比较不同线程数的性能
    - 展示 as_completed 和 wait 的用法
    """
    pass


def batch_download_simulation(urls: List[str]) -> List[Dict[str, Any]]:
    """
    TODO: 模拟批量下载
    - 使用线程池并发下载多个URL
    - 每个URL的下载时间随机
    - 返回下载结果和耗时统计
    """
    pass


def parallel_file_processing(file_paths: List[str], 
                           processor: Callable[[str], Any]) -> List[Any]:
    """
    TODO: 并行文件处理
    - 使用线程池处理多个文件
    - 支持自定义处理函数
    - 处理异常情况
    """
    pass


# =============================================================================
# 4. 多进程基础
# =============================================================================

def worker_function(task_data: Any, result_queue: multiprocessing.Queue) -> None:
    """
    TODO: 工作进程函数
    - 处理传入的任务数据
    - 将结果放入结果队列
    - 处理进程间的异常传递
    """
    pass


class MultiprocessManager:
    """
    TODO: 多进程管理器
    - 管理多个工作进程
    - 分发任务和收集结果
    """
    
    def __init__(self, num_processes: int = None):
        self.num_processes = num_processes or multiprocessing.cpu_count()
        self.processes: List[multiprocessing.Process] = []
        self.task_queue = multiprocessing.Queue()
        self.result_queue = multiprocessing.Queue()
    
    def start_workers(self) -> None:
        """TODO: 启动工作进程"""
        pass
    
    def submit_task(self, task_data: Any) -> None:
        """TODO: 提交任务"""
        pass
    
    def get_results(self, num_results: int) -> List[Any]:
        """TODO: 获取结果"""
        pass
    
    def shutdown(self) -> None:
        """TODO: 关闭所有进程"""
        pass


def run_multiprocessing(tasks: List[tuple], task_func: Callable) -> List[Any]:
    """
    TODO: 多进程执行任务
    - 创建多个进程执行CPU密集型任务
    - 分配任务到不同进程
    - 收集所有进程结果
    """
    pass


# =============================================================================
# 5. 进程间通信
# =============================================================================

class ProducerConsumerMP:
    """
    TODO: 多进程生产者-消费者模式
    - 使用 multiprocessing.Queue 进行进程间通信
    - 支持多个生产者和消费者进程
    """
    
    def __init__(self, num_producers: int = 2, num_consumers: int = 2):
        self.num_producers = num_producers
        self.num_consumers = num_consumers
        self.queue = multiprocessing.Queue(maxsize=10)
        self.result_queue = multiprocessing.Queue()
    
    def producer(self, producer_id: int, items: List[Any]) -> None:
        """TODO: 生产者进程"""
        pass
    
    def consumer(self, consumer_id: int) -> None:
        """TODO: 消费者进程"""
        pass
    
    def run(self, items_per_producer: List[List[Any]]) -> List[Any]:
        """TODO: 运行生产者-消费者系统"""
        pass


def shared_memory_example():
    """
    TODO: 共享内存示例
    - 使用 multiprocessing.Manager 创建共享对象
    - 演示多进程访问共享数据
    - 展示同步机制
    """
    pass


def pipe_communication_example():
    """
    TODO: 管道通信示例
    - 使用 multiprocessing.Pipe 进行双向通信
    - 在父子进程间传递数据
    """
    pass


# =============================================================================
# 6. 进程池执行器
# =============================================================================

def demonstrate_process_pool():
    """
    TODO: 演示进程池的使用
    - 使用 ProcessPoolExecutor 执行CPU密集型任务
    - 比较不同进程数的性能
    - 处理进程间的数据传递
    """
    pass


def parallel_computation(numbers: List[int], 
                        computation: Callable[[int], int]) -> List[int]:
    """
    TODO: 并行计算
    - 使用进程池并行处理数字列表
    - 支持自定义计算函数
    - 比较串行和并行的性能
    """
    pass


def monte_carlo_pi(num_samples: int, num_processes: int = None) -> float:
    """
    TODO: 蒙特卡洛法计算π
    - 使用多进程并行采样
    - 将工作分配到多个进程
    - 汇总所有进程的结果
    """
    pass


# =============================================================================
# 7. concurrent.futures 统一接口
# =============================================================================

def unified_executor_demo():
    """
    TODO: 统一执行器演示
    - 使用相同的代码处理ThreadPoolExecutor和ProcessPoolExecutor
    - 比较线程池和进程池的性能差异
    - 展示future对象的使用
    """
    pass


class TaskExecutor:
    """
    TODO: 任务执行器
    - 自动选择合适的执行器（线程池或进程池）
    - 根据任务类型优化性能
    """
    
    def __init__(self, max_workers: int = None):
        self.max_workers = max_workers
    
    def execute_io_tasks(self, tasks: List[Callable]) -> List[Any]:
        """TODO: 执行IO密集型任务"""
        pass
    
    def execute_cpu_tasks(self, tasks: List[Callable]) -> List[Any]:
        """TODO: 执行CPU密集型任务"""
        pass
    
    def execute_mixed_tasks(self, 
                           io_tasks: List[Callable], 
                           cpu_tasks: List[Callable]) -> Dict[str, List[Any]]:
        """TODO: 执行混合任务"""
        pass


# =============================================================================
# 8. 性能基准测试
# =============================================================================

@dataclass
class BenchmarkResult:
    """
    TODO: 基准测试结果
    - 记录执行时间、吞吐量等指标
    """
    execution_time: float
    task_count: int
    throughput: float
    method: str


def benchmark_concurrency():
    """
    TODO: 并发性能基准测试
    - 比较顺序、多线程、多进程的性能
    - 测试IO密集型和CPU密集型任务
    - 生成性能报告
    """
    pass


def find_optimal_workers(task_func: Callable, 
                        tasks: List[Any], 
                        max_workers: int = 20) -> Dict[str, Any]:
    """
    TODO: 寻找最优工作者数量
    - 测试不同工作者数量的性能
    - 找到最佳的线程/进程数量
    - 返回优化建议
    """
    pass


# =============================================================================
# 9. 实际应用案例
# =============================================================================

class WebScraper:
    """
    TODO: 网络爬虫示例
    - 使用多线程并发抓取网页
    - 实现请求限流和重试机制
    - 处理异常和超时
    """
    
    def __init__(self, max_workers: int = 10, delay: float = 0.1):
        self.max_workers = max_workers
        self.delay = delay
        self.session_data = {}
    
    def fetch_url(self, url: str) -> Dict[str, Any]:
        """TODO: 抓取单个URL"""
        pass
    
    def fetch_urls(self, urls: List[str]) -> List[Dict[str, Any]]:
        """TODO: 批量抓取URL"""
        pass


class DataProcessor:
    """
    TODO: 数据处理器
    - 使用多进程处理大数据集
    - 支持分块处理和进度监控
    """
    
    def __init__(self, chunk_size: int = 1000):
        self.chunk_size = chunk_size
    
    def process_data(self, data: List[Any], 
                    processor: Callable) -> List[Any]:
        """TODO: 处理数据"""
        pass
    
    def process_file(self, file_path: str, 
                    processor: Callable) -> List[Any]:
        """TODO: 处理文件"""
        pass


# =============================================================================
# 10. 错误处理和最佳实践
# =============================================================================

class ThreadSafeLogger:
    """
    TODO: 线程安全的日志记录器
    - 支持多线程环境下的日志记录
    - 避免日志混乱
    """
    
    def __init__(self, log_file: str = None):
        self.log_file = log_file
        self.lock = threading.Lock()
    
    def log(self, message: str, level: str = "INFO") -> None:
        """TODO: 记录日志"""
        pass


def handle_worker_exceptions():
    """
    TODO: 处理工作者异常
    - 演示如何在多线程/多进程中处理异常
    - 实现优雅的错误恢复机制
    """
    pass


def graceful_shutdown_demo():
    """
    TODO: 优雅关闭演示
    - 实现信号处理
    - 等待所有任务完成
    - 清理资源
    """
    pass


# =============================================================================
# 主程序示例
# =============================================================================

def main():
    """主程序示例"""
    print("=== 线程和多进程示例 ===")
    
    # 性能比较示例
    print("\n1. 性能比较:")
    try:
        # IO密集型任务
        io_tasks = [(0.1, i) for i in range(10)]
        
        seq_time = time.time()
        seq_results = run_sequential(io_tasks, io_bound_task)
        seq_time = time.time() - seq_time
        
        thread_time = time.time()
        thread_results = run_threaded(io_tasks, io_bound_task)
        thread_time = time.time() - thread_time
        
        print(f"顺序执行时间: {seq_time:.2f}s")
        print(f"多线程执行时间: {thread_time:.2f}s")
        print(f"性能提升: {seq_time/thread_time:.2f}x")
    except Exception as e:
        print(f"未实现: {e}")
    
    # 线程同步示例
    print("\n2. 线程同步:")
    try:
        counter = Counter()
        
        def increment_task():
            for _ in range(1000):
                counter.increment_safe()
        
        threads = [threading.Thread(target=increment_task) for _ in range(5)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        
        print(f"计数器最终值: {counter.get_value()}")
    except Exception as e:
        print(f"未实现: {e}")


if __name__ == "__main__":
    main()
    print("\n=== 运行 'python -m exercises.chapter16_threading_multiprocessing' 查看更多示例 ===") 