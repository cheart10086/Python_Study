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