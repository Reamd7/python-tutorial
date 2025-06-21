"""
测试第16章：线程和多进程 (Threading & Multiprocessing)
Tests for Chapter 16: Threading and Multiprocessing for Concurrent Programming
"""

import pytest
import time
import threading
import multiprocessing
from unittest.mock import patch, MagicMock

# 导入要测试的模块
try:
    from exercises.chapter16_threading_multiprocessing import (
        SimpleThread, cpu_bound_task, io_bound_task,
        run_sequential, run_threaded, Counter, BoundedBuffer,
        ConnectionPool, demonstrate_thread_pool, batch_download_simulation,
        parallel_file_processing, worker_function, MultiprocessManager,
        run_multiprocessing, ProducerConsumerMP, shared_memory_example,
        pipe_communication_example, demonstrate_process_pool,
        parallel_computation, monte_carlo_pi, unified_executor_demo,
        TaskExecutor, BenchmarkResult, benchmark_concurrency,
        find_optimal_workers, WebScraper, DataProcessor,
        ThreadSafeLogger, handle_worker_exceptions, graceful_shutdown_demo
    )
except ImportError:
    pytest.skip("Chapter 16 module not found", allow_module_level=True)


class TestBasicThreadOperations:
    """测试基础线程操作"""
    
    def test_simple_thread(self):
        """测试简单线程类"""
        try:
            def test_target(x, y):
                return x + y
            
            thread = SimpleThread(test_target, (5, 3), "test_thread")
            thread.start()
            thread.join()
            
            assert thread.result == 8
            assert not thread.is_alive()
        except NotImplementedError:
            pytest.skip("SimpleThread not implemented yet")
    
    def test_cpu_bound_task(self):
        """测试CPU密集型任务"""
        try:
            result = cpu_bound_task(100)
            expected = sum(i * i for i in range(100))
            assert result == expected
        except NotImplementedError:
            pytest.skip("cpu_bound_task not implemented yet")
    
    def test_io_bound_task(self):
        """测试IO密集型任务"""
        try:
            start_time = time.time()
            result = io_bound_task(0.1, 1)
            end_time = time.time()
            
            assert "task" in result.lower()
            assert end_time - start_time >= 0.1
        except NotImplementedError:
            pytest.skip("io_bound_task not implemented yet")
    
    def test_run_sequential_vs_threaded(self):
        """测试顺序执行与多线程执行的比较"""
        try:
            tasks = [(0.05, i) for i in range(4)]
            
            # 顺序执行
            start_time = time.time()
            seq_results = run_sequential(tasks, io_bound_task)
            seq_time = time.time() - start_time
            
            # 多线程执行
            start_time = time.time()
            thread_results = run_threaded(tasks, io_bound_task)
            thread_time = time.time() - start_time
            
            assert len(seq_results) == len(thread_results) == 4
            # 多线程应该更快
            assert thread_time < seq_time
        except NotImplementedError:
            pytest.skip("Sequential/threaded execution not implemented yet")


class TestThreadSynchronization:
    """测试线程同步机制"""
    
    def test_thread_safe_counter(self):
        """测试线程安全计数器"""
        try:
            counter = Counter()
            threads = []
            
            def increment_task():
                for _ in range(100):
                    counter.increment_safe()
            
            # 创建多个线程
            for _ in range(5):
                thread = threading.Thread(target=increment_task)
                threads.append(thread)
                thread.start()
            
            # 等待所有线程完成
            for thread in threads:
                thread.join()
            
            # 线程安全的计数器应该得到正确结果
            assert counter.get_value() == 500
        except NotImplementedError:
            pytest.skip("Counter not implemented yet")
    
    def test_bounded_buffer(self):
        """测试有界缓冲区"""
        try:
            buffer = BoundedBuffer(capacity=3)
            
            # 添加项目
            buffer.put("item1")
            buffer.put("item2")
            assert buffer.size() == 2
            
            # 获取项目
            item = buffer.get()
            assert item == "item1"
            assert buffer.size() == 1
        except NotImplementedError:
            pytest.skip("BoundedBuffer not implemented yet")
    
    def test_connection_pool(self):
        """测试连接池"""
        try:
            pool = ConnectionPool(max_connections=3)
            
            # 获取连接
            conn1 = pool.acquire_connection()
            conn2 = pool.acquire_connection()
            
            assert "Connection-" in conn1
            assert "Connection-" in conn2
            assert conn1 != conn2
            
            # 释放连接
            pool.release_connection(conn1)
            
            # 再次获取应该得到释放的连接
            conn3 = pool.acquire_connection()
            assert conn3 == conn1
        except NotImplementedError:
            pytest.skip("ConnectionPool not implemented yet")


