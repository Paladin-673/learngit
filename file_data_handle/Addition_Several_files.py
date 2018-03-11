# -*- coding: cp936 -*-
#作者：李月
#功能：合并多个txt或csv文件

import os
import time
import sys

#文件中数据精度损失是excel转csv的过程中发生的

def JoinMoreFile(fromdir,tofilename,todir):

    if not os.path.exists(todir):
        os.mkdir(todir)
    if not os.path.exists(fromdir):
        print('路径错误')

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
    JoinMoreFile('C:\\Users\\liyue\\Desktop\\新建文件夹','文件追加结果.csv',
                'C:\\Users\\liyue\\Desktop\\追加结果')
    print('finish!')
    end=time.time()
    print('time is %d seconds' %(end - begin))
    
