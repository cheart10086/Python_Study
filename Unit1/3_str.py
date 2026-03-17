#字符串定义
#双引号定义
s1 = "hello"

#单引号定义
s2 = 'world'

#三引号定义
s3 = '''
congratulation!!
'''
#在”“和‘’之间输出”和‘需要使用转义字符，\',\"
#字符串拼接
s4 = "he""is"
s5 = "she"+"is\n"#+只可以拼接字符串
print(s4,s5)

#字符串格式化.使用占位符
name = "jam"
age = 18.2
pro = "cs"
print("我的名字是%s，我今年%f，我的专业是%s\n " %(name,age,pro))
#通过f"内容{变量/表达式}替代"
#可在{}中变量后使用“:”来修饰变量
#age:.1f表示保留一位小数
print(f"我的名字是{name}，我今年{age:.1f}，我的专业是{pro}")

