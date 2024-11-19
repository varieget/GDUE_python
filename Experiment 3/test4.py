# 4.	编写程序实现猜数字游戏，5次机会猜1-100内的数字。

import random

targetNum = random.randint(1, 100)

for i in range(5):
    inputNum = int(input("请输入你猜的数："))
    if inputNum > targetNum:
        print("偏大")
    elif inputNum < targetNum:
        print("偏小")
    else:
        print("猜中了")
        break

if inputNum != targetNum:
    print("目标数是：", targetNum)
    print("5次没有猜中")
