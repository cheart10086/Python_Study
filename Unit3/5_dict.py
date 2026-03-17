#dict中存储的是键值对(key:value)
#键不可重复，可修改,重复后后面的值会覆盖前面的值
#key必须为不可变类型，value可为任意类型
dict1 = {"张三":88,"李四": 76,"王五":95}
print(dict1 )
print(dict1["张三"])
dict1["张三"] = 100
print(dict1["张三"])

#字典添加
dict1["王五"]=90

#字典删除,pop返回删除的键值对的值
num = dict1.pop("王五")
print(num)
del dict1["张三"]
print(dict1)

#修改
dict1["李四"] = 100
print(dict1)

dict1.keys()#获得所有的键
for k in dict1.keys():
    print(f"{dict1[k]}")

dict1.values()#获得所有的值
dict1.items()#获得所有的键值对