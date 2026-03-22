
class Phone:
    __is__5g__enable:bool = False
    def __init__(self):
        pass
    def __check_5g(self):
        if self.__is__5g__enable:
            print("5g开启")
        else: print("5g关闭，使用4g网络")

    def cal_by_5g(self):
        self.__check_5g()
        print("正在通话中")

if __name__ == '__main__':
    phone = Phone()
    phone.cal_by_5g()