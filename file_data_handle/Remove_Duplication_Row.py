# -*- coding: cp936 -*-
#作者：李月
#功能：删除重复行

import os
import time

def DulFile(filename):
    [forward_filename,last_filename]=os.path.splitext(filename)
    new_filename = forward_filename + "_dul.txt"
    fout = open(new_filename,'w')
    buff=[]
    fin = open(filename,'r')
    for line in fin:
        tmp = line.strip()
        if tmp not in buff:
            buff.append(tmp)
            fout.write(line)
    buff=[]
    fin.close()
    fout.close()

if __name__ == '__main__':
    begin=time.time()
    print('begin to dul file...')
    DulFile('C:\\Documents and Settings\\Administrator\\桌面\\1.txt')
    print('finish!')
    end=time.time()
    print('time is %d seconds' %(end - begin))
    
