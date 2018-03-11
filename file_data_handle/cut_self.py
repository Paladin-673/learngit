# -*- coding: cp936 -*-

f = open("C:\\Users\\liyue\\Desktop\\试验.txt",'r')       # 返回一个文件对象 
#line = f.readline()       # 调用文件的 readline()方法 
for line in f:
    m=line.split('\t')
    if m[1]=='小明':
        print(line),       # 后面跟 ',' 将忽略换行符  
    #line = f.readline() 
 
f.close() 
