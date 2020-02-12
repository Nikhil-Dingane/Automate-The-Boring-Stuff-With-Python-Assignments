
def listToString(tempList):
    ret=''
    for r in tempList:
        ret=ret+' '+r
    return ret
    
userList=[]
while True:
    print('Enter the list item(or enter nothing to exit)')
    item=input()
    if item=='':
        break
    userList.append(item)
print(listToString(userList))