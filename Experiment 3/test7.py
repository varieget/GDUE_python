# 7.	编写程序实现打印100以内的素数。

for i in range(2, 100):
    num = 0
    for j in range(2, i):
        if i % j == 0:
            num += 1
            break

    if num == 0:
        print(i)
