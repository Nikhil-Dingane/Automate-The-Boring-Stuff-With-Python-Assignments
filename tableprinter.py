tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printtable(tableData):
    maxWidth=0
    for i in tableData:
        for j in i:
            if(maxWidth<len(j)):
                maxWidth=len(j)
    for i in range(0,len(tableData[0])):
        for j in range(0,len(tableData)):
            print((tableData[i][j]).centre(maxWidth," "),end='')
        print()
printtable(tableData)