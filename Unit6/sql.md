# 数据库SQL语句
## 数据库的创建
### 1.创建数据库
    create database 数据库名
### 2.删除数据库
    drop database 数据库名
### 3.使用数据库
    use 数据库名
### 4. 查看所有数据库
    show databases
## 表的增删改查
### 1.创建表
    创建学生表
    CREATE TABLE students (
        id INT PRIMARY KEY AUTO_INCREMENT,  
        name VARCHAR(50),
        age INT,
    );
### 2.查看表结构
    SHOW COLUMNS FROM students;
### 3.修改表结构
    
### 4.删除表
    DROP TABLE students;                -- 删除表（含数据）
    DROP TABLE IF EXISTS students;     -- 如果存在才删除（安全写法）
### 5.查看所有表
    SHOW TABLES;
## 数据的增删改查
### 1.插入数据
#### 插入单条记录
    INSERT INTO students (id name, age, email) 
    VALUES ('张三', 18, 'zhangsan@example.com');
#### 插入多条记录
    INSERT INTO students (name, age, email) 
    VALUES 
        ('李四', 19, 'lisi@example.com'),
        ('王五', 20, 'wangwu@example.com');
### 2.删除数据
    DELETE FROM students WHERE age < 16;
### 3.更新数据
    UPDATE students 
    SET email = 'new@example.com' 
    WHERE name = '张三';   
    --将 students 表中 所有姓名为“张三”的记录的 email 字段更新为 'new@example.com'
### 4.查询出具
    SELECT * FROM students;                  -- 查询所有列
    SELECT name, age FROM students;          -- 查询指定列
    SELECT name AS 姓名, age AS 年龄 FROM students; -- 别名