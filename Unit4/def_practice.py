"""
案例2:定义一个用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额的函数具体规则如下:
1.优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
2.积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元(且抵扣金额不能超过商品总价，积分只能整百抵扣)。

"""
#参数信息不确定，使用不定长参数
#函数的类型注解，需要在形参后进行类型注解
def sum_prize(*args: list[str,float,int],coupen = 0,score = 0,express = 0) ->float:#返回值为float
    """
    :param args:商品信息(商品名，价格，数量)
    :param coupen:优惠券
    :param score: 积分
    :param express:运费
    :return:订单总金额 = 商品总金额 + 运费 -优惠
    """
#1.计算总金额
    total_price = [goods[1]*goods[2] for goods in args]#利用列表推导式将商品的总价格形成一个列表
    total_cost = sum(total_price)
#2，计算优惠
    if total_cost>=5000 and coupen<=total_cost:
        total_cost -= coupen
#3，计算积分抵扣
    if total_cost>5000 and (score//100)<=total_cost:
        total_cost -= (score//100)
#4.添加运费
    total_cost += express

    return total_cost

#类型注解：用于明确变量，函数参数和返回值的数据类型
a:int = 100

total_cost = sum_prize(("鼠标",188.2,50),("键盘",388,100),("电脑",100,100),coupen=500,express=50,score=1000)
print(total_cost)
