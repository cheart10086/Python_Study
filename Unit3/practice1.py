num_list = []
for i in range(10):
    num = int(input("输入数据"))
    num_list.append(num)
    num_list.sort()
print(f"最小值为{num_list[0]}")
print(f"最大值为{num_list[9]}")