class TestThreadPoolExecutor:
    """测试线程池执行器"""
    
    def test_demonstrate_thread_pool(self):
        """测试线程池演示"""
        try:
            demonstrate_thread_pool()
            # 如果能运行完成就算成功
            assert True
        except NotImplementedError:
            pytest.skip("demonstrate_thread_pool not implemented yet")
    
    def test_batch_download_simulation(self):
        """测试批量下载模拟"""
        try:
            urls = [f"http://example.com/page{i}" for i in range(3)]
            results = batch_download_simulation(urls)
            
            assert len(results) == 3
            assert all('url' in result for result in results)
        except NotImplementedError:
            pytest.skip("batch_download_simulation not implemented yet")
    
    def test_parallel_file_processing(self):
        """测试并行文件处理"""
        try:
            import tempfile
            import os
            
            # 创建临时文件
            temp_files = []
            for i in range(3):
                with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
                    f.write(f"content {i}")
                    temp_files.append(f.name)
            
            try:
                def file_processor(filepath):
                    with open(filepath, 'r') as f:
                        return f.read()
                
                results = parallel_file_processing(temp_files, file_processor)
                assert len(results) == 3
                assert all('content' in str(result) for result in results)
            finally:
                # 清理临时文件
                for filepath in temp_files:
                    if os.path.exists(filepath):
                        os.unlink(filepath)
        except NotImplementedError:
            pytest.skip("parallel_file_processing not implemented yet")


class TestMultiprocessing:
    """测试多进程"""
    
    def test_multiprocess_manager(self):
        """测试多进程管理器"""
        try:
            manager = MultiprocessManager(num_processes=2)
            
            # 启动工作进程
            manager.start_workers()
            
            # 提交任务
            for i in range(5):
                manager.submit_task(i * i)
            
            # 获取结果
            results = manager.get_results(5)
            assert len(results) == 5
            
            # 关闭
            manager.shutdown()
        except NotImplementedError:
            pytest.skip("MultiprocessManager not implemented yet")
    
    def test_run_multiprocessing(self):
        """测试多进程执行"""
        try:
            tasks = [(10,), (20,), (30,)]
            results = run_multiprocessing(tasks, cpu_bound_task)
            
            assert len(results) == 3
            assert all(isinstance(r, int) for r in results)
        except NotImplementedError:
            pytest.skip("run_multiprocessing not implemented yet")


class TestInterProcessCommunication:
    """测试进程间通信"""
    
    def test_producer_consumer_mp(self):
        """测试多进程生产者-消费者模式"""
        try:
            pc = ProducerConsumerMP(num_producers=2, num_consumers=2)
            items_per_producer = [[1, 2, 3], [4, 5, 6]]
            
            results = pc.run(items_per_producer)
            assert len(results) == 6  # 总共6个项目
        except NotImplementedError:
            pytest.skip("ProducerConsumerMP not implemented yet")
    
    def test_shared_memory_example(self):
        """测试共享内存示例"""
        try:
            shared_memory_example()
            # 如果能运行完成就算成功
            assert True
        except NotImplementedError:
            pytest.skip("shared_memory_example not implemented yet")
    
    def test_pipe_communication_example(self):
        """测试管道通信示例"""
        try:
            pipe_communication_example()
            # 如果能运行完成就算成功
            assert True
        except NotImplementedError:
            pytest.skip("pipe_communication_example not implemented yet")


class TestProcessPoolExecutor:
    """测试进程池执行器"""
    
    def test_demonstrate_process_pool(self):
        """测试进程池演示"""
        try:
            demonstrate_process_pool()
            # 如果能运行完成就算成功
            assert True
        except NotImplementedError:
            pytest.skip("demonstrate_process_pool not implemented yet")
    
    def test_parallel_computation(self):
        """测试并行计算"""
        try:
            numbers = [1, 2, 3, 4, 5]
            
            def square(x):
                return x * x
            
            results = parallel_computation(numbers, square)
            expected = [1, 4, 9, 16, 25]
            assert results == expected
        except NotImplementedError:
            pytest.skip("parallel_computation not implemented yet")
    
    def test_monte_carlo_pi(self):
        """测试蒙特卡洛法计算π"""
        try:
            # 使用较少的样本数以加快测试
            pi_estimate = monte_carlo_pi(num_samples=10000, num_processes=2)
            
            # π的估计值应该在合理范围内
            assert 2.5 < pi_estimate < 3.5
        except NotImplementedError:
            pytest.skip("monte_carlo_pi not implemented yet")


