#集合会自动去重不会存储相同的元素
#集合使用{}定义
#无序，不可重复，可修改
s = {1,2,3,4,1,4}
print(s)

#定义空集合
s3 = set()
# 初始化两个集合
s1 = {'a', 'b', 'c', 'd'}
s2 = {'c', 'd', 'e', 'f'}

print("初始集合:")
print(f"s1: {s1}")
print(f"s2: {s2}")

# 1. add(): 添加元素
s1.add('t')
print(f"\nadd('t') 后: {s1}")

# 2. remove(): 移除指定元素（注意异常）
try:
    s1.remove('b')
    print(f"remove('b') 后: {s1}")
except KeyError:
    print("元素不存在，无法移除")

# 3. pop(): 随机弹出一个元素
popped = s1.pop()
print(f"pop() 弹出: {popped}, 剩余: {s1}")

# 4. clear(): 清空集合
s1.clear()
print(f"clear() 后: {s1}")

# 5. difference(): 差集
s1 = {'a', 'b', 'c', 'd'}
s2 = {'c', 'd', 'e', 'f'}
diff = s1.difference(s2)#在集合s1，不在s2
print(f"\ndifference(): {diff}")

# 6. union(): 并集
uni = s1.union(s2)
print(f"union(): {uni}")

# 7. intersection(): 交集
inter = s1.intersection(s2)
print(f"intersection(): {inter}")