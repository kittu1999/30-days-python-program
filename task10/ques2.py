import re
text=input('enter the sentence:')
def check(text):
        patterns = '\a*b.\a*'
        if re.search(patterns,  text):
                return 'Yes!! a and b are found in the text'
        else:
                return('No!! a and b are not found in the text')

print(check(text))
