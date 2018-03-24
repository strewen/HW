#!/usr/bin/env python3
#-*-coding:utf-8-*-
#@author=strewen:

import sys

#求最大公因子
def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

#素数判断函数
def is_prime(number):
    if(not number.isdigit()):
        return False
    number=int(number)
    if(number<=1):
        return False
    
    for i in range(2,number):
        if(number%i==0):
            return False
    return True

#生成小于number且与number互素的数的集合
def create_dataset(number):
    dataset=[];
    for i in range(1,number):
        if(gcd(i,number)==1):
            dataset.append(i)
    return dataset

#判断集合中每个元素都有逆元
def have_eve_inverse(data_set,number):
    data=[]
    for i in data_set:
        for j in data_set:
            if ((i*j)%number==1):
                data.append(i)
                data.append(j)
    data=list(set(data)) #去重
    data.sort()  #排序
    if(data==data_set):
        return True
    else:
        return False

#主函数
if __name__=='__main__':
    p=input('input first prime number:')
    while(not(is_prime(p))):
        print("It's not a prime number!")
        p=input('input again:')
    q=input('input second prime number:')
    while(not(is_prime(q))):
        print("It's not a prime number!")
        q=input('input again:')
    N=int(p)*int(q)
    data=[]
    data=create_dataset(N)
    if(have_eve_inverse(data,N)):
        print("每个元素都有逆元，集合构成群！")
        print('集合元素总数为%d' %len(data))
    else:
        print("每个元素不都有逆元，集合不构成群！/n")
        print('集合元素总数为%d' %len(data))
