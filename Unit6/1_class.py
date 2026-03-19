#定义类,类名的每个单词的首字母都要大写
#class 类名:
#   def __init__(self,参数列表):  self代表创建出来的对象实例
#       self.属性名 = 参数值
#   def 方法名(self,形参列表)
class Car:
    def __int__(self,c_brand,c_prize,c_name):
        self.brand = c_brand
        self.prize = c_prize
        self.name = c_name
    def print_num(self,num):
        print(num)
car = Car()
car.brand = "xiaomi"
print(car.__dict__)

c1 = Car
a = 10
c1.print_num(a)
#   __dict__用来以字典形式存储对象的属性