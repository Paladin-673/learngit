# -*- coding: cp936 -*-
#作者：李月
#功能：自动把指定文件转为utf8格式

import os
import time
import sys
import chardet
import codecs

#查看当前文件编码格式,并实现编码转换
def convertCode(fromfile,tofile,target_code):
    result_list = []
    #读文件
    readfile = codecs.open(fromfile,'rb')
    #读的文件写入内存
    buff = readfile.read()
    result = chardet.detect(buff)
    source_code = result['encoding']
    confidence = result['confidence']
    #原文件的编码方式写入数组
    result_list.append(source_code)
    result_list.append(confidence)
    #读文件的内容解码并编码
    filedata = buff.decode(source_code,'ignore')
    filedata_utf8 = filedata.encode(target_code)
    #写文件
    writefile = open(tofile,'wb')
    writefile.write(filedata_utf8)
    readfile.close()
    writefile.close()
    
    return result_list
    

#遍历文件夹,转换每个文件
def traverseDir(fromdir):
    if not os.path.exists(fromdir):
        print("路径错误！")
    
    i = 1  #转换文件计数
    target_code = 'utf-8'  #目标编码格式

    files = os.listdir(fromdir)
    
    for file in files:
        fromfilepath = os.path.join(fromdir,file)
        [des_filename,extname] = os.path.splitext(fromfilepath)
        tofilepath = des_filename + '_utf-8.csv'
        print('开始转换第%d个文件...' % i)
        tolist = convertCode(fromfilepath,tofilepath,target_code)
        print('转换完成！文件 %s 的原编码格式为： %s ，准确率为：%.2f%%' %(file,tolist[0],tolist[1] * 100))

        i = i + 1
        tolist = []


    
if __name__ == '__main__':
    begin = time.time()
    traverseDir("E:\\learngit\\learngit\\py_to_utf8\\转换")
    end = time.time()
    print("It tooks %d seconds" % (end - begin))
