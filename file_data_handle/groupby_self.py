# -*- coding: cp936 -*-

from pandas import *

f = open("C:\\Users\\liyue\\Desktop\\����.txt",'r')# ����һ���ļ�����

dict={'name':[],'value':[],'class':[]}
#line = f.readline()       # �����ļ��� readline()���� 
for line in f:
    m=line.split('\t')
    m2=m[2].replace('\n','')
    dict['name'].append(m[0])
    dict['value'].append(int(m[1]))
    dict['class'].append(m2)
df=DataFrame(dict)
j=df.groupby(['name','class']).mean().reset_index()

'''fw=open("C:\\Users\\liyue\\Desktop\\666.txt",'w')
fw.writelines(str(j))
fw.close()'''
out_xlsx="shiyan"+'-group.xlsx'
j.to_excel(out_xlsx,sheet_name='Sheet1',index=False)

           # ����� ',' �����Ի��з�  
    #line = f.readline() 
 
f.close()

