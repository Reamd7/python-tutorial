"""
测试第14章：数据类 (Dataclasses)
Tests for Chapter 14: Dataclasses and Modern Data Handling
"""

import pytest
from datetime import datetime, date
import json
import math

# 导入要测试的模块
try:
    from exercises.chapter14_dataclasses import (
        Person, Point, Book, User, Product, ImmutablePoint, Color,
        Rectangle, EmailAddress, DatabaseRecord, Priority, Task,
        Animal, Dog, Cat, Student, Address, PersonWithAddress,
        BankAccount, TraditionalClass, DataclassVersion,
        compare_implementations, dataclass_utilities_demo
    )
except ImportError:
    pytest.skip("Chapter 14 module not found", allow_module_level=True)


class TestBasicDataclasses:
    """测试基础数据类"""
    
    def test_person_dataclass(self):
        """测试Person数据类"""
        try:
            person = Person("Alice", 25, "alice@example.com")
            
            assert person.name == "Alice"
            assert person.age == 25
            assert person.email == "alice@example.com"
            assert person.is_adult() == True
            
            young_person = Person("Bob", 17, "bob@example.com")
            assert young_person.is_adult() == False
        except (NotImplementedError, TypeError):
            pytest.skip("Person dataclass not implemented yet")
    
    def test_point_dataclass(self):
        """测试Point数据类"""
        try:
            point1 = Point(0.0, 0.0)
            point2 = Point(3.0, 4.0)
            
            # 测试距离计算
            distance = point1.distance_to(point2)
            assert distance == 5.0
            
            # 测试移动
            moved_point = point1.move(1.0, 1.0)
            assert moved_point.x == 1.0
            assert moved_point.y == 1.0
        except (NotImplementedError, TypeError):
            pytest.skip("Point dataclass not implemented yet")
    
    def test_book_dataclass(self):
        """测试Book数据类"""
        try:
            book = Book("Python Guide", "Alice", 300, 29.99)
            
            assert book.title == "Python Guide"
            assert book.author == "Alice"
            assert book.pages == 300
            assert book.price == 29.99
            assert book.isbn is None
            assert book.in_stock == True
            
            # 测试带ISBN的书
            book_with_isbn = Book("Advanced Python", "Bob", 500, 39.99, "123-456")
            assert book_with_isbn.isbn == "123-456"
        except (NotImplementedError, TypeError):
            pytest.skip("Book dataclass not implemented yet")


class TestDefaultValuesAndFields:
    """测试默认值和字段配置"""
    
    def test_user_dataclass(self):
        """测试User数据类"""
        try:
            user = User("alice", "alice@example.com")
            
            assert user.username == "alice"
            assert user.email == "alice@example.com"
            assert user.full_name == ""
            assert user.is_active == True
            assert isinstance(user.created_at, datetime)
            assert user.tags == []
            assert user.metadata == {}
            
            # 测试修改列表和字典
            user.tags.append("admin")
            user.metadata["role"] = "user"
            
            # 创建新用户，确保默认值独立
            user2 = User("bob", "bob@example.com")
            assert user2.tags == []
            assert user2.metadata == {}
        except (NotImplementedError, TypeError):
            pytest.skip("User dataclass not implemented yet")
    
    def test_product_dataclass(self):
        """测试Product数据类"""
        try:
            product = Product(1, "Laptop", 1000.0, "Electronics")
            
            assert product.discounted_price() == 1000.0  # 无折扣
            assert product.average_rating() == 0.0  # 无评分
            assert product.is_available() == False  # 无库存
            
            # 带折扣和评分的产品
            product2 = Product(
                2, "Phone", 800.0, "Electronics",
                discount=0.1, stock_count=5,
                review_scores=[4.5, 4.0, 5.0]
            )
            
            assert product2.discounted_price() == 720.0  # 800 * 0.9
            assert product2.average_rating() == 4.5
            assert product2.is_available() == True
        except (NotImplementedError, TypeError):
            pytest.skip("Product dataclass not implemented yet")


