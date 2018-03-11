# -*- coding: cp936 -*-
#作者：李月
#功能：根据某列对文件进行排序，然后取前N行

#跑代码时有3点注意：1.源文件有无表头；2.源文件的分隔符；3.要排序字段在行中位置

import os
import time

def SortRowforValue(filename,number):

    #根据源文件名字给目标文件起名
    [forward_filename,last_filename]=os.path.splitext(filename)
    new_filename = forward_filename + "_sorted.csv"

    #定义空字典
    dict_before={}
    dict_after={}

    #打开源文件读取源文件
    fin = open(filename,'r')
    #注意有没有表头
    head = fin.readline()   #读取表头

    #把line和相应字段写入字典的key和value,注意line中字段的标号，如流量是field[7]
    for line in fin:
        field=line.split(',')   #注意csv用','分隔，txt用'\t'分隔
        field6=float(field[6].strip())
        dict_before[line]=field6

    #对字典进行排序,e[1]是按value排序,reverse=True是从大到小排序    
    dict_after=dict(sorted(dict_before.items(),key=lambda e:e[1],reverse=True))
    #清空排序前字典
    dict_before={}

    #打开目标文件并写入表头
    fout = open(new_filename,'w')
    #和上面表头对应，没有则注释掉
    fout.writelines([head])  #无表头请注释掉

    #写入内容
    n=0
    for key in dict_after:
        n += 1
        if n > number or n >len(dict_after):
            break
        if '\n' not in key:
            fout.write(key+'\n')
        else:
            fout.write(key)

    #清空内存
    dict_after={}
    #关闭表
    fin.close()
    fout.close()

if __name__ == '__main__':
    begin=time.time()
    print('begin to sort row for value of column...')
    SortRowforValue('C:\\Users\\liyue\\Desktop\\gprs_20171103_10h_1_汇总.csv',1000)
    print('finish!')
    end=time.time()
    print('time is %d seconds' %(end - begin))
    
