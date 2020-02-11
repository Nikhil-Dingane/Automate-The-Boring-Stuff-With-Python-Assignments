def Hello(name,age):
    print('Inside hello function')
    print('Your name is '+str(name)+' and age is '+str(int(age)))
    return age+1;
newage=Hello('nikhil',10)
print('Your age after one year is='+str(int(newage)))