# -*- coding: cp936 -*-
#作者：李月
#功能：按照规则把excel内容生成txt日报。

import os
import time
import sys
import xlrd
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox

def popupWindow():
    root = Tk()
    
    tkinter.messagebox.showinfo('提示','请选择excel文件')
    path = tkinter.filedialog.askopenfilename()
    excelTotxt(path)
    tkinter.messagebox.showinfo('提示','日报已生成！')
    root.destroy()
    
#excel转日报main函数
def excelTotxt(path):
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name('日报统计')

    [des,file] = os.path.split(path)
    txtfile = open(des + "\\日报.txt",mode = "w",encoding = "utf-8")

    sentence1 = sentenceOperateOne(worksheet)
    sentence2 = sentenceOperateTwo(worksheet)
    sentence3 = sentenceOperateThree(worksheet)
    sentence4 = sentenceOperateFour(worksheet)
    sentence5 = sentenceOperateFive(worksheet)
    sentence6 = "\t3月29日至4月1日定位超时工单0。\n\n\t3月29日\
至4月1日闭环超时工单0。\n\n\t短信通报内容："
    sentence7 = sentenceOperateSeven(worksheet)
    
    txtfile.write(sentence1+"\n\n"+sentence2+"\n\n"+sentence3+"\n\n"\
                  +sentence4+"\n\n"+sentence5+"\n\n"+sentence6+"\n\n"\
                  +sentence7+"\n\n")
    txtfile.close()

#第一段文字处理
def sentenceOperateOne(f):
    str1 = f.cell_value(23,3)
    str2 = f.cell_value(24,3)
    str3 = f.cell_value(23,4)
    str4 = f.cell_value(23,5)
    str5 = f.cell_value(24,5)

    value1 = int(str1) + int(str2)
    value2 = int(str2)
    value3 = int(str3)
    value4 = int(str4)
    value5 = float(str5)
    sentence = "    截止4月1日，质量监控工单总计发单%d，其中已入案例库%d，\
未入案例库但已闭环%d，未入案例库且未闭环%d，历史总体闭环率%.2f%%。" \
% (value1,value2,value3,value4,value5*100)

    return sentence

#第二段文字处理
def sentenceOperateTwo(f):
    value1 = int(f.cell_value(24,31))
    value2 = int(f.cell_value(24,36))
    value3 = float(f.cell_value(24,26))
    sentence = "    根据运维部2018年考核办法，\
质量监控工单闭环率考核将根据重要性引入工单权重的概念，\
并在此基础上对工单权重进行动态调控，所有工单将分为不同的类型，\
在统计时给予不同的权重系数。按3月考核口径，未入案例库逻辑工单总计%d，\
其中已闭环逻辑工单%d，闭环率%.2f%%。\n\n\
注：逻辑工单数为实际工单数按照不同类型乘以相应权重系数计算得出。"\
% (value1,value2,value3*100)

    return sentence

def abstractLoop(f,startrow,endrow,column):
    string = ""
    for i in range(startrow-1,endrow):
        if i == endrow-1 and f.cell_value(i,column-1) != 0:
            string = string+f.cell_value(i,1)+str(int(f.cell_value(i,column-1)))
        elif f.cell_value(i,column-1) != 0:
            string = string+f.cell_value(i,1)+str(int(f.cell_value(i,column-1)))+"，"

    return string

#第三段文字处理
def sentenceOperateThree(f):
    value1 = int(f.cell_value(23,13))
    value2 = int(f.cell_value(1,13))
    value3 = int(f.cell_value(10,13))
    string1 = abstractLoop(f,4,10,14)
    value4 = int(f.cell_value(16,13))
    string2 = abstractLoop(f,12,16,14)
    value5 = int(f.cell_value(22,13))
    string3 = abstractLoop(f,18,22,14)
    
    sentence = "    3月29日至4月1日发送工单%d：无线网络优化中心%d，\
无线网络东北区域优化中心%d（%s），\
无线网络南部区域优化中心%d（%s），\
无线网络西北区域优化中%d（%s）。"\
% (value1,value2,value3,string1,value4,string2,value5,string3)

    return sentence

