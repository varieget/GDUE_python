# 5.	编写程序实现打印9*9乘法表。

for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, "*", i, "=", j * i, end="\t")

    print("")  # \n
