# -*- coding: cp936 -*-
#作者：李月
#功能：对某一列进行汇聚，如求和、求平均、计数等

import os  
import time
import numpy
from pandas import *
  
def convergeByKey(filename):
    fin = open(filename,'r')
    try:

        #把想汇聚字段建立成字典
        dict={'用户属性':[],'手机号':[],'LAC':[],'CI':[],
              '流量':[],'终端类型':[]}

        #遍历txt文件，填充字典，此处是存储在内存中
        for line in fin:
            m=line.split('\t')
            #m10=m[10].replace('\n','')
            dict['用户属性'].append(m[0])
            dict['手机号'].append(m[1])
            #dict['IMSI'].append(m[2])
            #dict['IMEI'].append(m[3])
            #dict['开始时间'].append(m[4])
            dict['LAC'].append(m[5])
            dict['CI'].append(m[6])
            dict['流量'].append(float(m[7]))
            #dict['业务时长'].append(int(m[8]))
            dict['终端类型'].append(m[9])
            #dict['套餐'].append(m10)           #此处是去除换行符的

        #格式化字典
        df=DataFrame(dict)

        #求和：对字典中数据汇聚,手机号作为key，仍存在内存
        #j=df.groupby(by=['手机号','用户属性','IMSI','IMEI','终端类型','套餐']).sum().reset_index()

        #求均值
        #j=df.groupby(by=['手机号','用户属性','IMSI','IMEI','终端类型','套餐']).mean().reset_index()

        #计数
        j=df.groupby(by=['手机号','用户属性','LAC','CI','终端类型']).count().reset_index()
        shuang=j.groupby(by=['LAC','CI']).count().reset_index()

        #获取filename前半部分，生成新文件名
        [des_filename, extname] = os.path.splitext(filename)  
        #out_xlsx  = des_filename + '_业务次数汇总.xlsx'
        out_filename = des_filename + '_用户数汇总.csv'

        #把汇聚数据存储在新文件中
        print( 'Converge file: %s' %out_filename)  
        #shuang.to_excel(out_xlsx,sheet_name='Sheet1',index=False)
        shuang.to_csv(out_filename,index=False,encoding="utf_8_sig")

        #清空内存中的字典数据
        dict={'用户属性':[],'手机号':[],'LAC':[],'CI':[],
              '流量':[],'终端类型':[]}
        #dict.clear()
        
    finally:  
        fin.close()  
  
if __name__ == '__main__':  
    begin = time.time()  
    convergeByKey('D:\\bigdata\\大王卡\\dawangka_hebing_21-22.txt')
    end = time.time()  
    print('time is %d seconds ' % (end - begin))
