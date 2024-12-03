import cv2 as cv
import matplotlib.pyplot as plt

import numpy as np

# （1）读取一张个人的照片；如果是彩色图像，请转换为灰度图像。
img = cv.imread('img.png')
img_tmp = cv.imread('img.png', 0)  # 直接以灰度图片读取
img_tmp_hang = img_tmp[180, :]
plt.plot(img_tmp_hang)
plt.axis([0, 700, 0, 255])
plt.legend(['data'], loc='lower center')
plt.show()

# cv.namedWindow('Image')
# 在窗口中显示图像
size = img_tmp.shape
print(size)  # (h,w,c)
x = size[0]
y = size[1]
img1 = img_tmp[::-1, :]  # cv.flip(img_tmp,-1 ) #图像上下翻转
img1 = img_tmp[-1:-x:-1, :]  # cv.flip(img_tmp,-1 ) #图像上下翻转
cv.imshow('upsidedown', img1)
# cv.imencode('.jpg', img1)[1].tofile('上下翻转.jpg')  # 防止乱码
# 同理，请自己进行左右，对角翻转

img2 = img_tmp.copy()
# cv.imwrite('rose_copy2.jpg', img2)
cv.imshow('gray', img2)

# print(img.dtype)
# print(img.size)  # 像素总数目

# （2）实现图像剪裁 ，输入原始图像对象，返回剪裁后的图像对象。剪裁的区域自己决定。
dst = img[80:600, 150:500]
cv.imshow('cut', dst)

# （3）实现图像水平，垂直，对角翻转，输入原始图像对象，返回水平垂直，对角后的图像对象。（此内容自己写函数实现）
def translation(mat, code):
    return cv.flip(mat, code)


for axis, i in [['x-axis', 0], ['y-axis', 1], ['both-axes', -1]]:
    dst = translation(img, i)
    cv.imshow(f'translation-%s' % axis, dst)


# （4）实现图像逆时针或顺时针旋转90度的函数rotate()，输入原始图像对象，返回逆时针或顺时针旋转90度后的图像对象 。（此内容自己写函数实现）
def rotate(mat):
    return cv.warpAffine(
        mat,
        cv.getRotationMatrix2D((height * 0.5, width * 0.5), 90, 1),  # 1 center 2 angle 3 缩放系数
        (height, width)
    )


# （5）实现图像的反转，即亮的区域变暗，暗的区域变亮。
dst = cv.bitwise_not(img_tmp)
cv.imshow('invert', dst)

# （6）实现图像的平移，缩放，旋转。
# 图像平移
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]

dst = np.zeros(imgInfo, np.uint8)

for i in range(height):
    for j in range(width - 200):
        dst[i, j + 200] = img[i, j]

cv.imshow('translation', dst)

# 缩放
# 1 放大 缩小 2 等比例 非等比例
dstHeight = int(height * 0.5)
dstWeight = int(width * 1.5)
# 最近邻域插值 双线性插值 像素关系重采样 立方插值
dst = cv.resize(img, (dstWeight, dstHeight))
# print(dst.shape)
cv.imshow('resize', dst)

# 旋转
dst = rotate(img)
cv.imshow('rotate', dst)

# （7）读取图像中间1行数据，并通过画图显示出来。
dst = img[height // 2]
cv.imshow('middle-row', dst)

# 原文链接：https://blog.csdn.net/missyougoon/article/details/81092512
cv.waitKey(0)
