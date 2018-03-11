# -*- coding: cp936 -*-
#���ߣ�����
#���ܣ���ĳһ�н��л�ۣ�����͡���ƽ����������

import os  
import time
import numpy
from pandas import *
  
def convergeByKey(filename):
    fin = open(filename,'r')
    try:

        #�������ֶν������ֵ�
        dict={'�û�����':[],'�ֻ���':[],'LAC':[],'CI':[],
              '����':[],'�ն�����':[]}

        #����txt�ļ�������ֵ䣬�˴��Ǵ洢���ڴ���
        for line in fin:
            m=line.split('\t')
            #m10=m[10].replace('\n','')
            dict['�û�����'].append(m[0])
            dict['�ֻ���'].append(m[1])
            #dict['IMSI'].append(m[2])
            #dict['IMEI'].append(m[3])
            #dict['��ʼʱ��'].append(m[4])
            dict['LAC'].append(m[5])
            dict['CI'].append(m[6])
            dict['����'].append(float(m[7]))
            #dict['ҵ��ʱ��'].append(int(m[8]))
            dict['�ն�����'].append(m[9])
            #dict['�ײ�'].append(m10)           #�˴���ȥ�����з���

        #��ʽ���ֵ�
        df=DataFrame(dict)

        #��ͣ����ֵ������ݻ��,�ֻ�����Ϊkey���Դ����ڴ�
        #j=df.groupby(by=['�ֻ���','�û�����','IMSI','IMEI','�ն�����','�ײ�']).sum().reset_index()

        #���ֵ
        #j=df.groupby(by=['�ֻ���','�û�����','IMSI','IMEI','�ն�����','�ײ�']).mean().reset_index()

        #����
        j=df.groupby(by=['�ֻ���','�û�����','LAC','CI','�ն�����']).count().reset_index()
        shuang=j.groupby(by=['LAC','CI']).count().reset_index()

        #��ȡfilenameǰ�벿�֣��������ļ���
        [des_filename, extname] = os.path.splitext(filename)  
        #out_xlsx  = des_filename + '_ҵ���������.xlsx'
        out_filename = des_filename + '_�û�������.csv'

        #�ѻ�����ݴ洢�����ļ���
        print( 'Converge file: %s' %out_filename)  
        #shuang.to_excel(out_xlsx,sheet_name='Sheet1',index=False)
        shuang.to_csv(out_filename,index=False,encoding="utf_8_sig")

        #����ڴ��е��ֵ�����
        dict={'�û�����':[],'�ֻ���':[],'LAC':[],'CI':[],
              '����':[],'�ն�����':[]}
        #dict.clear()
        
    finally:  
        fin.close()  
  
if __name__ == '__main__':  
    begin = time.time()  
    convergeByKey('D:\\bigdata\\������\\dawangka_hebing_21-22.txt')
    end = time.time()  
    print('time is %d seconds ' % (end - begin))
