#使用__all__可以在调用当前模块时，from 模块 import *，则调用的是__all__这个列表中的    内容
__all__ = ["print_num","PI"]
PI = 3.14

def print_num(num):
    print(num)

if __name__ == "__main__":
    print("我是fun,py的输出")