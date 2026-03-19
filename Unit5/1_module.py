#一个.py文件就是一个module，是python程序中的基本组织单位
#使用import 模块名进行
# =============================
# 方法一：import 模块名
# =============================
import random, os  # 导入整个模块（多个模块可用逗号分隔）
# 使用方式：模块名.功能名
print(random.randint(10, 100))  # 从 10 到 100 中随机选一个整数
print(os.getcwd())              # 获取当前工作目录

# =============================
# 方法二：import 模块名 as 别名
# =============================
import random as rd  # 给模块起别名（避免命名冲突或简化书写）
# 使用方式：别名.功能名
print(rd.randint(10, 100))  # 等价于 random.randint()

# =============================
# 方法三：from 模块名 import 功能名
# =============================
from random import randint, choice  # 导入指定函数（不需要加模块名）
# 使用方式：直接调用函数名
print(randint(10, 100))   # 直接使用 randint
print(choice(['a', 'b', 'c']))  # 随机选择一个元素

# =============================
# 方法四：from 模块名 import 功能名 as 别名
# =============================
from random import randint as rint  # 给函数起别名（避免重名）
# 使用方式：别名
print(rint(10, 100))  # 等价于 randint(10, 100)

# =============================
# 方法五：from 模块名 import *
# =============================
from random import *  # 导入模块中所有公共函数（不推荐，容易污染命名空间）
# 使用方式：直接调用函数名
print(randint(10, 100))  # 可以直接用
print(choice(['x', 'y']))  # 也可以直接用
#方法3-5可以直接使用功能名，功能可以是函数，变量，方法
# ⚠️ 注意：这种方式可能导致命名冲突（如两个模块都有 randint）

#当只使用其他模块的一个方法时，需使用__name__
#否则在导入后，会将模块其它方法一起执行
import fun #python模块名必须为标识符

if __name__ == "__main__":
    fun.print_num(10)
    print(fun.__name__)