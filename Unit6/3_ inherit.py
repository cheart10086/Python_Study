#单继承 class 类名(继承的类名)

class NFC:
    NFC_type = "第五代"
    Producer = "samsung"
class Phone:
    __is__4g__enable:bool = False
    IEMI = None #序列号
    Producer = "xiaomi" #制造商
    def __init__(self):
        pass
    def __check_4g(self):
        if self.__is__4g__enable:
            print("4g开启")
        else: print("4g关闭")

    def call_by_4g(self):
        self.__check_4g()
        print("正在通话中")

class NewPhone(Phone):
    face_id = "1001" #面部识别ID

    def call_by_5g(self):
        print("5g通话")

phone = NewPhone()
phone.call_by_4g()

#多继承
#复写：重写父类成员的方法
#如果要调用父类的方法 使用super或者直接使用父类进行调用
class NewNewPhone(Phone,NFC):
    def call_by_5g(self):
        print("子类的5g通话")
        print(f"父类的{Phone.Producer}")
        print(f"父类的厂商   {super().Producer}")
    pass

p1 = NewNewPhone()
print(p1.Producer)#同名变量，先使用左边的父类
p1.call_by_5g()

