import xml.etree.ElementTree as ET
from collections import defaultdict
import operator
import sys

stop_words = input().split(';')
index_terms = input().split(';')

#document_xml = input()
document_xml = str(sys.stdin.read())
document_xml = document_xml.lower()

tree = ET.fromstring(document_xml)

special_tags = ['title', 'abstract', 'body']

punctuation = [',' , '.' , '?' , '!']

def normalize(data):
    normalised=''
    for char in data:
        if char not in punctuation:
            normalised = normalised+char

    data = normalised.split(' ')
    return data

def count(data):
    length=0
    for j in data:
        if j not in stop_words:
            if(len(j)>=4):
                length+=1
    return length

l1=l2=l3=0

d=defaultdict(int)

for i in special_tags:
    e=tree.find(i)
    if(i=='title'):
        if not e:
        #no nested tags
            l = tree.findall('.//title')
            for tag in l:
                #print(tag)
                data1=tag.text
                d1=[]
                d1=normalize(data1)
                l1=count(d1)
                for j in d1:
                    for k in index_terms:
                        if k==j:
                            d[k]+=5
                            
        else:
            for tags in tree.find('.//title').iter():

                data1=tags.text
                data1=data1.split(' ')

                normalised=''

                for strings in data1:
                    for char in strings:
                        if char not in punctuation:
                            normalised = normalised+char
                    normalised+=' '
                   
                data1 = normalised.split(' ')
                for j in data1:
                    if j not in stop_words:
                        if(len(j)>=4):
                            l3+=1
                    for k in index_terms:
                        if k==j:
                            d[k]+=5

    elif(i=='abstract'):
        if not e:
        #no nested tags
            l = tree.findall('.//abstract')
            for tag in l:
                #print(tag)
                data2=tag.text
                d2=[]
                d2=normalize(data2)
                l2=count(d2)
                for j in d2:
                    for k in index_terms:
                        if k==j:
                            d[k]+=3
        else:
            for tags in tree.find('.//abstract').iter():

                data2=tags.text
                data2=data2.split(' ')

                normalised=''

                for strings in data2:
                    for char in strings:
                        if char not in punctuation:
                            normalised = normalised+char
                    normalised+=' '
                   
                data2 = normalised.split(' ')
                for j in data2:
                    if j not in stop_words:
                        if(len(j)>=4):
                            l3+=1
                    for k in index_terms:
                        if k==j:
                            d[k]+=3

    elif(i=='body'):
        if not e:
        #no nested tags
            l = tree.findall('.//abstract')
            for tag in l:
                #print(tag)
                data3=tag.text
                d3=[]
                d3=normalize(data3)
                l3=count(d3)
                for j in d3:
                    for k in index_terms:
                        if k==j:
                            d[k]+=1
                            
        else:
            for tags in tree.find('.//body').iter():

                data3=tags.text
                data3=data3.split(' ')

                normalised=''

                for strings in data3:
                    for char in strings:
                        if char not in punctuation:
                            normalised = normalised+char
                    normalised+=' '
                   
                data3 = normalised.split(' ')
                for j in data3:
                    if j not in stop_words:
                        if(len(j)>=4):
                            l3+=1
                    for k in index_terms:
                        if k==j:
                            d[k]+=1
    
#print(d)
#print(l1,l2,l3)
L=l1+l2+l3

kd={}
for k in d.keys():
    den=float(d[k]/L)*100
    kd[k]=den;

#kd = sorted(kd.items(), key=lambda x: x[1], reverse=True)
kd = dict( sorted(kd.items(), key=operator.itemgetter(1),reverse=True))

flag=0
for q,r in kd.items():
    flag+=1
    if(flag<=3):
        q=q+':'
        print(q,r)
        f=r
    if(flag==4):
        if(r==f):
            q=q+':'
            print(q,r)
