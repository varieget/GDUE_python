# 1.创建文件hello.txt,手动输入内容“hello，world”；然后向文件“hello.txt”中追加从0到9的随机整数, 10个数字一行，共10行整数。

import random

with open('hello.txt', 'a') as f:
    for i in range(10):
        f.write(f"%d" % random.randint(0, 9))
        f.write('\n')
