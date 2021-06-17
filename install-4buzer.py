#!/usr/bin/python3
import subprocess
from termcolor import colored
import os
import time

print(os.getcwd()) # Prints Current Directory.
if '/4BUZER' in os.getcwd(): # Checks For /4BUZER in PWD. If user is inside /4BUZER folder then install tool else print error.
    print('Installing 4buzer. Please wait')
    time.sleep(2)
    subprocess.call('chmod +x 4buzer.py',shell=True) # Changes Permission for 4buzer.py file
    subprocess.call('chmod +x banner.py',shell=True) # Changes Permission for banner.py file
    time.sleep(1)
    print('Installing Termcolor library for Python3!\n')
    subprocess.call('pip install termcolor',shell=True) # Installs Termcolor library for Python3
    print(colored('Installation Completed. Type ./4buzer in terminal.','red'))
else:
    print(colored('\nPlease "cd" to 4BUZER folder.','yellow'))
    exit(0)
