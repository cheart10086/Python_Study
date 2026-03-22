#多态：使用不同的行为例如函数，传入不同的对象时，得到不同的结果

class Animal:
    def speak(self):
        pass
#父类是空实现
#具体方法实现，由子类确定

class Dog(Animal):
    def speak(self):
        print('I am dog.')

class Cat(Animal):
    def speak(self):
        print('I am cat.')

def speak(animal:Animal):
    animal.speak()

if __name__ == '__main__':

    dog = Dog()
    speak(dog)
    cat = Cat()
    speak(cat)