import re
s=input('enter the string:')
def end_num(s):
    text = re.compile(r".*[0-9]$")
    if text.match(s):
        return 'Yes!Number is present at the end of string'
    else:
        return 'No!Number is not present at the end of string'

print(end_num(s))
