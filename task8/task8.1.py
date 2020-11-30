# 1.index error
n=[1,2,3,4]
try:
    a=int(input('enter the index num:'))
    print(n[a])
except IndexError:
    print('your enter index num is out of range:')


#2.key error
D1={'1':"aa", '2':"bb", '3':"cc"}
try:
    print(D1['9'])
except KeyError:
    print('the key element is not found')

#3. import error
import math
try:
    from math import cube
except:
    print('in math cube is not present')


#4.value error
a='xyz'
try:
    print(int(a))
except  :
    print('you entered A string is ')

#there are lot erros like type error,zero devision error...etc



    
