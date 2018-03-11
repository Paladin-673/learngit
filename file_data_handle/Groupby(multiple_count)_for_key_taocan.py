# -*- coding: cp936 -*-
#作者：李月
#功能：双重Groupby，一般用于2次计数汇总，也有去重功能
 
import os  
import time
import numpy
from pandas import *
  
def convergeByKey(filename):
    fin = open(filename,'r')
    try:

        #把想汇聚字段建立成字典
        dict={'手机号':[],'套餐':[],'开始时间':[]}

        #遍历txt文件，填充字典，此处是存储在内存中
        for line in fin:
            m=line.split('\t')
            m10=m[10].replace('\n','')
            #dict['用户属性'].append(m[0])
            dict['手机号'].append(m[1])
            #dict['IMSI'].append(m[2])
            #dict['IMEI'].append(m[3])
            dict['开始时间'].append(m[4])
            #dict['LAC'].append(m[5])
            #dict['CI'].append(m[6])
            #dict['流量'].append(float(m[7]))
            #dict['业务时长'].append(int(m[8]))
            #dict['终端类型'].append(m[9])
            dict['套餐'].append(m10)           #此处是去除换行符的

        #格式化字典
        df=DataFrame(dict)

        #求和：对字典中数据汇聚,手机号作为key，仍存在内存
        #j=df.groupby(by=['手机号','用户属性','IMSI','IMEI','终端类型','套餐']).sum().reset_index()

        #求均值
        #j=df.groupby(by=['手机号','用户属性','IMSI','IMEI','终端类型','套餐']).mean().reset_index()

        #计数
        d=df.groupby(by=['手机号','套餐']).count().reset_index()

        #第二重计数
        j=d.groupby(by=['套餐']).count().reset_index()
        
        #获取filename前半部分，生成新文件名
        [des_filename, extname] = os.path.splitext(filename)  
        #out_filename  = des_filename + '_双重汇总计数.xlsx'
        out_filename = des_filename + '_双重汇总计数.csv'

        #把汇聚数据存储在新文件中(excel)
        print( 'Converge file: %s' %out_filename)  
        #j.to_excel(out_filename,sheet_name='Sheet1',index=False)

        #不生成excel，生成csv文件
        j.to_csv(out_filename,index=False,encoding="utf_8_sig")

        #清空内存中的字典数据
        dict={'套餐':[]}
    finally:  
        fin.close()  
  
if __name__ == '__main__':  
    begin = time.time()  
    convergeByKey('D:\\bigdata\\gprs_20171111_0.txt')
    end = time.time()  
    print('time is %d seconds ' % (end - begin))
