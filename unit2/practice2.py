name = input("请输入用户名")
name1 = "admin"
name2 = "zhangsan"
name3 = "taoge"

secret = input("请输入密码")
secret1 = "666888"
secret2 = "123456"
secret3 = "888666"
while not((name == name1 or name == name1 or name == name1)
    and(secret ==secret1 or secret ==secret2 or secret ==secret3)):
    print("输入有误")
    name = input("请输入用户名")
    secret = input("请输入密码")

print("登录成功！")