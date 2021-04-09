#!/usr/bin/python3

import subprocess
from termcolor import colored
import os
import time

print(os.getcwd())

if '/4BUZER' in os.getcwd():
    print('Installing 4buzer. Please wait')
    time.sleep(2)
    subprocess.call('chmod +x 4buzer.py',shell=True)
    subprocess.call('chmod +x banner.py',shell=True)
    print(colored('Installation Completed. You can run 4buzer using ./4buzer.py','red'))

else:
    print('Please "cd" to 4BUZER folder.')
    exit(0)
