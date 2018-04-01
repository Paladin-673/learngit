# -*- coding: cp936 -*-
#���ߣ�����
#���ܣ��Զ���ָ���ļ�תΪutf8��ʽ

import os
import time
import sys
import chardet
import codecs

#�鿴��ǰ�ļ������ʽ,��ʵ�ֱ���ת��
def convertCode(fromfile,tofile,target_code):
    result_list = []
    #���ļ�
    readfile = codecs.open(fromfile,'rb')
    #�����ļ�д���ڴ�
    buff = readfile.read()
    result = chardet.detect(buff)
    source_code = result['encoding']
    confidence = result['confidence']
    #ԭ�ļ��ı��뷽ʽд������
    result_list.append(source_code)
    result_list.append(confidence)
    #���ļ������ݽ��벢����
    filedata = buff.decode(source_code,'ignore')
    filedata_utf8 = filedata.encode(target_code)
    #д�ļ�
    writefile = open(tofile,'wb')
    writefile.write(filedata_utf8)
    readfile.close()
    writefile.close()
    
    return result_list
    

#�����ļ���,ת��ÿ���ļ�
def traverseDir(fromdir):
    if not os.path.exists(fromdir):
        print("·������")
    
    i = 1  #ת���ļ�����
    target_code = 'utf-8'  #Ŀ������ʽ

    files = os.listdir(fromdir)
    
    for file in files:
        fromfilepath = os.path.join(fromdir,file)
        [des_filename,extname] = os.path.splitext(fromfilepath)
        tofilepath = des_filename + '_utf-8.csv'
        print('��ʼת����%d���ļ�...' % i)
        tolist = convertCode(fromfilepath,tofilepath,target_code)
        print('ת����ɣ��ļ� %s ��ԭ�����ʽΪ�� %s ��׼ȷ��Ϊ��%.2f%%' %(file,tolist[0],tolist[1] * 100))

        i = i + 1
        tolist = []


    
if __name__ == '__main__':
    begin = time.time()
    traverseDir("E:\\learngit\\learngit\\py_to_utf8\\ת��")
    end = time.time()
    print("It tooks %d seconds" % (end - begin))
