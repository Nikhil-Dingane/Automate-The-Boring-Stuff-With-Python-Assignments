def collatz(number):
    if int(number)%2==0:
        print(int(number)//2)
        return int(number)//2
    else:
        print(3 * int(number) + 1)
        return (3 * int(number) + 1)


while True:
    print('Enter the number:')
    num=input()
    if collatz(num)==1:
        break;