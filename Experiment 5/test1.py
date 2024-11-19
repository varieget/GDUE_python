import random

with open('hello.txt', 'a') as f:
    for i in range(10):
        f.write(f"%d" % random.randint(0, 9))
        f.write('\n')