class TestFrozenDataclasses:
    """测试不可变数据类"""
    
    def test_immutable_point(self):
        """测试不可变坐标点"""
        try:
            point1 = ImmutablePoint(1.0, 2.0)
            point2 = ImmutablePoint(3.0, 4.0)
            
            # 测试加法
            result = point1 + point2
            assert result.x == 4.0
            assert result.y == 6.0
            
            # 测试标量乘法
            scaled = point1 * 2
            assert scaled.x == 2.0
            assert scaled.y == 4.0
            
            # 测试向量长度
            magnitude = point1.magnitude()
            expected = math.sqrt(1.0**2 + 2.0**2)
            assert abs(magnitude - expected) < 0.001
            
            # 测试不可变性
            with pytest.raises(AttributeError):
                point1.x = 5.0
        except (NotImplementedError, TypeError):
            pytest.skip("ImmutablePoint dataclass not implemented yet")
    
    def test_color_dataclass(self):
        """测试Color数据类"""
        try:
            color = Color(255, 128, 64)
            
            # 测试十六进制转换
            hex_color = color.to_hex()
            assert hex_color.startswith("#")
            assert len(hex_color) == 7
            
            # 测试变亮
            brighter = color.brighten(1.2)
            assert isinstance(brighter, Color)
            
            # 测试变暗
            darker = color.darken(0.8)
            assert isinstance(darker, Color)
        except (NotImplementedError, TypeError):
            pytest.skip("Color dataclass not implemented yet")


class TestPostInit:
    """测试后处理方法"""
    
    def test_rectangle_validation(self):
        """测试Rectangle验证"""
        try:
            # 有效的矩形
            rect = Rectangle(4.0, 3.0)
            assert rect.area() == 12.0
            assert rect.perimeter() == 14.0
            assert rect.is_square() == False
            
            # 正方形
            square = Rectangle(5.0, 5.0)
            assert square.is_square() == True
            
            # 无效的尺寸
            with pytest.raises(ValueError):
                Rectangle(-1.0, 3.0)
            
            with pytest.raises(ValueError):
                Rectangle(4.0, 0.0)
        except (NotImplementedError, TypeError):
            pytest.skip("Rectangle dataclass not implemented yet")
    
    def test_email_validation(self):
        """测试EmailAddress验证"""
        try:
            # 有效邮箱
            email = EmailAddress("alice@example.com")
            assert email.username == "alice"
            assert email.domain == "example.com"
            
            # 无效邮箱
            with pytest.raises(ValueError):
                EmailAddress("invalid-email")
            
            with pytest.raises(ValueError):
                EmailAddress("@example.com")
        except (NotImplementedError, TypeError):
            pytest.skip("EmailAddress dataclass not implemented yet")


class TestAdvancedFieldConfiguration:
    """测试高级字段配置"""
    
    def test_database_record(self):
        """测试DatabaseRecord字段配置"""
        try:
            record1 = DatabaseRecord(1, {"key": "value"})
            record2 = DatabaseRecord(1, {"key": "value"})
            
            # 测试比较（时间字段不参与比较）
            assert record1 == record2
            
            # 测试repr（某些字段不显示）
            repr_str = repr(record1)
            assert "id" in repr_str
            assert "data" in repr_str
        except (NotImplementedError, TypeError):
            pytest.skip("DatabaseRecord dataclass not implemented yet")
    
    def test_task_dataclass(self):
        """测试Task数据类"""
        try:
            task = Task("Complete project")
            
            assert task.priority == Priority.MEDIUM
            assert task.completed == False
            
            # 测试标记完成
            task.mark_completed()
            assert task.completed == True
            
            # 测试添加子任务
            task.add_subtask("Review code")
            assert "Review code" in task.subtasks
            
            # 测试截止日期
            task_with_due = Task("Urgent task", due_date=date.today())
            days = task_with_due.days_until_due()
            assert days == 0
        except (NotImplementedError, TypeError):
            pytest.skip("Task dataclass not implemented yet")


class TestInheritance:
    """测试数据类继承"""
    
    def test_animal_inheritance(self):
        """测试动物类继承"""
        try:
            # 基础动物
            animal = Animal("Generic", "Unknown", 5)
            assert animal.make_sound() == "Some generic animal sound"
            assert "Generic" in animal.info()
            
            # 狗类
            dog = Dog("Buddy", "Canine", 3, "Golden Retriever")
            assert dog.make_sound() == "Woof!"
            assert dog.breed == "Golden Retriever"
            
            trained_dog = Dog("Rex", "Canine", 5, "German Shepherd", True)
            fetch_result = trained_dog.fetch()
            assert "fetch" in fetch_result.lower()
            
            # 猫类
            cat = Cat("Whiskers", "Feline", 2)
            assert cat.make_sound() == "Meow!"
            assert cat.indoor_only == True
            
            hunt_result = cat.hunt()
            assert isinstance(hunt_result, str)
        except (NotImplementedError, TypeError):
            pytest.skip("Animal inheritance not implemented yet")


