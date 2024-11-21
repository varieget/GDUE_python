# 1•根据输入参数(行数)不同，输出下面图形

def jzt(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")

        for j in range(2 * i - 1):
            print("*", end="")

        print()


num = int(input())
jzt(num)
