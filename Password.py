import re,sys

pwd=input('Enter your password:')

pwdregexvstrong=re.compile('((?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*~`])){8,}')
pwdregexstrong=re.compile('((?=.*[A-Z])(?=.*[0-9])(?=.*[a-z])){7,}')
pwdregexmild=re.compile('((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])){5,}')
pwdregexweak=re.compile('[a-z]')


mo1=pwdregexvstrong.search(pwd)
mo2=pwdregexstrong.search(pwd)
mo3=pwdregexmild.search(pwd)
mo4=pwdregexweak.search(pwd)

if mo1 != None:
    print('Your password is Very strong!')
    sys.exit()
elif mo2 != None:
    print('Your password is Strong mate!')
    sys.exit()
elif mo3!=None:
    print('Your password is Mild!')
    sys.exit()
elif mo4!=None:
    print('Your password is weak, Weakling!')
    sys.exit()