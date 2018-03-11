# -*- coding: cp936 -*-
#作者：李月
#按某列对文件进行筛选，并切割
#注意：1.打开文件的编码格式；2.每行最后一行的换行符

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
            if m10 == '畅爽全国冰激凌套餐398元档':
                buf.append(line)  
                if len(buf) == count:  
                    sub = mkSubFile(buf,filename,sub)  
                    buf = []
                    #break  #加break为试验1000行
        if len(buf) != 0:  
            sub = mkSubFile(buf,filename,sub)  #取消这行注释，为循环切割 
    finally:  
        fin.close()  
  
if __name__ == '__main__':  
    begin = time.time()  
    splitByLineCount('D:\\bigdata\\gprs_20171111.txt',40000000)
    end = time.time()  
    print('time is %d seconds ' % (end - begin))
