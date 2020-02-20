import re
print("Enter the date")
mydate=input()
print(mydate)

dateregex=re.compile(r'\d[0-31]?.*');
mo=dateregex.search(mydate)
print(mo)