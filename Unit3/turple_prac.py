students = (
    ("张三", 88, 92, 85),
    ("李四", 76, 85, 90),
    ("王五", 95, 88, 93),
    ("赵六", 82, 78, 80),
    ("陈七", 90, 94, 87),
    ("刘洋", 70, 75, 78),
    ("周婷", 85, 89, 91),
    ("吴浩", 92, 80, 88),
    ("郑雪", 78, 82, 84),
    ("孙磊", 88, 86, 90)
)

#计算均分
print("姓名\t\t数学\t\t语文\t\t英语\t\t均分")
for name,math,chinese,english in students:#利用元组的解包分解每一个学生的成绩
    total = math+chinese+english
    avg = total/3
    print(f"{name}\t\t{math}\t\t{chinese}\t\t{english}\t\t{avg:.1f}")

#计算最高分最低分
#生成成绩列表
math_score = [s[1] for s in students]
chinese_score = [s[2] for s in students]
english_score = [s[3] for s in students]

print(f"数学最低分为{min(math_score)},数学最高分为{max(math_score)}")
