# -*- coding: cp936 -*-
#���ߣ�����

import os
import xlrd
import sys

path = "C:\\Users\\liyue\\Desktop\\ʵ���1.xlsx"

workbook = xlrd.open_workbook(path)

sheet1 = workbook.sheet_by_name(u'ѧ����')

#��һ��д�뷽���������Ԫ��д��
'''NROWS = sheet1.nrows
NCOLS = sheet1.ncols

file = open("C:\\Users\\liyue\\Desktop\\ʵ���1.txt","w")
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

#�ڶ���д�뷽��������д��
file = open("C:\\Users\\liyue\\Desktop\\ʵ���1.txt","w",encoding="utf-8")
for n in range(sheet1.nrows):
    row = sheet1.row_values(n)
    file.write(str(row))
    file.write('\n')
file.close()

