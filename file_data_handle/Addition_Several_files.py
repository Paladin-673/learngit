# -*- coding: cp936 -*-
#���ߣ�����
#���ܣ��ϲ����txt��csv�ļ�

import os
import time
import sys

#�ļ������ݾ�����ʧ��excelתcsv�Ĺ����з�����

def JoinMoreFile(fromdir,tofilename,todir):

    if not os.path.exists(todir):
        os.mkdir(todir)
    if not os.path.exists(fromdir):
        print('·������')

    outfile = open(os.path.join(todir,tofilename),'wb')
    files = os.listdir(fromdir)
    files.sort()

    buff = []
    sub = 1
    for file in files:
        filepath = os.path.join(fromdir,file)
        infile = open(filepath,'rb')
        if sub <= 1:
            buff = infile.read()
            outfile.write(buff)
            infile.close()
        else:
            head = infile.readline()
            for line in infile:
                buff.append(line)
            outfile.writelines(buff)
            infile.close()
        
        sub += 1
        buff = []
        
if __name__ == '__main__':
    begin=time.time()
    print('begin to Combine more file...')
    JoinMoreFile('C:\\Users\\liyue\\Desktop\\�½��ļ���','�ļ�׷�ӽ��.csv',
                'C:\\Users\\liyue\\Desktop\\׷�ӽ��')
    print('finish!')
    end=time.time()
    print('time is %d seconds' %(end - begin))
    