class TestUnifiedInterface:
    """测试统一接口"""
    
    def test_unified_executor_demo(self):
        """测试统一执行器演示"""
        try:
            unified_executor_demo()
            # 如果能运行完成就算成功
            assert True
        except NotImplementedError:
            pytest.skip("unified_executor_demo not implemented yet")
    
    def test_task_executor(self):
        """测试任务执行器"""
        try:
            executor = TaskExecutor(max_workers=2)
            
            # IO密集型任务
            io_tasks = [lambda: time.sleep(0.01) or "io_result" for _ in range(3)]
            io_results = executor.execute_io_tasks(io_tasks)
            assert len(io_results) == 3
            
            # CPU密集型任务
            cpu_tasks = [lambda x=i: x * x for i in range(3)]
            cpu_results = executor.execute_cpu_tasks(cpu_tasks)
            assert len(cpu_results) == 3
        except NotImplementedError:
            pytest.skip("TaskExecutor not implemented yet")


class TestPerformanceBenchmarking:
    """测试性能基准测试"""
    
    def test_benchmark_result(self):
        """测试基准测试结果"""
        try:
            result = BenchmarkResult(
                execution_time=1.5,
                task_count=10,
                throughput=6.67,
                method="threading"
            )
            
            assert result.execution_time == 1.5
            assert result.task_count == 10
            assert result.method == "threading"
        except NotImplementedError:
            pytest.skip("BenchmarkResult not implemented yet")
    
    def test_benchmark_concurrency(self):
        """测试并发性能基准测试"""
        try:
            benchmark_concurrency()
            # 如果能运行完成就算成功
            assert True
        except NotImplementedError:
            pytest.skip("benchmark_concurrency not implemented yet")
    
    def test_find_optimal_workers(self):
        """测试寻找最优工作者数量"""
        try:
            def simple_task(x):
                return x * 2
            
            tasks = [i for i in range(10)]
            result = find_optimal_workers(simple_task, tasks, max_workers=4)
            
            assert 'optimal_workers' in result
            assert 'performance_data' in result
        except NotImplementedError:
            pytest.skip("find_optimal_workers not implemented yet")


class TestPracticalApplications:
    """测试实际应用案例"""
    
    def test_web_scraper(self):
        """测试网络爬虫"""
        try:
            scraper = WebScraper(max_workers=2, delay=0.01)
            
            # 模拟URL
            urls = ["http://example.com/page1", "http://example.com/page2"]
            
            # 由于是模拟，我们只测试是否能创建实例
            assert scraper.max_workers == 2
            assert scraper.delay == 0.01
        except NotImplementedError:
            pytest.skip("WebScraper not implemented yet")
    
    def test_data_processor(self):
        """测试数据处理器"""
        try:
            processor = DataProcessor(chunk_size=100)
            
            # 测试基本属性
            assert processor.chunk_size == 100
            
            # 简单的处理函数
            def double_value(x):
                return x * 2
            
            data = [1, 2, 3, 4, 5]
            results = processor.process_data(data, double_value)
            expected = [2, 4, 6, 8, 10]
            assert results == expected
        except NotImplementedError:
            pytest.skip("DataProcessor not implemented yet")


class TestErrorHandlingAndBestPractices:
    """测试错误处理和最佳实践"""
    
    def test_thread_safe_logger(self):
        """测试线程安全的日志记录器"""
        try:
            import tempfile
            import os
            
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
                log_file = tmp.name
            
            try:
                logger = ThreadSafeLogger(log_file)
                
                # 多线程日志记录
                def log_task(thread_id):
                    for i in range(5):
                        logger.log(f"Thread {thread_id} - Message {i}")
                
                threads = []
                for i in range(3):
                    thread = threading.Thread(target=log_task, args=(i,))
                    threads.append(thread)
                    thread.start()
                
                for thread in threads:
                    thread.join()
                
                # 检查日志文件是否存在
                assert os.path.exists(log_file)
            finally:
                if os.path.exists(log_file):
                    os.unlink(log_file)
        except NotImplementedError:
            pytest.skip("ThreadSafeLogger not implemented yet")
    
    def test_handle_worker_exceptions(self):
        """测试工作者异常处理"""
        try:
            handle_worker_exceptions()
            # 如果能运行完成就算成功
            assert True
        except NotImplementedError:
            pytest.skip("handle_worker_exceptions not implemented yet")
    
    def test_graceful_shutdown_demo(self):
        """测试优雅关闭演示"""
        try:
            graceful_shutdown_demo()
            # 如果能运行完成就算成功
            assert True
        except NotImplementedError:
            pytest.skip("graceful_shutdown_demo not implemented yet")


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 