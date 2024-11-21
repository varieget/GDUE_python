# 3.编写程序，创建文件data.txt，共100000行，每行存放一个1～100之间的随机整数。

import random

with open('data.txt', 'w+') as f:
    for i in range(100000):
        f.write(f"%d" % random.randint(1, 100))
        f.write('\n')
