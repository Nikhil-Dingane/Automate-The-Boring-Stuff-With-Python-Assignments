#!python3

import time, subprocess

time_left = 60
try:
    while time_left > 0:
        print(time_left)
        time.sleep(1)
        time_left = time_left - 1
    subprocess.Popen(['open', 'alarm.wav'])
except KeyboardInterrupt:
    print ('You canceled the countdown')
