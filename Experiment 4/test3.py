# 3.请分别设计如下函数：
# 将小写字母转换为大写字母函数（函数命名为xiao2da）和将大写字母转换为小写字母函数（函数命名为da2xiao）。
# 其中这两个函数保存在zimuzhuanhuan.py文件中。
# 然后设计一个主函数（不可以在zimuzhuanhuan.py文件中定义），通过对上述两个函数的调用，可以对任意输入的字符串进行大小写转换。

from zimuzhuanhuan import xiao2da, da2xiao


def main(text):
    print(xiao2da(text))
    print(da2xiao(text))


str1 = input()
main(str1)
