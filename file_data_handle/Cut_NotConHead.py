# -*- coding: cp936 -*-
#作者：李月
#功能：切分不带表头的文件
 
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
            buf.append(line)  
            if len(buf) == count:  
                sub = mkSubFile(buf,filename,sub)  
                buf = []
                break  #加break为试验10000行

    finally:  
        fin.close()  
  
if __name__ == '__main__':  
    begin = time.time()  
    splitByLineCount('文件路径',10000)  
    end = time.time()  
    print('time is %d seconds ' % (end - begin))
