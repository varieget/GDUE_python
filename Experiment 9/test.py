import numpy as np
import matplotlib.pyplot as plt

# （1）自行写一个一元二次方程。
# （2）求出该方程的极值点。
# （3）在图上显示方程图像和极值点。
# （3）思考梯度下降是否可以实现本实验的求解。

# 原函数
def f(x):
    return x ** 2 + 2


##导数
def h(x):
    return 2 * x


X = []
Y = []
x = 2.5
step = 0.8
f_change = f(x)
f_current = f(x)
X.append(x)
Y.append(f_current)

while f_change > 1e-10:
    x = x - step * h(x)
    tmp = f(x)
    f_change = np.abs(f_current - tmp)
    f_current = tmp
    X.append(x)
    Y.append(f_current)

print("输出结果为：(", x, ",", f_current, ")")

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
fig = plt.figure()

X2 = np.arange(-2.1, 2.6, 0.04)
Y2 = X2 ** 2 + 2

plt.plot(X2, Y2, '-', color='#666666', linewidth=2)
plt.plot(X, Y, 'bo-')
plt.title(u'$y=x^2$函数求解最小值,最终解为:x=%.2f,y=%.2f' % (x, f_current))

plt.show()
plt.savefig('exam_01.png')
