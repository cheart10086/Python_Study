#模式匹配 match case
day = input("请输入星期几（1-7）")

match day:
    case "1":
        print("周一")
    case "2":
        print("周一")
    case "3":
        print("周一")
    case "4":
        print("周一")
    case "5":
        print("周一")
    case "6"|"7":#|表示或的关系
        print("周末")
    case _:#其它匹配情况
        print("输入错误")
#case后还可以嵌套判断语句if
