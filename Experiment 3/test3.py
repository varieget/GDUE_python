# 3.	编写程序实现输入x,y，判断属于第几象限。

x = int(input("输入x的值："))
y = int(input("输入y的值："))

result = 0

if x > 0 and y > 0:
    result = 1
elif x < 0 and y > 0:
    result = 2
elif x < 0 and y < 0:
    result = 3
elif x > 0 and y < 0:
    result = 4

print("位于第", result, "象限")
