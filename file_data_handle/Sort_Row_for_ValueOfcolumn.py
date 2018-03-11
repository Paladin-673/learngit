# -*- coding: cp936 -*-
#���ߣ�����
#���ܣ�����ĳ�ж��ļ���������Ȼ��ȡǰN��

#�ܴ���ʱ��3��ע�⣺1.Դ�ļ����ޱ�ͷ��2.Դ�ļ��ķָ�����3.Ҫ�����ֶ�������λ��

import os
import time

def SortRowforValue(filename,number):

    #����Դ�ļ����ָ�Ŀ���ļ�����
    [forward_filename,last_filename]=os.path.splitext(filename)
    new_filename = forward_filename + "_sorted.csv"

    #������ֵ�
    dict_before={}
    dict_after={}

    #��Դ�ļ���ȡԴ�ļ�
    fin = open(filename,'r')
    #ע����û�б�ͷ
    head = fin.readline()   #��ȡ��ͷ

    #��line����Ӧ�ֶ�д���ֵ��key��value,ע��line���ֶεı�ţ���������field[7]
    for line in fin:
        field=line.split(',')   #ע��csv��','�ָ���txt��'\t'�ָ�
        field6=float(field[6].strip())
        dict_before[line]=field6

    #���ֵ��������,e[1]�ǰ�value����,reverse=True�ǴӴ�С����    
    dict_after=dict(sorted(dict_before.items(),key=lambda e:e[1],reverse=True))
    #�������ǰ�ֵ�
    dict_before={}

    #��Ŀ���ļ���д���ͷ
    fout = open(new_filename,'w')
    #�������ͷ��Ӧ��û����ע�͵�
    fout.writelines([head])  #�ޱ�ͷ��ע�͵�

    #д������
    n=0
    for key in dict_after:
        n += 1
        if n > number or n >len(dict_after):
            break
        if '\n' not in key:
            fout.write(key+'\n')
        else:
            fout.write(key)

    #����ڴ�
    dict_after={}
    #�رձ�
    fin.close()
    fout.close()

if __name__ == '__main__':
    begin=time.time()
    print('begin to sort row for value of column...')
    SortRowforValue('C:\\Users\\liyue\\Desktop\\gprs_20171103_10h_1_����.csv',1000)
    print('finish!')
    end=time.time()
    print('time is %d seconds' %(end - begin))
    
