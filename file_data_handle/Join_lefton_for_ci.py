# -*- coding: cp936 -*-
#作者：李月
#功能：左join，对第一个表进行vlookup

import os  
import time
import numpy
import pandas as pd
from pandas import *

#函数实现的join left on  
def JoinDoubleCsv(filename1,filename2):

    #把文件内容读入内存
    fin1 = open(filename1,'r',encoding='gb18030',errors='ignore')
    fin2 = open(filename2,'r',encoding='gb18030',errors='ignore')
    try:

        #遍历csv文件，填充字典，此处是存储在内存中
        head1=fin1.readline()

        #把想汇聚字段建立成字典
        dict1={'手机号':[],'LAC':[],'CI':[]}
        
        for line1 in fin1:
            m=line1.split(',')
            #dict1['用户属性'].append(m[1])
            dict1['手机号'].append(m[2])
            dict1['LAC'].append(m[0])
            dict1['CI'].append(m[1])
            #dict1['开始时间'].append(m[4])
            #dict1['LAC'].append(m[5])
            #dict1['CI'].append(m[6])
            #dict1['流量'].append(m6)               #此处是去除换行符的
            #dict1['业务时长'].append(int(m[8]))
            #dict1['终端类型'].append(m[4])
            #dict1['套餐'].append(m[5])          

        #格式化字典
        df1=DataFrame(dict1)
        #print(df1)

         #遍历csv文件，填充字典，此处是存储在内存中
        head2=fin2.readline()

        #把想汇聚字段建立成字典
        dict2={'CI':[],'经度':[],'纬度':[]}
        
        for line2 in fin2:
            n=line2.split(',')
            n2=n[2].replace('\n','')
            #dict2['用户属性'].append(n[1])
            dict2['CI'].append(n[0])
            dict2['经度'].append(n[1])
            dict2['纬度'].append(n2)
            #dict2['开始时间'].append(n[4])
            #dict2['LAC'].append(n[5])
            #dict2['CI'].append(n[6])
            #dict2['流量'].append(n6)               #此处是去除换行符的
            #dict2['业务时长'].append(int(n[8]))
            #dict2['终端类型'].append(n[4])
            #dict2['套餐'].append(n[5])          

        #格式化字典
        df2=DataFrame(dict2)
        #print(df2)

        #left join相当于对左边表的vlookup，如果字段不唯一，会join出多行
        j=pd.merge(df1,df2,how='left',on='CI')

        #获取filename前半部分，生成新文件名
        [des_filename, extname] = os.path.splitext(filename1)  
        out_filename  = des_filename + '_vlookup.xlsx'
        #out_filename = des_filename + '_vlookup.csv'

        #把汇聚数据存储在新文件中(excel)
        print( 'Converge file: %s' %out_filename)  
        j.to_excel(out_filename,sheet_name='Sheet1',index=False)

        #不生成excel，生成csv文件
        #j.to_csv(out_filename,index=False,encoding="utf_8_sig")

        #清空内存
        dict1={'手机号':[],'LAC':[],'CI':[]}
        dict2={'CI':[],'经度':[],'纬度':[]}
    finally:
        fin1.close()
        fin2.close()
  
if __name__ == '__main__':  
    begin = time.time()  
    JoinDoubleCsv('D:\\bigdata\\大王卡\huizong\\dawangka_hebing_21-22_用户数汇总.csv',
                  'D:\\bigdata\\大王卡\huizong\\ci-jingweidu.csv')
    end = time.time()  
    print('time is %d seconds ' % (end - begin))
