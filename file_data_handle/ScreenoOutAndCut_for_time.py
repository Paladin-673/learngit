# -*- coding: cp936 -*-
#���ߣ�����
#��ĳ�ж��ļ�����ɸѡ�����и�
#ע�⣺1.���ļ��ı����ʽ��2.ÿ�����һ�еĻ��з�

import os  
import time  
  
def mkSubFile(lines,srcName,sub):  
    [des_filename, extname] = os.path.splitext(srcName)  
    filename  = des_filename + '_' + str(sub) + extname  
    print( 'make file: %s' %filename)  
    fout = open(filename,'w')  
    try:  
        '''fout.writelines([head])''' 
        fout.writelines(lines) 
        return sub + 1  
    finally:  
        fout.close()  
  
def splitByLineCount(filename,count):  
    fin = open(filename,'r',encoding='utf-8')
    try:  
        '''head = fin.readline()'''
        buf = []  
        sub = 1  
        for line in fin:
            m=line.split('\t')
            m10=m[10].strip()
            if m10 == '��ˬȫ���������ײ�398Ԫ��':
                buf.append(line)  
                if len(buf) == count:  
                    sub = mkSubFile(buf,filename,sub)  
                    buf = []
                    #break  #��breakΪ����1000��
        if len(buf) != 0:  
            sub = mkSubFile(buf,filename,sub)  #ȡ������ע�ͣ�Ϊѭ���и� 
    finally:  
        fin.close()  
  
if __name__ == '__main__':  
    begin = time.time()  
    splitByLineCount('D:\\bigdata\\gprs_20171111.txt',40000000)
    end = time.time()  
    print('time is %d seconds ' % (end - begin))
