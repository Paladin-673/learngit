# -*- coding: cp936 -*-
#���ߣ�����
#���ܣ�˫��Groupby��һ������2�μ������ܣ�Ҳ��ȥ�ع���
 
import os  
import time
import numpy
from pandas import *
  
def convergeByKey(filename):
    fin = open(filename,'r')
    try:

        #�������ֶν������ֵ�
        dict={'�ֻ���':[],'�ײ�':[],'��ʼʱ��':[]}

        #����txt�ļ�������ֵ䣬�˴��Ǵ洢���ڴ���
        for line in fin:
            m=line.split('\t')
            m10=m[10].replace('\n','')
            #dict['�û�����'].append(m[0])
            dict['�ֻ���'].append(m[1])
            #dict['IMSI'].append(m[2])
            #dict['IMEI'].append(m[3])
            dict['��ʼʱ��'].append(m[4])
            #dict['LAC'].append(m[5])
            #dict['CI'].append(m[6])
            #dict['����'].append(float(m[7]))
            #dict['ҵ��ʱ��'].append(int(m[8]))
            #dict['�ն�����'].append(m[9])
            dict['�ײ�'].append(m10)           #�˴���ȥ�����з���

        #��ʽ���ֵ�
        df=DataFrame(dict)

        #��ͣ����ֵ������ݻ��,�ֻ�����Ϊkey���Դ����ڴ�
        #j=df.groupby(by=['�ֻ���','�û�����','IMSI','IMEI','�ն�����','�ײ�']).sum().reset_index()

        #���ֵ
        #j=df.groupby(by=['�ֻ���','�û�����','IMSI','IMEI','�ն�����','�ײ�']).mean().reset_index()

        #����
        d=df.groupby(by=['�ֻ���','�ײ�']).count().reset_index()

        #�ڶ��ؼ���
        j=d.groupby(by=['�ײ�']).count().reset_index()
        
        #��ȡfilenameǰ�벿�֣��������ļ���
        [des_filename, extname] = os.path.splitext(filename)  
        #out_filename  = des_filename + '_˫�ػ��ܼ���.xlsx'
        out_filename = des_filename + '_˫�ػ��ܼ���.csv'

        #�ѻ�����ݴ洢�����ļ���(excel)
        print( 'Converge file: %s' %out_filename)  
        #j.to_excel(out_filename,sheet_name='Sheet1',index=False)

        #������excel������csv�ļ�
        j.to_csv(out_filename,index=False,encoding="utf_8_sig")

        #����ڴ��е��ֵ�����
        dict={'�ײ�':[]}
    finally:  
        fin.close()  
  
if __name__ == '__main__':  
    begin = time.time()  
    convergeByKey('D:\\bigdata\\gprs_20171111_0.txt')
    end = time.time()  
    print('time is %d seconds ' % (end - begin))
