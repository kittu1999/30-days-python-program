#1
colors={1:'orange',2:'red',3:'black'}
fruits={4:'banana',5:'mango'}
merge=colors.update(fruits)
print(colors)


#2
x={'a':'good','b':'bad','c':'boy'}
del x['c']
print(x)


#3
x=[1,2,3,4]
y=['a','b','c','d']
z=dict(zip(x,y))
print(z)


#4
a={'hyd','tam','mum','kol'}
print(len(a))


#5
a={1,2,3,4,5}
b={3,4,8,9,1}
print(a-b)