#第四段文字处理
def sentenceOperateFour(f):
    value1 = int(f.cell_value(23,15))
    value2 = int(f.cell_value(1,15))
    value3 = int(f.cell_value(10,15))
    string1 = abstractLoop(f,4,10,16)
    value4 = int(f.cell_value(16,15))
    string2 = abstractLoop(f,12,16,16)
    value5 = int(f.cell_value(22,15))
    string3 = abstractLoop(f,18,22,16)
    
    sentence = "    3月29日至4月1日闭环工单%d：无线网络优化中心%d，\
无线网络东北区域优化中心%d（%s），\
无线网络南部区域优化中心%d（%s），\
无线网络西北区域优化中%d（%s）。"\
% (value1,value2,value3,string1,value4,string2,value5,string3)

    return sentence

#第五段文字处理
def sentenceOperateFive(f):
    value1 = int(f.cell_value(23,14))
    value2 = int(f.cell_value(1,14))
    value3 = int(f.cell_value(2,14))
    value4 = int(f.cell_value(10,14))
    string1 = abstractLoop(f,4,10,15)
    value5 = int(f.cell_value(16,14))
    string2 = abstractLoop(f,12,16,15)
    value6 = int(f.cell_value(22,14))
    string3 = abstractLoop(f,18,22,15)
    
    sentence = "    3月29日至4月1日定位工单%d：无线网络优化中心%d，\
重要客户支撑中心%d，无线网络东北区域优化中心%d（%s），\
无线网络南部区域优化中心%d（%s），\
无线网络西北区域优化中%d（%s）。"\
% (value1,value2,value3,value4,string1,value5,string2,value6,string3)

    return sentence

def dictionarySort(f,startrow,endrow):
    listOne = []
    dictOne = {}
    string1 = ""
    string2 = ""
    n = 0
    m = 0
    
    for i in range(startrow-1,endrow):
        dictOne[f.cell_value(i,25)+"/"+str(round(f.cell_value(i,26)*100,2))]=f.cell_value(i,26)

    #对字典进行排序,e[1]是按value排序,reverse=True是从大到小排序
    dict_bigtosmall=dict(sorted(dictOne.items(),key=lambda e:e[1],reverse=True))

    for key in dict_bigtosmall:
        if n < 3:
            string1 = string1 + " " + key
        n += 1
    listOne.append(string1)

    #对字典进行排序,e[1]是按value排序,reverse=False是从小到大排序
    dict_smalltobig=dict(sorted(dictOne.items(),key=lambda e:e[1],reverse=False))

    for key in dict_smalltobig:
        if m < 3:
            string2 = string2 + " " + key
        m += 1
    listOne.append(string2)

    return listOne

#第七段文字处理
def sentenceOperateSeven(f):
    value1 = int(f.cell_value(23,13))
    value2 = int(f.cell_value(23,15))
    value3 = int(f.cell_value(23,3))
    value4 = int(f.cell_value(24,3))
    value5 = value3 + value4
    value6 = float(f.cell_value(24,5))*100
    value7 = float(f.cell_value(24,26))
    
    value8 = float(f.cell_value(2,26))*100
    value9 = float(f.cell_value(3,26))*100
    value10 = float(f.cell_value(11,26))*100
    value11 = float(f.cell_value(17,26))*100
    value12 = float(f.cell_value(23,26))*100

    [one,two] = dictionarySort(f,31,47)
    
    sentence = "    质量监控3月29日到4月1日发单%d闭环%d。\
截止4月1日，总计发单%d，已入案例库%d，历史总体闭环率%.2f。\
按3月考核口径：未入库逻辑工单%d，未入库中闭环率%.2f%%，\
按网优：系统%.2f，重客%.2f，东北%.2f，南部%.2f，西北%.2f。\
按分公司最好：%s，最差：%s。"\
%(value1,value2,value5,value4,value6,value3,value7*100,\
value8,value9,value10,value11,value12,one,two)

    return sentence

if __name__ == '__main__':
    begin = time.time()
    print("开始生成日报...")
    popupWindow()
    end = time.time()
    print("共花费时间: %d 秒" % (end - begin))
