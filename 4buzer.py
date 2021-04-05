#!/usr/bin/python3
import os
import subprocess
from termcolor import colored
import time

######## IMPORTANT::::::  I have to add binaries of /usr/lib/ld-2.30.so will do it tommorrow.

# Normal Binaries which are always running and not vulnerable to current version. You can add your system normal binaries here.

normal = ['exim4','mount.nfs','pppd','mount.cifs','pkexec',
        'bwrap','chsh','passwd','kismet_cap_linux_bluetooth',
        'kismet_cap_ti_cc_2540','kismet_cap_ti_cc_2531','kismet_cap_nrf_51822','kismet_cap_nxp_kw41z','fusermount3',
        'chfn','gpasswd','mount','newgrp','sudo','su','ntfs-3g',
        'kismet_cap_linux_wifi','kismet_cap_nrf_mousejack','umount']

# Vulnerable Binaries which are Vulnerable and Suspicious. You can add new Vulnerable Binaries here.

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

# This Binaries are not inside the /usr/bin. This binaries are located inside /usr/sbin and /usr/lib/ and /usr/lib32

other = []
def banner():
	try:
		subprocess.call('./banner.py',shell=True)
	except FileNotFoundError:
		print(colored("[!] The Banner for 4buzer can't be found ! :( ",'red'))
		exit(1)
def perm_checker():
    try:
        #####  #####  # #   # BIN
        #####    #    #  # #
        #####  #####  #   #

        vulnerable = 0 
        sbin_vuln = 0
        
        # Searching for SUID BITS inside /usr/bin folder.
        find_bin = "find /usr/bin -perm -4000"
        
        print(colored('\n[+] Searching in bin/\n','white'))
        permis = subprocess.check_output(find_bin,shell=True,text=True).split('\n')
        
        for perm in permis:
            bin_name = perm.split('/')
        
            if bin_name[-1] in vuln: # Taking the binary name and matching it with 'vuln' list. for eg:- /usr/bin/nice in bin_name[-1] is nice.
                print(colored('\n[Vulnerability] Found {} .'.format(perm),'red'))
                vulnerable += 1
                print(colored('[Exploit] is available for {} .\n'.format(perm),'yellow'))
                continue
            elif bin_name[-1] in normal:# Taking the binary name and matching it with 'normal' list. for eg:- /usr/bin/exim4 in bin_name[-1] is exim4.
                print(colored('[+] Normal binary {}'.format(perm),'green'))
        
        if vulnerable >= 1:
            print(colored('\n[FOUND] There are {} Vulnerable Binaries inside /usr/bin.'.format(str(vulnerable)),'red'))
        elif vulnerable == 0:
            print(colored('\n[+] Nothing Suspicious Found in /usr/bin\n','blue'))
        
        #    # # # ##### #####  # #  # SBIN
        #    # # # #####   #    # # #
        #    # # # ##### #####  #  #
        
        time.sleep(2)
        # Searching for SUID BITS inside /usr/sbin foler.
        find_sbin = "find /usr/sbin -perm -4000"
        
        print(colored('\n[+] Searching in sbin/\n','white'))
        sbin_permis = subprocess.check_output(find_sbin,shell=True,text=True).split('\n')

        for sbin_perm in sbin_permis:
            sbin_name = sbin_perm.split('/')

            if sbin_name[-1] in vuln: # Taking the binary name and matching it with 'vuln' list. for eg:- /usr/sbin/openvpn in sbin_name[-1] is openvpn.
                print(colored('\n[Vulnerability] Found {} .'.format(sbin_perm),'red'))
                sbin_vuln += 1
                print(colored('[Exploit] is available for {} .\n'.format(sbin_perm),'yellow'))
                continue
            elif sbin_name[-1] in normal: # Taking the binary name and matching it with 'normal' list. for eg:- /usr/sbin/exim4 in sbin_name[-1] is exim4.
                print(colored('[+] Normal binary {}'.format(sbin_perm),'green'))
        if sbin_vuln >= 1:
            print(colored('\n[FOUND] There are {} Vulnerable Binaries inside /usr/sbin/'.format(str(sbin_vuln)),'red'))
        elif sbin_vuln == 0:
            print(colored('\n[+] Nothing Suspicious Found in /usr/sbin/\n','blue'))

    except:
        print(colored('[-] OOps something went wrong !','red'))
banner()
time.sleep(2)
perm_checker()
