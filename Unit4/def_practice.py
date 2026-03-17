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