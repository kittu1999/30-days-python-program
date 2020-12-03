import re
list= re.finditer(r"([0-9]{1,3})", "These are the numberss 4,5,22,3,0000,234 and 43")
print("The Numbers of length 1 to 3 are")
for n in list:
     print(n.group(1))
