#!/usr/bin/python3
import subprocess
# from termcolor import colored #Uncomment this line if you have 4buzer installed.
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
    print('Installation Completed. Type ./4buzer in terminal.')
else:
    print('\nPlease "cd" to 4BUZER folder.')
    exit(0)
