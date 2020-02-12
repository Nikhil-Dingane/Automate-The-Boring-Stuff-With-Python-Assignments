import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flipList=[]
    for i in range(100):
        if random.randint(0,1)==1:
            flipList.append('H')
        else:
            flipList.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    counter=0
    previousflip=flipList[0]
    for i in range(1,100):
        if flipList[i]==previousflip:
            counter+=1
        else:
            counter=0
            previousflip=flipList[i]
        if counter==6:
            numberOfStreaks+=1
            counter=0
print('Chance of streak: %s%%' % (numberOfStreaks / 100))