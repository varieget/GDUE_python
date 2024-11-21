# 6.	编写程序实现打印第一个三位的水仙花数。
# abc = a^3 + b^3 + c^3
# 1^3 + 5^3 + 3^3 = 153

for i in range(100, 1000):
    temp = i
    result = 0
    while temp > 0:
        result += (temp % 10) ** 3
        temp //= 10

    if i == result:
        print(i)
        break  # 第一个
