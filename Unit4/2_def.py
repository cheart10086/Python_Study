#匿名函数
#使用lambda关键字,将函数的结果直接赋值给一个变量
#lambda 参数列表:函数体
#只适用于单行函数
#可以不返回结果
add = lambda x,y:x+y

#匿名函数可以当做高阶函数的输入值
#sort的key是用作排序依据，以哪一种方式进行排序，匿名函数会为key提供一个列表
students = [('张三', 85), ('李四', 92), ('王五', 78)]
students.sort(key=lambda x: x[1])  # 按分数排序
print(students)

