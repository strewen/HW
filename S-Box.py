#!/usr/bin/env python3
#-*-coding:utf-8-*-
"""
基于拓展的欧几里得算法构造GF(2^8)的S-box
@author:strewen
Create on 2018-2-23
"""

import numpy as np

#获取数的最高位的位置
def getHeightLoction(num):
    num1=num
    for i in range(8,-1,-1):
        temp=2**i
        if(num1&temp!=0):
            return i
#多项式乘法
def times(factor1,factor2):
    sum1=0
    for i in range(0,8):
        if(factor2&(2**i)==2**i):
          sum1=sum1^(factor1<<i)
    return sum1

#返回数的逆元
def getInverse(num):
    v=[1,0]    #初始化v(x)
    w=[0,1]   #初始化w(x)
    current=1
    divisor=num   #除数
    dividend=283  #初始化被除数为x**8+x**4+x**3+x+1
    remainder=divisor  #余数
    quotient=0         #商
    if(num==0):   #0无逆元
        return num 
    #拓展的欧几里得算法
    while(remainder!=1):
        h0=getHeightLoction(divisor)
        h1=getHeightLoction(dividend)
        quotient=2**(h1-h0)
        remainder=dividend^(divisor<<(h1-h0))
        while(remainder>=divisor):
            h1=getHeightLoction(remainder)
            quotient+=2**(h1-h0)
            remainder=remainder^(divisor<<(h1-h0))
        v[current^1]=v[current^1]^times(quotient,v[current])  
        w[current^1]=w[current^1]^times(quotient,w[current])
        dividend=divisor
        divisor=remainder
        current=current^1
    return w[current]

#字节转换
def bit_chage(num):
    arr=np.zeros(8,dtype='int')
    arr2=np.zeros(8,dtype='int')
    c=np.array([1,1,0,0,0,1,1,0,0],dtype='int')

    #将数转为二进制并存在数组中
    for i in range(8):  
        if(num&2**i!=0):
            arr[i]=1
    
    #b[i]'=b[i]^b[(i+4)mod8]^b[(i+5)mod8]^b[(i+6)mod8]^b[(i+7)mod8]^c[i]
    for i in range(8):
        arr2[i]=arr[i]
        for k in range(4,8):
            arr2[i]^=arr[((i+k)%8)]
        arr2[i]^=c[i]
    
    #将数组代表的二进制转换为十进制数
    res=0
    for i in range(7,-1,-1):
        res=res*2
        res+=arr2[i]
    return np.uint8(res)

s_box=np.array(range(256))
s_box2=[]
for i in range(0,256):
    s_box[i]=getInverse(s_box[i]) 
    s_box[i]=bit_chage(s_box[i])
    s_box2.append(hex(s_box[i]))
s_box2=(np.array(s_box2)).reshape((16,16))
#s_box=s_box.reshape((16,16))
#print(s_box)
print(s_box2)
