#!/usr/bin/python3
import os
import subprocess
from termcolor import colored
import time


###### Normal Binaries which are always running and not vulnerable to current version. You can add your system normal binaries here.

normal = ['exim4','mount.nfs','pppd','mount.cifs','pkexec',
        'bwrap','chsh','passwd','kismet_cap_linux_bluetooth',
        'kismet_cap_ti_cc_2540','kismet_cap_ti_cc_2531','kismet_cap_nrf_51822','kismet_cap_nxp_kw41z','fusermount3',
        'chfn','gpasswd','mount','newgrp','sudo','su','ntfs-3g',
        'kismet_cap_linux_wifi','kismet_cap_nrf_mousejack','umount']

###### Vulnerable Binaries which are Vulnerable and Suspicious. You can add new Vulnerable Binaries here.

vuln = ['ash','bash','capsh','chmod','chroot',
        'chown','cpulimit','csh','dash','dmsetup',
        'docker','emacs','env','expect','find',
        'flock','gdb','gimp','gtester','hping3',
        'ionice','ip','jjs','jrunscript','ksh',
        'ld-2.30.so','logsave','make','nice','node',
        'nohup','openvpn','perl','php','python2.7',
        'rlwrap','rsync','run-parts','setarch','start-stop-daemon',
        'stdbuf','strace','systemctl','taskset','tclsh','time',
        'timeout','unshare','view','xargs','zsh','python','python3.9']

###### Locations for searching Vulnerable Binaries. You can add your path here.

locations = ['/etc','/bin','/dev','/home','/lib',
        '/lib64','/libx32','/lost+found','/media',
        '/mnt','/opt','/root','/sbin',
        '/srv','/sys','/tmp','/usr']

###### This Binaries are set to be SUID BIT and Vulnerable to 'read/write' .

r_w_vuln = []


def banner():
	try:
            subprocess.call('./banner.py',shell=True)
            print()
	except FileNotFoundError:
		print(colored("[!] The Banner for 4buzer can't be found ! :( ",'red'))
		exit(1)
def perm_checker():
    try:
        vulnerable = 0 
        
        for locate in locations:
            # Searching for SUID BITS inside all files and  folders.
            find_bin = "find "+locate+" -perm -4000 2>/dev/null"

            print(colored('[+] Searching in {}'.format(locate),'white'))
            permis = subprocess.check_output(find_bin,shell=True,text=True).split('\n')
            print('[+] Searched {}\n'.format(locate))      
                        
            for perm in permis:
                bin_name = perm.split('/')
        
                if bin_name[-1] in vuln: # Taking the binary name and matching it with 'vuln' list. for eg:- /usr/bin/nice in bin_name[-1] is nice.
                    print(colored('\n[Vulnerability] Found {} .'.format(perm),'red'))
                    vulnerable += 1
                    print(colored('[Exploit] is available for {} .\n'.format(perm),'yellow'))
                    continue
                elif bin_name[-1] in normal:# Taking the binary name and matching it with 'normal' list. for eg:- /usr/bin/exim4 in bin_name[-1] is exim4.
                    print(colored('[+] Normal binary {}'.format(perm),'green'))
            continue

        if vulnerable >= 1:
            print(colored('\n[FOUND] There is/are {} Vulnerable Binary/ies.'.format(str(vulnerable)),'red'))
        elif vulnerable == 0:
            print(colored('\n[+] Nothing Suspicious Found.','blue'))
            print(colored('[+] Searched All System Files/Folders.','blue'))
    except:
        print(colored('[-] OOps something went wrong !','red'))

def main():
    
    # Calling All Functions

    banner()
    time.sleep(2)
    perm_checker()

main()
