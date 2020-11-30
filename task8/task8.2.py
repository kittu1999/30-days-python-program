try:
    a=int(input('enter the number1:'))
    b=int(input('enter the number2:'))
    c=int(input('enter the operation:'))

    
    def operation(x,y):
        if c==1:
            print(x+y)
        elif c==2:
            print(x-y)
        elif c==3:
            print(x*y)
        elif c==4:
            print(x/y)
        else:
            print('the given operation is not defined')
    operation(a,b)
except(TypeError, ValueError, ZeroDivisionError, AttributeError, SyntaxError):
    print('something went wrong')
