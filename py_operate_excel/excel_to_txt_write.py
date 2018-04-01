# -*- coding: cp936 -*-
#作者：李月

import os
import xlrd
import sys

path = "C:\\Users\\liyue\\Desktop\\实验表1.xlsx"

workbook = xlrd.open_workbook(path)

sheet1 = workbook.sheet_by_name(u'学生表')

#第一种写入方法，逐个单元格写入
'''NROWS = sheet1.nrows
NCOLS = sheet1.ncols

file = open("C:\\Users\\liyue\\Desktop\\实验表1.txt","w")
for n in range(sheet1.nrows):
    for i in range(sheet1.ncols):
        text = sheet1.cell_value(n,i)
        if i == NCOLS - 1:
            file.write(str(text))
        else:
            file.write(str(text) + "\t")
    if n != NROWS - 1:
        file.write('\n')
file.close()'''

#第二种写入方法，逐行写入
file = open("C:\\Users\\liyue\\Desktop\\实验表1.txt","w",encoding="utf-8")
for n in range(sheet1.nrows):
    row = sheet1.row_values(n)
    file.write(str(row))
    file.write('\n')
file.close()

