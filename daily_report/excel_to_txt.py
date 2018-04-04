# -*- coding: cp936 -*-
#���ߣ�����
#���ܣ����չ����excel��������txt�ձ���

import os
import time
import sys
import xlrd
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox

def popupWindow():
    root = Tk()
    
    tkinter.messagebox.showinfo('��ʾ','��ѡ��excel�ļ�')
    path = tkinter.filedialog.askopenfilename()
    excelTotxt(path)
    tkinter.messagebox.showinfo('��ʾ','�ձ������ɣ�')
    root.destroy()
    
#excelת�ձ�main����
def excelTotxt(path):
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name('�ձ�ͳ��')

    [des,file] = os.path.split(path)
    txtfile = open(des + "\\�ձ�.txt",mode = "w",encoding = "utf-8")

    sentence1 = sentenceOperateOne(worksheet)
    sentence2 = sentenceOperateTwo(worksheet)
    sentence3 = sentenceOperateThree(worksheet)
    sentence4 = sentenceOperateFour(worksheet)
    sentence5 = sentenceOperateFive(worksheet)
    sentence6 = "\t3��29����4��1�ն�λ��ʱ����0��\n\n\t3��29��\
��4��1�ձջ���ʱ����0��\n\n\t����ͨ�����ݣ�"
    sentence7 = sentenceOperateSeven(worksheet)
    
    txtfile.write(sentence1+"\n\n"+sentence2+"\n\n"+sentence3+"\n\n"\
                  +sentence4+"\n\n"+sentence5+"\n\n"+sentence6+"\n\n"\
                  +sentence7+"\n\n")
    txtfile.close()

#��һ�����ִ���
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
    sentence = "    ��ֹ4��1�գ�������ع����ܼƷ���%d���������밸����%d��\
δ�밸���⵫�ѱջ�%d��δ�밸������δ�ջ�%d����ʷ����ջ���%.2f%%��" \
% (value1,value2,value3,value4,value5*100)

    return sentence

#�ڶ������ִ���
def sentenceOperateTwo(f):
    value1 = int(f.cell_value(24,31))
    value2 = int(f.cell_value(24,36))
    value3 = float(f.cell_value(24,26))
    sentence = "    ������ά��2018�꿼�˰취��\
������ع����ջ��ʿ��˽�������Ҫ�����빤��Ȩ�صĸ��\
���ڴ˻����϶Թ���Ȩ�ؽ��ж�̬���أ����й�������Ϊ��ͬ�����ͣ�\
��ͳ��ʱ���費ͬ��Ȩ��ϵ������3�¿��˿ھ���δ�밸�����߼������ܼ�%d��\
�����ѱջ��߼�����%d���ջ���%.2f%%��\n\n\
ע���߼�������Ϊʵ�ʹ��������ղ�ͬ���ͳ�����ӦȨ��ϵ������ó���"\
% (value1,value2,value3*100)

    return sentence

def abstractLoop(f,startrow,endrow,column):
    string = ""
    for i in range(startrow-1,endrow):
        if i == endrow-1 and f.cell_value(i,column-1) != 0:
            string = string+f.cell_value(i,1)+str(int(f.cell_value(i,column-1)))
        elif f.cell_value(i,column-1) != 0:
            string = string+f.cell_value(i,1)+str(int(f.cell_value(i,column-1)))+"��"

    return string

#���������ִ���
def sentenceOperateThree(f):
    value1 = int(f.cell_value(23,13))
    value2 = int(f.cell_value(1,13))
    value3 = int(f.cell_value(10,13))
    string1 = abstractLoop(f,4,10,14)
    value4 = int(f.cell_value(16,13))
    string2 = abstractLoop(f,12,16,14)
    value5 = int(f.cell_value(22,13))
    string3 = abstractLoop(f,18,22,14)
    
    sentence = "    3��29����4��1�շ��͹���%d�����������Ż�����%d��\
�������綫�������Ż�����%d��%s����\
���������ϲ������Ż�����%d��%s����\
�����������������Ż���%d��%s����"\
% (value1,value2,value3,string1,value4,string2,value5,string3)

    return sentence

#���Ķ����ִ���
def sentenceOperateFour(f):
    value1 = int(f.cell_value(23,15))
    value2 = int(f.cell_value(1,15))
    value3 = int(f.cell_value(10,15))
    string1 = abstractLoop(f,4,10,16)
    value4 = int(f.cell_value(16,15))
    string2 = abstractLoop(f,12,16,16)
    value5 = int(f.cell_value(22,15))
    string3 = abstractLoop(f,18,22,16)
    
    sentence = "    3��29����4��1�ձջ�����%d�����������Ż�����%d��\
�������綫�������Ż�����%d��%s����\
���������ϲ������Ż�����%d��%s����\
�����������������Ż���%d��%s����"\
% (value1,value2,value3,string1,value4,string2,value5,string3)

    return sentence

#��������ִ���
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
    
    sentence = "    3��29����4��1�ն�λ����%d�����������Ż�����%d��\
��Ҫ�ͻ�֧������%d���������綫�������Ż�����%d��%s����\
���������ϲ������Ż�����%d��%s����\
�����������������Ż���%d��%s����"\
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

    #���ֵ��������,e[1]�ǰ�value����,reverse=True�ǴӴ�С����
    dict_bigtosmall=dict(sorted(dictOne.items(),key=lambda e:e[1],reverse=True))

    for key in dict_bigtosmall:
        if n < 3:
            string1 = string1 + " " + key
        n += 1
    listOne.append(string1)

    #���ֵ��������,e[1]�ǰ�value����,reverse=False�Ǵ�С��������
    dict_smalltobig=dict(sorted(dictOne.items(),key=lambda e:e[1],reverse=False))

    for key in dict_smalltobig:
        if m < 3:
            string2 = string2 + " " + key
        m += 1
    listOne.append(string2)

    return listOne

#���߶����ִ���
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
    
    sentence = "    �������3��29�յ�4��1�շ���%d�ջ�%d��\
��ֹ4��1�գ��ܼƷ���%d�����밸����%d����ʷ����ջ���%.2f��\
��3�¿��˿ھ���δ����߼�����%d��δ����бջ���%.2f%%��\
�����ţ�ϵͳ%.2f���ؿ�%.2f������%.2f���ϲ�%.2f������%.2f��\
���ֹ�˾��ã�%s����%s��"\
%(value1,value2,value5,value4,value6,value3,value7*100,\
value8,value9,value10,value11,value12,one,two)

    return sentence

if __name__ == '__main__':
    begin = time.time()
    print("��ʼ�����ձ�...")
    popupWindow()
    end = time.time()
    print("������ʱ��: %d ��" % (end - begin))
