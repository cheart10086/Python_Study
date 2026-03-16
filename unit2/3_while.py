#while语法结构
#while 条件表达式：
#   循环体语句...
#for语法结构
#for 元素 in 待处理数据集:
#   循环体代码
#遍历字符串

str = "hello"
for i in str:
    print(i,end=" ")#print自带换行效果，每次调用都会另起一行输出
    #使用end，使print以空字符串结束，默认为\n
#range(end)生成从0开始到end的数字序列，不包括end本身
range(10)