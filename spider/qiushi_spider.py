#!C:\python27\
# -*- coding: cp936 -*-
#���°ٿ����棬���ַ��㣬python�汾Ϊ2.7

__author__='Moon'


import urllib
import urllib2
import re
import thread
import time

#���°ٿ�������
class QSBK:

    #��ʼ������������һЩ����
    def __init__(self):
        self.pageIndex=1
        self.user_agent='Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)'
        #��ʼ��headers
        self.headers={'User-Agent':self.user_agent}
        #��Ŷ��ӵı�����ÿһ��Ԫ����ÿһҳ�Ķ�����
        self.stories=[]
        #����Ƿ�������еı���
        self.enable=False

    #����ĳһҳ���������ҳ�����
    def getPage(self,pageIndex):
        try:
            url='http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            #���������request
            request=urllib2.Request(url,headers=self.headers)
            #����urlopen��ȡҳ�����
            response=urllib2.urlopen(request)
            #��ҳ��ת��ΪUTF-8����
            pageCode=response.read().decode('utf-8')
            return pageCode

        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"�������°ٿ�ʧ�ܣ�����ԭ��",e.reason
                return None

    #����ĳһҳ���룬���ر�ҳ����ͼƬ�Ķ����б�
    def getPageItems(self,pageIndex):
        pageCode=self.getPage(pageIndex)
        if not pageCode:
            print "ҳ�����ʧ��...."
            return None
        pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>(.*?)<div class="stats">.*?<i class="number">(.*?)</i>.*?</span>', re.S)
        items=re.findall(pattern,pageCode)
        #�����洢ÿҳ�Ķ�����
        pageStories=[]
        #����������ʽƥ�����Ϣ
        for item in items:
            #�Ƿ���ͼƬ
            haveImg=re.search("img",item[2])
            #���������ͼƬ����������list��
            if not haveImg:
                replaceBR=re.compile('<br/>')
                text=re.sub(replaceBR,"\n",item[1])
                #item[0]��һ�����ӵķ����ߣ�item[1]�Ƕ������ݣ�item[3]�ǵ�����
                pageStories.append([item[0].strip(),text.strip(),item[3].strip()])
        return pageStories

    #���ز���ȡҳ������ݣ����뵽�б���
    def loadPage(self):
        #�����ǰδ����ҳ������2ҳ���������һҳ
        if self.enable==True:
            if len(self.stories)<2:
                #��ȡ�µ�һҳ
                pageStories=self.getPageItems(self.pageIndex)
                #����ҳ�Ķ��Ӵ�ŵ�ȫ��list��
                if pageStories:
                    self.stories.append(pageStories)
                    #��ȡ��֮��ҳ��������һ����ʾ�´ζ�ȡ��һҳ
                    self.pageIndex+=1

    #���ø÷�����ÿ���ûس���ӡ���һ������
    def getOneStory(self,pageStories,page):
        #����һҳ�Ķ���
        for story in pageStories:
            #�ȴ��û�����
            input=raw_input()
            #ÿ������س�һ�Σ��ж�һ���Ƿ�Ҫ������ҳ��
            self.loadPage()
            #�������Q��������
            if input=="Q":
                self.enable=False
                return
            print u"��%dҳ\t�����ˣ�%s\t�ޣ�%s\n%s"%(page,story[0],story[2],story[1])

    #��ʼ����
    def start(self):
        print u"���ڶ�ȡ���°ٿƣ����س��鿴�¶��ӣ���Q�˳�"
        #ʹ����ΪTrue�����������������
        self.enable=True
        #�ȼ���һҳ����
        self.loadPage()
        #�ֲ����������Ƶ�ǰ�����˵ڼ�ҳ
        nowPage=0
        while self.enable:
            if len(self.stories)>0:
                #��ȫ��list�л�ȡһҳ�Ķ���
                pageStories=self.stories[0]
                #��ǰ������ҳ����һ
                nowPage+=1
                #��ȫ��list�е�һ��Ԫ��ɾ������Ϊ�Ѿ�ȡ��
                del self.stories[0]
                #�����ҳ�Ķ���
                self.getOneStory(pageStories,nowPage)

if __name__=="__main__":
    spider=QSBK()
    spider.start()
