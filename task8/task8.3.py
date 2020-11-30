#type error
try:
    a=2+'2'
    print(a)
except TypeError:
    print('it is type error')

#name error
try:
    a='name'
    print(b)
except NameError:
    print('error occured')


#like this we have do for all errors
