#定义私有成员变量和私有成员方法，使变量名和方法名前添加”__“

#私有成员法被类对象使用，但是可以被其他成员使用

class Phone:
    __current_number = 0

    def __init__(self):
        pass
    def get_current_number(self):
        print(self.__current_number)

    def change_current_number(self, new_number):
        self.__current_number = new_number

    def __keep_single(self):
        print("使手机单核运行")

    def change_state(self):
        if self.__current_number == 0:
            self.__keep_single()

if __name__ == '__main__':
    p1 = Phone()
    p1.change_state()