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
        'timeout','unshare','view','xargs','zsh','python','python3.9','busybox']

###### Locations for searching Vulnerable Binaries. If You are 'root' and want to search SUID binaries in system then you can add more / folders here. 

locations = ['/bin','/dev','/lib','/lib64',
        '/libx32','/mnt','/opt','/sbin','/usr']

###### This Binaries are set to be SUID BIT and Vulnerable to 'read/write/download/upload' .

rwud_vuln = ['ar','arp','atobm','awk','gawk','base32','base64','basenc','busybox','bridge','cat',
        'column','comm','cp','cpio','ksshell','less','look','lua','lwp-download','csplit',
        'cupsfilter','curl','cut','date','dd','dialog','diff','dig','docker','ed',
        'eqn','expand','file','fmt','fold','grep','gzip','hd','head','hexdump','highlight','iconv',
        'ip','join','jq','mawk','more','nawk','nl','nmap','od','openssl','paste','pg','pr','readelf',
        'restic','rev','sed','shuf','soelim','sort','sqlite3','ss','ssh-keyscan','ssh-keygen',
        'strings','sysctl','tac','tail','tbl','tee','tftp','troff','ul','unexpand','uniq',
        'update-alternatives','uudecode','uuencode','vim','vimdiff','restic','rvim','rview','vpiw','vigr',
        'wget','xmodmap','xxd','xz','zsoelim']


def banner():
	try:
            subprocess.call('./banner.py',shell=True)
            print(colored('\n\t\t\t\t[R00T]    = Exploit will provide root shell.','red'))
            print(colored('\t\t\t\t[R-W-U-D] = Exploit will give privileges to Read, Write, Upload, Download.','magenta'))
            print(colored('\t\t\t\t[Exploit] = Exploit is available for binary.','yellow'))
            print(colored('\t\t\t\t[Normal]  = Binaries are normal not exploitable.','green'))
            time.sleep(5)
            print()
	except FileNotFoundError:
		print(colored("[!] The Banner for 4buzer can't be found ! :( ",'red'))
		exit(1)
def perm_checker():
    try:
        vulnerable = 0
        suspicious = 0
    
        for locate in locations:
            
            # Searching for SUID BITS inside all files and  folders.
            find_bin = "find "+locate+" -perm -4000 2>/dev/null"

            print(colored('[+] Searching in {}'.format(locate),'white'))
            permis = subprocess.check_output(find_bin,shell=True,text=True).split('\n')
            print('[+] Searched {}\n'.format(locate))      

            for perm in permis:
                bin_name = perm.split('/')
                
                # Taking the binary name and matching it with 'vuln' list. for eg:- /usr/bin/nice in bin_name[-1] is nice.

                if bin_name[-1] in vuln:
                    print(colored('\n[R00T] Found {} .'.format(perm),'red'))
                    vulnerable += 1
                    print(colored('[Exploit] is available for {} .\n'.format(perm),'yellow',attrs=['reverse']))
                    continue
                
                # Taking the binary name and matching it with 'normal' list. for eg:- /usr/bin/exim4 in bin_name[-1] is exim4.
                
                elif bin_name[-1] in normal:
                    print(colored('[Normal] binary {}'.format(perm),'green'))
                
                # Taking the binary name and matching it with 'rwud_vuln' list. rwud is read/write/upload/download. Some SUID don't spawn root shell but are vulnerable to Read, Write, Upload, and Download.

                elif bin_name[-1] in rwud_vuln:
                    print(colored('\n[R-W-U-D] Found {}'.format(perm),'magenta'))
                    suspicious += 1
                    print(colored('[Exploit] is available for {}\n'.format(perm),'yellow'))
                    continue
            continue

        if vulnerable >= 1 or suspicious >= 1:
            print(colored('\n[FOUND-R00T] There is/are ( {} ) Vulnerable Binary/ies.'.format(str(vulnerable)),'red'))
            print(colored('\n[FOUND-RWUD] There is/are ( {} ) Vulnerable Binary/ies.'.format(str(suspicious)),'magenta'))
        elif vulnerable == 0:
            print(colored('\n[+] Nothing Suspicious Found.','blue'))
            print(colored('[+] Searched All Accessible Files/Folders.','blue'))
    except:
        print(colored('[-] OOps something went wrong !','red'))

def main():
    
    # Calling All Functions

    banner()
    time.sleep(2)
    perm_checker()

main()
