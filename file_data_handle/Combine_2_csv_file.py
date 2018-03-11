# -*- coding: cp936 -*-
#���ߣ�����
#�ϲ�2��csv�ļ�������ļ���ʵ���ò���ע���txt��'\t',��csv��','

import os  
import time
import numpy
import pandas as pd
from pandas import *

#����ʵ�ֵ�join left on  
def CombineDoubleCsv(filename1,filename2):

    #���ļ����ݶ����ڴ�
    fin1 = open(filename1,'r')
    fin2 = open(filename2,'r')
    try:

        #����csv�ļ�������ֵ䣬�˴��Ǵ洢���ڴ���
        head1=fin1.readline()

        #�������ֶν������ֵ�
        dict1={'�û�����':[],'�ֻ���':[],'IMSI':[],'IMEI':[],
              '����':[],'�ն�����':[],
              '�ײ�':[]}
        
        for line1 in fin1:
            m=line1.split(',')
            m6=m[6].replace('\n','')
            dict1['�û�����'].append(m[1])
            dict1['�ֻ���'].append(m[0])
            dict1['IMSI'].append(m[2])
            dict1['IMEI'].append(m[3])
            #dict1['��ʼʱ��'].append(m[4])
            #dict1['LAC'].append(m[5])
            #dict1['CI'].append(m[6])
            dict1['����'].append(m6)               #�˴���ȥ�����з���
            #dict1['ҵ��ʱ��'].append(int(m[8]))
            dict1['�ն�����'].append(m[4])
            dict1['�ײ�'].append(m[5])          

        #��ʽ���ֵ�
        df1=DataFrame(dict1)
        #print(df1)

         #����csv�ļ�������ֵ䣬�˴��Ǵ洢���ڴ���
        head2=fin2.readline()

        #�������ֶν������ֵ�
        dict2={'�û�����':[],'�ֻ���':[],'IMSI':[],'IMEI':[],
              '����':[],'�ն�����':[],
              '�ײ�':[]}
        
        for line2 in fin2:
            n=line2.split(',')
            n6=n[6].replace('\n','')
            dict2['�û�����'].append(n[1])
            dict2['�ֻ���'].append(n[0])
            dict2['IMSI'].append(n[2])
            dict2['IMEI'].append(n[3])
            #dict2['��ʼʱ��'].append(n[4])
            #dict2['LAC'].append(n[5])
            #dict2['CI'].append(n[6])
            dict2['����'].append(n6)               #�˴���ȥ�����з���
            #dict2['ҵ��ʱ��'].append(int(n[8]))
            dict2['�ն�����'].append(n[4])
            dict2['�ײ�'].append(n[5])          

        #��ʽ���ֵ�
        df2=DataFrame(dict2)
        #print(df2)

        #df1appenddf2
        j=df1.append(df2)

        #��ȡfilenameǰ�벿�֣��������ļ���
        [des_filename, extname] = os.path.splitext(filename)  
        #out_filename  = des_filename + '_�ϲ�.xlsx'
        out_filename = des_filename + '_�ϲ�.csv'

        #�ѻ�����ݴ洢�����ļ���(excel)
        print( 'Converge file: %s' %out_filename)  
        #j.to_excel(out_filename,sheet_name='Sheet1',index=False)

        #������excel������csv�ļ�
        j.to_csv(out_filename,index=False,encoding="utf_8_sig")

        #����ڴ�
        dict1={'�û�����':[],'�ֻ���':[],'IMSI':[],'IMEI':[],
              '����':[],'�ն�����':[],
              '�ײ�':[]}
        dict2={'�ֻ���':[],'����':[]}
    finally:
        fin1.close()
        fin2.close()
  
if __name__ == '__main__':  
    begin = time.time()  
    CombineDoubleCsv('C:\\Users\\liyue\\Desktop\\�½� Microsoft Excel ������ (2).csv',
                  'C:\\Users\\liyue\\Desktop\\�½� Microsoft Excel ������.csv')
    end = time.time()  
    print('time is %d seconds ' % (end - begin))
