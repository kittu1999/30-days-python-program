#1
a=int(input('enter the number1:'))
b=int(input('enter the number2:'))
def operation(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
operation(a,b)


#2
x=str(input('enter the patient name:'))
def covid(patient_name, body_temparature=98):
    print('patient name is:', patient_name ,',the temparature of the body is:', body_temparature)
covid(x)


