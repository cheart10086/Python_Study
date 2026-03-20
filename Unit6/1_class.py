#定义类,类名的每个单词的首字母都要大写
#class 类名:
#   def __init__(self,参数列表):  self代表创建出来的对象实例
#       self.属性名 = 参数值
#   def 方法名(self,形参列表)
class Car:
    wheel = 4#类属性，通过 类名.属性访问
    def __init__(self,c_brand,c_prize,c_name):
        self.brand :str = c_brand
        self.prize :int= c_prize
        self.name :str = c_name
    def print_num(self,num):
        print(num)
    #魔法方法
    #魔法方法，以双下划线开头和结尾的方法，用于类的特殊行为，python会在合适的时机自动调用
    def __str__(self):
        return f"{self.brand} {self.name} {self.prize}"
    def __eq__(self,other):
        return  self.brand == other.brand and self.prize == other.prize


c1 = Car("xiaomi",100000,"su7")
c2 = Car("xiaomi",200000,"su8")
print(c1 == c2)
print(c1)
#   __dict__用来以字典形式存储对象的属性
#实例属性，每个具体对象的属性，
#类属性，所有实例共享