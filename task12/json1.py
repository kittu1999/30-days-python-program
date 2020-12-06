person={} 
person['kittu']={
    'name': 'kittu',
    'address':'Andra Pradesh',
    'phone_no':'657389',
    'email_id':None,
    'married':True
    }

person['hani']={
    'name': 'hani',
    'address':'kerala',
    'phone_no':'867549',
    'email_id':'hani@gmail.com',
    'married':False
    }



import json
s=json.dumps(person)
print(s)

with open("file.json","w") as f:
    f.write(s)
