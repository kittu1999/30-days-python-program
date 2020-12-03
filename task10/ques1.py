import re
x=input('enter the text:')
result=re.sub("[A-Za-z0-9]", '', x)
if len(result) == 0:
    print("Yes!It contains only alphabets and numbers")
else:
    print("No it contains other than alphabets and numbers")
