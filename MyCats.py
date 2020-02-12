catNames=[]
while True:
    print('Enter the name of the cat '+str(len(catNames)+1)+(' Or enter nothing to exit'))
    newCatName=input()
    if newCatName=='':
        break;
    catNames=catNames+[newCatName]
print('Name of the cats are:')
for name in catNames:
    print(name)