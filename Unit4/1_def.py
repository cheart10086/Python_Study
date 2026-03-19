#函数定义
#def 函数名(参数列表):
    #函数体
#函数有多个返回值，则使用","相隔
#多个返回值返回的为元组
def circle_area(r):
    return 3.14*r*r,r

a = circle_area(10)

area,r1 = circle_area(12)#使用解包
print(a)
print(type(a))

ss = 1000
def find(str):
    global ss#告诉解释器，使用的是全局变量

    count = 0
    for a in str:
        if a in "aeiou":
            count+=1
    return count

num = find("abcdef")
print(num)

#默认参数,在定义函数时直接定义,北京为默认值
def register(name,age,home="北京"):
    print(f"{name}")
register("jam",17)

#不定长参数，用于函数定义或者调用时不确定的参数个数
#为位置传参
#定义不定长参数，使用*args,只为形参名，不为关键字，可以为其它名字
def print_num(*args):
    print(args)
    print(type(args))
print_num(1,2,3,4,5,56,6)

#使用关键字传参,使用**kwargs
def print_dict(**kwargs):
    print(kwargs)
    kwargs.get("num")
    print(type(kwargs))
print_dict(num = 1,str = "hello")

#函数传参也可以传递函数名
def add_num(x,y):
    return x+y
def use(x, y ,oper):
    return(oper(x,y))

sju =  use(1,2,add_num)
print(sju)
