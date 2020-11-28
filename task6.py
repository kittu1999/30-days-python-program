#1
list=[1,3,7,12,56]
for i in list:
    print(i+2)
    
#2
for i in range(5,0,-1):
    for j in  range(i,0,-1):
        print(j, end="")
    print()

#3
n= int(input('enter the no:'))
def fibonacci(n):
    if n<=0:
        print('enter positive no:')
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(n))


#4
def power(x, y): 
	
	if y == 0: 
		return 1
	if y % 2 == 0: 
		return power(x, y // 2) * power(x, y // 2) 
		
	return x * power(x, y // 2) * power(x, y // 2) 
 
def order(x): 
	n = 0
	while (x != 0): 
		n = n + 1
		x = x // 10
		
	return n 
x=int(input('enter the number:'))
def isArmstrong(x): 
	
	n = order(x) 
	temp = x 
	sum1 = 0
	
	while (temp != 0): 
		r = temp % 10
		sum1 = sum1 + power(r, n) 
		temp = temp // 10
	return (sum1 == x) 
print(isArmstrong(x))


#5
n=int(input('enter the number:'))
if n>=0:
    print('the number is positive')
else:
    print('the number is negative')


#6
n=int(input('enter the number of days:'))
if(n%365==0):
    print(n//365,'year(s)')
elif(n%366==0):
    print('it is leaf year')
else:
    year=n//365
    days=n%365
    print(year,'years',days,'day(s)')


#7
import math
a=math.pi/3
b=math.pi/6
print(math.cos(a)*math.sin(b))


#8
a=float(input('enter the first number:'))
b=float(input('enter the second numner'))
x=input('operator=')
if x== '+':
    print('addition of two numbers =',a+b)
elif x== '-':
    print('subration  of two numbers =',a-b)
elif x  == '*':
    print('multiplication of two numbers = ',a*b)
elif x == '/':
    print('division of two numbers =',a/b)
elif x == '%':
    print('modulas of two numbers =',a%b)
else:
    print("Invalid Operator")
    




        
        
