# -*- coding: cp936 -*-
#���ߣ�����
#���ܣ�Ϊ��������һ�У�������ĳ�н��з��࣬ע���txt��'\t',��csv��','

import os
import time
import numpy
from pandas import *

def AddClassicColumn(filename):
    fin = open(filename,'r')
    try:

        #�������ֶν������ֵ�
        dict={'�û�����':[],'�ֻ���':[],'IMSI':[],'IMEI':[],
              '����':[],'�ն�����':[],
              '�ײ�':[],'�����ֶ�':[]}

        #����txt�ļ�������ֵ䣬�˴��Ǵ洢���ڴ���,txt�ļ��ָ���'\t'
        head=fin.readline()
        for line in fin:
            m=line.split('\t')
            m6=m[6].strip()
            f6=float(m6)
            dict['�û�����'].append(m[1])
            dict['�ֻ���'].append(m[0])
            dict['IMSI'].append(m[2])
            dict['IMEI'].append(m[3])
            #dict['��ʼʱ��'].append(m[4])
            #dict['LAC'].append(m[5])
            #dict['CI'].append(m[6])
            dict['����'].append(f6)
            #dict['ҵ��ʱ��'].append(int(m[8]))
            dict['�ն�����'].append(m[4])
            dict['�ײ�'].append(m[5])

            #��ӷֶ��У�����Ҫ�����ֶ�����
            if f6 < 10:
                dict['�����ֶ�'].append('������')
            elif f6 < 100:
                dict['�����ֶ�'].append('������')
            else:
                dict['�����ֶ�'].append('������')

        #��ʽ���ֵ�
        df=DataFrame(dict)

        #��ȡfilenameǰ�벿�֣��������ļ���
        [des_filename, extname] = os.path.splitext(filename)  
        #out_filename  = des_filename + '_�ֶ�.xlsx'
        out_filename = des_filename + '_�ֶ�.csv'

        #�ѻ�����ݴ洢�����ļ���(excel)
        print( 'Converge file: %s' %out_filename)  
        #df.to_excel(out_filename,sheet_name='Sheet1',index=False)

        #������excel������csv�ļ�
        df.to_csv(out_filename,index=False,encoding="utf_8_sig")

        #����ڴ��е��ֵ�����
        dict={'�û�����':[],'�ֻ���':[],'IMSI':[],'IMEI':[],
              '����':[],'�ն�����':[],
              '�ײ�':[],'�����ֶ�':[]}

    finally:  
        fin.close()              

if __name__ == '__main__':
    begin=time.time()
    print('begin to add column to file...')
    AddClassicColumn('C:\\Users\\liyue\\Desktop\\gprs_20171110_10h_1000.txt')
    print('finish!')
    end=time.time()
    print('time is %d seconds' %(end - begin))
    
