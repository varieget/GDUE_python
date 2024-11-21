# 2.	编写程序实现根据考试成绩将成绩分为A,B,C,D四档。

score = input()

print("等级：")
if int(score) >= 75:
    print("A")
elif int(score) >= 50:
    print("B")
elif int(score) >= 25:
    print("C")
else:
    print("D")
