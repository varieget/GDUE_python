import numpy as np
import matplotlib.pyplot as plt

# modes = ['full', 'same', 'valid']
modes = ['valid']
# data = np.ones(200)
data = np.random.randint(15, 20, size=300)
data = np.random.normal(data)  # 白噪声（正态分布 均值为0,方差为1）

# window = np.ones(3)/3
window = lambda x: np.ones(x)/x
for size in [3, 7, 11]:
    for m in modes:
        # 当size取值较大时，滤波后的信号比较平滑，但是灵敏度差；相反size取值较小时，滤波平滑效果差，但灵敏度好。
        data_tmp = np.convolve(data, window(size), mode=m)  # 卷积 中值滤波
        # data_tmp = np.correlate(data, window(size), mode=m)  # 计算自相关 均值滤波
        plt.plot(data_tmp)

plt.plot(data)  # 原始数据
plt.axis([-10, 300, -.1, 25])
plt.legend(modes + ['data'], loc='lower center')
plt.show()
