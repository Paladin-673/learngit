# -*- coding: cp936 -*-
#作者：李月
#功能：自动把指定文件夹下的excel批量转为txt文件

import os
import time
import sys
import xlrd

#遍历文件夹
def openDir(fromdir):
    if not os.path.exists(fromdir):
        print("路径错误！")

    workbooks_list = []
    files = os.listdir(fromdir)
    files.sort()

    for file in files:
        filepath = os.path.join(fromdir,file)
        workbook = xlrd.open_workbook(filepath)
        workbooks_list.append(workbook)
    #print(workbooks_list)
    return workbooks_list
    
#遍历Workbook并把数据输出至txt文件
def openWorkBook(fromdir,appointsheetname):
    txtfile = open(fromdir + appointsheetname + ".txt",mode = "w",encoding = "utf-8")
    for workbook in openDir(fromdir):
        for sheetname in workbook.sheet_names():
            #如果遍历的sheet为指定名字的sheet，则开始写入
            if sheetname == appointsheetname:
                sheet = workbook.sheet_by_name(sheetname)

                for n in range(sheet.nrows):
                    for i in range(sheet.ncols):
                        text = sheet.cell_value(n,i)
                        if i == sheet.ncols - 1:
                            txtfile.write(str(text))
                        else:
                            txtfile.write(str(text) + "\t")

                    txtfile.write('\n')

    txtfile.close()
    

if __name__ == '__main__':
    begin = time.time()
    print("Begin to convert Excel to txt...")
    openWorkBook("C:\\Users\\liyue\\Desktop\\shiyan","学生表")
    end = time.time()
    print("It tooks %d seconds" % (end - begin))
