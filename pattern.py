import time,sys
intend =0
intendIncreament=True

while True:
    print(' '*intend,end='')
    print('********')
    time.sleep(0.1)
    if intendIncreament:
        intend=intend+1
        if intend==20:
            intendIncreament=False
    else:
        intend=intend-1
        if intend==0:
            intendIncreament=True
        
    
