"""
教务管理系统（学生成绩管理） - 功能需求说明

采用面向对象的编程思想，设计并实现一个简单的教务管理系统。
系统用于管理在校学生的成绩信息，通过控制台菜单与用户交互。

主要功能包括：
1. 添加学生成绩
2. 修改学生成绩
3. 删除学生成绩
4. 查询指定学生成绩
5. 展示全部学生成绩

详细功能描述如下：

1. 添加学生成绩
   1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
   1.2 检查学生姓名是否已存在：如果不存在，则添加；如果已存在，则不重复添加
   1.3 验证各科成绩是否在合法范围（0-100分），超出范围则提示错误
   1.4 创建学生对象，并将其添加到系统中存储的数据结构里

2. 修改学生成绩
   2.1 输入要修改的学生姓名
   2.2 根据姓名查找该学生，若未找到则提示“未找到该学生”
   2.3 输入新的语文、数学、英语成绩
   2.4 验证新成绩范围后，更新该学生的成绩数据

3. 删除学生成绩
   3.1 输入要删除的学生姓名
   3.2 查找并删除对应学生的记录
   3.3 若未找到该学生，则提示“未找到该学生”

4. 查询指定学生成绩
   4.1 输入学生姓名
   4.2 查找并输出该学生的成绩信息
   4.3 输出格式要求为：
        "姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263"

5. 展示全部学生成绩
   5.1 遍历系统中所有学生，依次输出每位学生的成绩信息
   5.2 输出格式同查询功能，每行一个学生
"""
from unittest import case
from pymysql import Connection

class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def total_score(self):
        return self.chinese + self.math + self.english

    def __str__(self):
        return (f"姓名：{self.name} | 语文：{self.chinese} | "
                f"数学：{self.math} | 英语：{self.english} | "
                f"总分：{self.total_score()}")
    def update_score(self,chinese = None,math = None,english = None):#使用默认参数，如果不传入值，则为None
        if chinese is not None:#如果传入的语文成绩不为空
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

class EduManagement(Student):
    sys_version = 1.0
    sys_name = "教务管理系统"

    def __init__(self):
        self.student_list = []

    #添加学生成绩
    def add_student(self):
        name = input("输入学生姓名")

        for s in self.student_list:
            if name == s.name:
                print("学生已经存在")
                return
        chinese = int(input("输入学生语文成绩"))
        math = int(input("输入学生数学成绩"))
        english = int(input("输入学生英语成绩"))
        #
        if 0 <= chinese <=100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("添加成功")
        else:   print("分数错误")

    #更新学生信息
    def update(self):
        name = input("请输入要修改学生的名字")
        for s in self.student_list:
            if s.name == name:
                print(f"{s}")

                chinese = int(input("输入修改后的学生语文成绩"))
                math = int(input("输入修改后的学生数学成绩"))
                english = int(input("输入修改后的学生英语成绩"))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese,math,english)
                    print("成绩修改成功")
                    print(f"修改后的成绩为{s}")
                    return
        print("未找到该学生")

    #删除学生成绩
    def delete_score(self):
        name = input("请输入要删除学生的名字")

        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("删除成功")
                return
        print("未找到学生")

    #查询指定学生成绩
    def find_score(self):
        name = input("请输入要查询学生的名字")

        for s in self.student_list:
            if s.name == name:
                print(f"{s}")
                return
        print("未找到学生")
    def show_score(self):
        for s in self.student_list:
            print(f"{s}")
    def running(self):

        while True:
            print("\t\t\t 教务系统 \t\t\t")
            print("\t\t\t1.添加学生成绩")
            print("\t\t\t2.删除学生成绩")
            print("\t\t\t3.修改学生成绩")
            print("\t\t\t4.查询学生成绩")
            print("\t\t\t5.展示所有学生成绩")
            a = int(input("请输入要使用的功能,输入0时跳出系统\n"))
            match a:
                case 1:
                    self.add_student()
                case 2:
                    self.delete_score()
                case 3:
                    self.update()
                case 4:
                    self.find_score()
                case 5:
                    self.show_score()
                case 0:
                    break
if __name__ == "__main__":
    edu = EduManagement()
    #edu.running()
    #实例化链接
    conn = Connection(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        autocommit=True,
    )

    #print(conn.get_server_info())
    #获取游标对象，通过游标对象执行sql语句
    cursor = conn.cursor()
    #连接到数据库
    #执行非查询性质的sql对象
    conn.select_db("test")

    #execute方法支持任意类型的sql操作
    #cursor.execute("CREATE TABLE students (name VARCHAR(50),chinese int,math int,english int)")
    cursor.execute("INSERT INTO students (name,chinese,math,english) VALUES ('张三',100,100,100)")


    cursor.execute("select * from students")

    #插入数据后，需要使用 连接对象.commit()确认插入数据
    #在连接对象时，可以设置自动提交
    #conn.commit()
    # 得到一个查询返回值
    results = cursor.fetchall()
    print(results)
    #关闭数据库
    conn.close()