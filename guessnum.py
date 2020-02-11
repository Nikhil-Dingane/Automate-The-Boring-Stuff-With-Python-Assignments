mynum=16
while True:
    print('Guess then number')
    ipnum=input()
    if int(mynum)==int(ipnum):
        print('Your guess is right')
        break;
    elif int(ipnum)>int(mynum):
        print('Your guess is too high')
    elif int(ipnum)<int(mynum):
        print('Your guess is too low')