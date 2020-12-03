
import re 
s=input('enter the sentence:')
def match(s): 
    pattern = '[A-Z]+$'
    if re.search(pattern, s): 
            return('Yes! it contains only upper case') 
    else: 
            return('No! It does not not contain upper case only') 
print(match(s))
