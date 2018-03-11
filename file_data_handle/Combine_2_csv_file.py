# -*- coding: cp936 -*-
#作者：李月
#合并2个csv文件，这个文件其实作用不大，注意打开txt用'\t',打开csv用','

import os  
import time
import numpy
import pandas as pd
from pandas import *

#函数实现的join left on  
def CombineDoubleCsv(filename1,filename2):

    #把文件内容读入内存
    fin1 = open(filename1,'r')
    fin2 = open(filename2,'r')
    try:

        #遍历csv文件，填充字典，此处是存储在内存中
        head1=fin1.readline()

        #把想汇聚字段建立成字典
        dict1={'用户属性':[],'手机号':[],'IMSI':[],'IMEI':[],
              '流量':[],'终端类型':[],
              '套餐':[]}
        
        for line1 in fin1:
            m=line1.split(',')
            m6=m[6].replace('\n','')
            dict1['用户属性'].append(m[1])
            dict1['手机号'].append(m[0])
            dict1['IMSI'].append(m[2])
            dict1['IMEI'].append(m[3])
            #dict1['开始时间'].append(m[4])
            #dict1['LAC'].append(m[5])
            #dict1['CI'].append(m[6])
            dict1['流量'].append(m6)               #此处是去除换行符的
            #dict1['业务时长'].append(int(m[8]))
            dict1['终端类型'].append(m[4])
            dict1['套餐'].append(m[5])          

        #格式化字典
        df1=DataFrame(dict1)
        #print(df1)

         #遍历csv文件，填充字典，此处是存储在内存中
        head2=fin2.readline()

        #把想汇聚字段建立成字典
        dict2={'用户属性':[],'手机号':[],'IMSI':[],'IMEI':[],
              '流量':[],'终端类型':[],
              '套餐':[]}
        
        for line2 in fin2:
            n=line2.split(',')
            n6=n[6].replace('\n','')
            dict2['用户属性'].append(n[1])
            dict2['手机号'].append(n[0])
            dict2['IMSI'].append(n[2])
            dict2['IMEI'].append(n[3])
            #dict2['开始时间'].append(n[4])
            #dict2['LAC'].append(n[5])
            #dict2['CI'].append(n[6])
            dict2['流量'].append(n6)               #此处是去除换行符的
            #dict2['业务时长'].append(int(n[8]))
            dict2['终端类型'].append(n[4])
            dict2['套餐'].append(n[5])          

        #格式化字典
        df2=DataFrame(dict2)
        #print(df2)

        #df1appenddf2
        j=df1.append(df2)

        #获取filename前半部分，生成新文件名
        [des_filename, extname] = os.path.splitext(filename)  
        #out_filename  = des_filename + '_合并.xlsx'
        out_filename = des_filename + '_合并.csv'

        #把汇聚数据存储在新文件中(excel)
        print( 'Converge file: %s' %out_filename)  
        #j.to_excel(out_filename,sheet_name='Sheet1',index=False)

        #不生成excel，生成csv文件
        j.to_csv(out_filename,index=False,encoding="utf_8_sig")

        #清空内存
        dict1={'用户属性':[],'手机号':[],'IMSI':[],'IMEI':[],
              '流量':[],'终端类型':[],
              '套餐':[]}
        dict2={'手机号':[],'年龄':[]}
    finally:
        fin1.close()
        fin2.close()
  
if __name__ == '__main__':  
    begin = time.time()  
    CombineDoubleCsv('C:\\Users\\liyue\\Desktop\\新建 Microsoft Excel 工作表 (2).csv',
                  'C:\\Users\\liyue\\Desktop\\新建 Microsoft Excel 工作表.csv')
    end = time.time()  
    print('time is %d seconds ' % (end - begin))
