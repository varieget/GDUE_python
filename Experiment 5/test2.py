import xlrd
from xlutils.copy import copy

workbook = xlrd.open_workbook('成绩.xls')
sheet1 = workbook.sheet_by_name('Sheet1')
grade = [sheet1.cell(row, 1).value for row in range(1, sheet1.nrows)]
avg = sum(grade) / len(grade)
print(f"全班的成绩平均分: %d" % avg)

wt = copy(workbook)
sh1 = wt.get_sheet(0)
sh1.write(10, 0, "平均分")
sh1.write(10, 1, avg)
wt.save("成绩.xls")
