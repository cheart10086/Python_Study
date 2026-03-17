#邮箱格式检验

mail = input("输入邮箱")

if mail.count("@")==1 and mail.count(".")>=1:
    print("邮箱合法")
else:
    print("邮箱不合法")