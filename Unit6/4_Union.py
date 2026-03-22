from typing import Union
#Union表示联合类型，描述混合类型的数据容器

my_list:list[Union[str,int]] = [1,1,1,2,'sjhssjh']
print(my_list)

def func(*args:Union[str,int]) -> Union[int,str]:#返回值为int或float
    return args[1]+args[2]

if __name__ == '__main__':
    print(func(1.2,2.3,3))
    print(func(1,2,3))