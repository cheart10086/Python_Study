#字符串切片与列表相同

#正向索引和反向索引
str = "hello"
print(str[4])
print((str[-1]))

#字符串不可修改
for i in str:
    print(i,end=" ")

#切片
#字符串[开始索引:结束索引:步长]
#开始索引默认为0，结束索引默认为列表长度，步长默认为1
print(str[0:4:1])

#字符串翻转
print(f"字符串翻转结果：{str[::-1]}")

#字符串不可变，调用所有字符串方法都不会对字符串进行改变，所有方法返回的是一个新字符串

# 1. find(sub)：查找子串 sub 第一次出现的位置，找不到返回 -1
index_of_l = str.find('l')
print(f"find('l') → 'l' 首次出现在索引: {index_of_l}")

# 2. count(sub)：统计子串 sub 在字符串中出现的次数
count_l = str.count('l')
print(f"count('l') → 'l' 出现了 {count_l} 次")

# 3. upper()：将字符串中所有字母转换为大写（不影响非字母字符）
upper_s = str.upper()
print(f"upper() → 转换为大写: '{upper_s}'")

# 4. lower()：将字符串中所有字母转换为小写
lower_s = str.lower()
print(f"lower() → 转换为小写: '{lower_s}'")

# 5. split(sep=None)：按指定分隔符 sep 拆分字符串，返回列表
#    默认按任意空白字符分割；若指定 sep，则按该字符分割
split_by_l = str.split('l')  # 按 'l' 分割
print(f"split('l') → 按 'l' 拆分: {split_by_l}")

# 6. strip(chars=None)：移除字符串首尾的空白字符或指定字符 chars
#    注意：只删除两端，且 chars 中的任意字符都会被移除（顺序无关）
stripped = str.strip('ho')  # 移除开头的 'h' 和结尾的 'o'
print(f"strip('ho') → 移除首尾的 h/o: '{stripped}'")

# 7. replace(old, new, count=-1)：将子串 old 替换为 new
#    count 指定最多替换次数，-1 表示全部替换
replaced = str.replace('l', 'X')
print(f"replace('l', 'X') → 所有 'l' 替换为 'X': '{replaced}'")

# 8. startswith(prefix)：检查字符串是否以 prefix 开头，返回 True/False
starts_with_h = str.startswith('h')
print(f"startswith('h') → 是否以 'h' 开头? {starts_with_h}")