#try:
    # 可能会引发异常的代码
# except 异常类型 as 变量名:
#     捕获并处理特定异常
# else:
#     如果没有异常发生，执行这里的代码（可选）
# finally:
#     无论是否发生异常，都会执行的代码（可选）


try:
    math.sqrt()
except NameError:
    print("未找到模块")
finally:
    print("end")