# -*- coding: cp936 -*-

f = open("C:\\Users\\liyue\\Desktop\\����.txt",'r')       # ����һ���ļ����� 
#line = f.readline()       # �����ļ��� readline()���� 
for line in f:
    m=line.split('\t')
    if m[1]=='С��':
        print(line),       # ����� ',' �����Ի��з�  
    #line = f.readline() 
 
f.close() 