class TestClassVariables:
    """测试类变量"""
    
    def test_student_class_variables(self):
        """测试学生类变量"""
        try:
            initial_count = Student.total_students
            
            student1 = Student("Alice", "S001")
            assert Student.total_students == initial_count + 1
            
            student2 = Student("Bob", "S002")
            assert Student.total_students == initial_count + 2
            
            # 测试成绩操作
            student1.add_grade(90.0)
            student1.add_grade(85.0)
            assert student1.gpa() == 87.5
            
            # 测试类方法
            count = Student.get_student_count()
            assert count == Student.total_students
        except (NotImplementedError, TypeError):
            pytest.skip("Student dataclass not implemented yet")


class TestJSONSerialization:
    """测试JSON序列化"""
    
    def test_address_serialization(self):
        """测试地址序列化"""
        try:
            address = Address("123 Main St", "Springfield", "IL", "62701")
            
            # 测试字典转换
            addr_dict = address.to_dict()
            assert addr_dict["street"] == "123 Main St"
            assert addr_dict["city"] == "Springfield"
            
            # 测试从字典创建
            new_address = Address.from_dict(addr_dict)
            assert new_address.street == address.street
            assert new_address.city == address.city
            
            # 测试JSON序列化
            json_str = address.to_json()
            assert isinstance(json_str, str)
            
            # 测试从JSON创建
            from_json = Address.from_json(json_str)
            assert from_json.street == address.street
        except (NotImplementedError, TypeError):
            pytest.skip("Address serialization not implemented yet")
    
    def test_person_with_address_serialization(self):
        """测试带地址的人员序列化"""
        try:
            address = Address("456 Oak Ave", "Chicago", "IL", "60601")
            person = PersonWithAddress("John Doe", 30, "john@example.com", address)
            
            # 测试嵌套序列化
            person_dict = person.to_dict()
            assert "address" in person_dict
            assert isinstance(person_dict["address"], dict)
            
            # 测试从字典恢复
            restored = PersonWithAddress.from_dict(person_dict)
            assert restored.name == person.name
            assert restored.address.city == person.address.city
        except (NotImplementedError, TypeError):
            pytest.skip("PersonWithAddress serialization not implemented yet")


class TestDataValidation:
    """测试数据验证"""
    
    def test_bank_account_validation(self):
        """测试银行账户验证"""
        try:
            # 有效账户
            account = BankAccount("ACC123", 1000.0, "John Doe")
            assert account.balance == 1000.0
            
            # 存款
            account.deposit(500.0)
            assert account.balance == 1500.0
            
            # 取款
            success = account.withdraw(200.0)
            assert success == True
            assert account.balance == 1300.0
            
            # 余额不足的取款
            success = account.withdraw(2000.0)
            assert success == False
            assert account.balance == 1300.0
            
            # 转账
            target_account = BankAccount("ACC456", 500.0, "Jane Doe")
            success = account.transfer_to(target_account, 300.0)
            assert success == True
            assert account.balance == 1000.0
            assert target_account.balance == 800.0
            
            # 无效参数测试
            with pytest.raises(ValueError):
                BankAccount("", 100.0, "John")  # 空账户号
            
            with pytest.raises(ValueError):
                BankAccount("ACC789", -100.0, "John")  # 负余额
        except (NotImplementedError, TypeError):
            pytest.skip("BankAccount validation not implemented yet")


class TestPerformanceComparison:
    """测试性能比较"""
    
    def test_traditional_vs_dataclass(self):
        """测试传统类与数据类的比较"""
        try:
            # 传统类
            trad = TraditionalClass("test", 42, ["a", "b"])
            assert trad.name == "test"
            assert trad.value == 42
            
            # 数据类
            dc = DataclassVersion("test", 42, ["a", "b"])
            assert dc.name == "test"
            assert dc.value == 42
            
            # 测试相等性
            trad2 = TraditionalClass("test", 42, ["a", "b"])
            dc2 = DataclassVersion("test", 42, ["a", "b"])
            
            assert trad == trad2  # 传统类应该实现__eq__
            assert dc == dc2  # 数据类自动实现
            
            # 测试字符串表示
            assert "test" in str(trad)
            assert "test" in str(dc)
        except (NotImplementedError, TypeError):
            pytest.skip("Performance comparison classes not implemented yet")
    
    def test_utility_functions(self):
        """测试实用工具函数"""
        try:
            # 测试比较函数
            compare_implementations()
            
            # 测试工具演示
            dataclass_utilities_demo()
        except (NotImplementedError, TypeError):
            pytest.skip("Utility functions not implemented yet")


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 