# -*- coding: cp936 -*-
#作者：李月
#功能：为表中增加一列，对其他某列进行分类，注意打开txt用'\t',打开csv用','

import os
import time
import numpy
from pandas import *

def AddClassicColumn(filename):
    fin = open(filename,'r')
    try:

        #把想汇聚字段建立成字典
        dict={'用户属性':[],'手机号':[],'IMSI':[],'IMEI':[],
              '流量':[],'终端类型':[],
              '套餐':[],'流量分段':[]}

        #遍历txt文件，填充字典，此处是存储在内存中,txt文件分隔用'\t'
        head=fin.readline()
        for line in fin:
            m=line.split('\t')
            m6=m[6].strip()
            f6=float(m6)
            dict['用户属性'].append(m[1])
            dict['手机号'].append(m[0])
            dict['IMSI'].append(m[2])
            dict['IMEI'].append(m[3])
            #dict['开始时间'].append(m[4])
            #dict['LAC'].append(m[5])
            #dict['CI'].append(m[6])
            dict['流量'].append(f6)
            #dict['业务时长'].append(int(m[8]))
            dict['终端类型'].append(m[4])
            dict['套餐'].append(m[5])

            #添加分段列，并按要求填充分段类型
            if f6 < 10:
                dict['流量分段'].append('低流量')
            elif f6 < 100:
                dict['流量分段'].append('中流量')
            else:
                dict['流量分段'].append('高流量')

        #格式化字典
        df=DataFrame(dict)

        #获取filename前半部分，生成新文件名
        [des_filename, extname] = os.path.splitext(filename)  
        #out_filename  = des_filename + '_分段.xlsx'
        out_filename = des_filename + '_分段.csv'

        #把汇聚数据存储在新文件中(excel)
        print( 'Converge file: %s' %out_filename)  
        #df.to_excel(out_filename,sheet_name='Sheet1',index=False)

        #不生成excel，生成csv文件
        df.to_csv(out_filename,index=False,encoding="utf_8_sig")

        #清空内存中的字典数据
        dict={'用户属性':[],'手机号':[],'IMSI':[],'IMEI':[],
              '流量':[],'终端类型':[],
              '套餐':[],'流量分段':[]}

    finally:  
        fin.close()              

if __name__ == '__main__':
    begin=time.time()
    print('begin to add column to file...')
    AddClassicColumn('C:\\Users\\liyue\\Desktop\\gprs_20171110_10h_1000.txt')
    print('finish!')
    end=time.time()
    print('time is %d seconds' %(end - begin))
    
