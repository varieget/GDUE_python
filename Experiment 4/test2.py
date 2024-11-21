# 2.设计一个函数，可计算n！，其中n是参数。

def jc(n):
    count = 1
    for i in range(1, n + 1):
        count *= i

    return count


num = int(input())
print(f"{num}! = {jc(num)}")
