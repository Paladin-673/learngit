# -*- coding: cp936 -*-
#���ߣ�����
#���ܣ��Զ���ָ���ļ����µ�excel����תΪtxt�ļ�

import os
import time
import sys
import xlrd

#�����ļ���
def openDir(fromdir):
    if not os.path.exists(fromdir):
        print("·������")

    workbooks_list = []
    files = os.listdir(fromdir)
    files.sort()

    for file in files:
        filepath = os.path.join(fromdir,file)
        workbook = xlrd.open_workbook(filepath)
        workbooks_list.append(workbook)
    #print(workbooks_list)
    return workbooks_list
    
#����Workbook�������������txt�ļ�
def openWorkBook(fromdir,appointsheetname):
    txtfile = open(fromdir + appointsheetname + ".txt",mode = "w",encoding = "utf-8")
    for workbook in openDir(fromdir):
        for sheetname in workbook.sheet_names():
            #���������sheetΪָ�����ֵ�sheet����ʼд��
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
    openWorkBook("C:\\Users\\liyue\\Desktop\\shiyan","ѧ����")
    end = time.time()
    print("It tooks %d seconds" % (end - begin))
