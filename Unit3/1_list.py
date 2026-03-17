#列表使用[],使用","分隔，且可以存储不同类型的元素
#元素有序，可重复，可以修改
#类似于C语言中的数组
#正向索引第一个为开始为0.反向索引从后向前，从最后一个开始为-1
s = [1,2,3,4,"hello"]
print(s)

#获取元素
print(s[0])
print(s[-5])

#修改
s[2] = "shw"
print(s[2])

#删除
del s[2]
print(s)

#遍历
for i in s:
    print(i,end=" ")

#切片：对操作的数据截取其中一部分的操作
#语法 序列数据[开始索引:结束索引:步长]
#不包含结束索引的元素，开始索引默认为开始，结束索引默认为列表长度，步长默认为1
#也可使用反向索引
a = [1,2,6,7,3,4,5,6,7]
print(a[:5:1])
print(a[:5:])
print(a[:5])#步长前的：可删除

#append()添加元素，在末尾添加
a.append(8)
print(a)

#insert(索引，数据)，在指定索引之前添加数据
a.insert(0,1)
print(a)

#remove(数据)，删除匹配的第一个元素
a.remove(1)
print(a)

#pop(索引)，删除索引位置的元素，默认为最后一个
a.pop(1)
print(a)

#sort()
a.sort()
print(a)

num = len(a)#求长度

if num in a:#判断num是否在a中
    print(num)

#合并列表
num_list1 = [1,3,5,7,9]
num_list2 = [2,4,6,8,0]
#解包，将列表这一类容器解开成一个一个独立的元素
#使用*进行解包
num_list = [*num_list1,*num_list2]
#也可使用num_list=num_list1+num_list2