#!/usr/bin/python3
import os
import subprocess
from termcolor import colored
import time

#####################################################################################################################
#                                                                                                                   #
# Author : Akash Pandey a.k.a L3V1ATH0N                                                                             #
# Date :   05/04/2021                                                                                               #
# Message to Script Kiddies : Remember Changing Author Name will never make you 1337. Appreciate someone's hardwork.#
# Tool For : Anyone who is interested in Security or wants to test their binaries.                                  #
#                                                                                                                   #
#####################################################################################################################


###### Normal Binaries which are always running and not vulnerable to current version. You can add your system normal binaries here.

normal = ['exim4','mount.nfs','pppd','mount.cifs','pkexec',
        'bwrap','chsh','passwd','kismet_cap_linux_bluetooth',
        'kismet_cap_ti_cc_2540','kismet_cap_ti_cc_2531','kismet_cap_nrf_51822','kismet_cap_nxp_kw41z','fusermount3',
        'chfn','gpasswd','mount','newgrp','sudo','su','ntfs-3g',
        'kismet_cap_linux_wifi','kismet_cap_nrf_mousejack','umount','ssh-keysign','Xorg.wrap']

###### Vulnerable Binaries which are Vulnerable and Suspicious. You can add new Vulnerable Binaries here.

vuln = ['ash','bash','capsh','chmod','chroot',
        'chown','cpulimit','bsd-csh','dash','dmsetup',
        'docker','emacs-gtk','env','expect','find',
        'flock','gdb','gimp-2.10','gtester','hping3',
        'ionice','ip','jjs','jrunscript','ksh93',
        'ld-2.30.so','logsave','make','nice','node',
        'nohup','openvpn','perl','php7.4','python',
        'rlwrap','rsync','run-parts','rview','vim.gtk3','setarch','start-stop-daemon',
        'stdbuf','strace','systemctl','taskset','tclsh8.6','time',
        'timeout','unshare','view','xargs','zsh','busybox','python2.7','python3.8']

###### Locations for searching Vulnerable Binaries. If You are 'root' and want to search SUID binaries in system then you can add more / folders here. 

locations = ['/bin','/dev','/lib','/lib64','/etc/alternatives',
        '/libx32','/mnt','/opt','/sbin','/usr']

###### This Binaries are set to be SUID BIT and Vulnerable to 'read/write/download/upload' .

rwud_vuln = ['ar','arp','atobm','awk','gawk','base32','base64','basenc','busybox','bridge','cat',
        'column','comm','cp','cpio','ksshell','less','look','lua','lwp-download','csplit',
        'cupsfilter','curl','cut','date','dd','dialog','diff','dig','docker','ed',
        'eqn','expand','file','fmt','fold','grep','gzip','hd','head','hexdump','highlight','iconv',
        'ip','join','jq','mawk','more','nawk','nl','nmap','od','openssl','paste','pg','pr','readelf',
        'restic','rev','sed','shuf','soelim','sort','sqlite3','ss','ssh-keyscan','ssh-keygen',
        'strings','sysctl','tac','tail','tbl','tee','tftp','troff','ul','unexpand','uniq',
        'update-alternatives','uudecode','uuencode','vim','vimdiff','restic','rvim','rview','vpiw','vigr','wget','xmodmap','xxd','xz','zsoelim']

def help():

    print(colored('\nrootex\t - Exploits the SUID binary which provides R00T Shell .','red',attrs=['reverse']))
    print(colored('rwexp\t - Exploits the SUID binary which provides to read/write files.','magenta'))
    print('help\t -  Prints this message.')
    print(colored('exit\t -  Exits the program after scanning.','cyan'))
    print(colored('save\t -  Saves the output in current directory.','green'))
    print(colored('clear\t - Clears the screen softly. You can scroll up to see output.','blue'))
    print(colored('Author\t - Prints the author name.','white'))
    print(colored('lifesaver- Prints the name of a site which helped to save my life :)','red'))
    print(colored('chbin\t - Changes the file permission (Only if you have permission or escalated to r00t ;)','red',attrs=['reverse','bold']))
    
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
            print('[+] Searched {}'.format(locate))      
            exploitroot = [] # For bin_name data to pass to function exploit.
            for perm in permis:

                bin_name = perm.split('/')

                # Taking the binary name and matching it with 'vuln' list. for eg:- /usr/bin/nice in bin_name[-1] is nice.

                if bin_name[-1] in vuln:
                    print(colored('\n[R00T] Found {} .'.format(perm),'red'))
                    vulnerable += 1
                    exploitroot.append(bin_name[-1])
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

            if vulnerable >= 1 or suspicious >= 1:
                print(colored('\n[FOUND-R00T] There is/are ( {} ) Vulnerable Binary/ies.'.format(str(vulnerable)),'red'))
                print(colored('\n[FOUND-RWUD] There is/are ( {} ) Vulnerable Binary/ies.'.format(str(suspicious)),'magenta'))

            # What to do with output.

                print('\n\t[TIP] Type "help" to check !\n')
                print(colored('\n[Master] what next: ','cyan'),end='')
                response = input()
                if response == 'rootex':
                    print(colored('Executing...','red'))
                    time.sleep(1)
                    print(colored('Executed R00T exploit for {}'.format(exploitroot[0]),'red',attrs=['blink']))
                    print(colored('\nIn case no root shell then locate the binary exploit file in root-binaries folder and execute the command of that file manually on terminal.\n','white',attrs=['reverse']))
                    exploit(exploitroot[0])
                elif response == 'rwexp':
                    print(colored('Executing...','magenta'))
                    time.sleep(1)
                    print(colored('Executed R-W exploit for {}'.format()))
            elif vulnerable == 0:
                print(colored('[+] Nothing Suspicious Found.','blue'))
                print(colored('[+] Searched All Accessible Files/Folders.\n','blue'))
        
    except:
        print(colored('[-] OOps something went wrong !','red'))


# This function is just for r00t exploit.

def exploit(binary):
    if 'dash' in binary:
        subprocess.call('bash root-binaries/suid_ash.sh',shell=True)
    elif 'python2' in binary:
        subprocess.call('bash root-binaries/suid_python.sh',shell=True)
    elif 'python3' in binary:
        subprocess.call('bash root-binaries/suid_python3.sh',shell=True)
    elif 'systemctl' in binary:
        subprocess.call('bash root-binaries/suid_systemctl.sh',shell=True)
    elif 'hping3' in binary:
        subprocess.call('bash root-binaries/suid_hping3.sh',shell=True)
    elif 'bash' in binary:
        subprocess.call('bash root-binaries/suid_bash.sh',shell=True)
    elif 'capsh' in binary:
        subprocess.call('bash root-binaries/suid_capsh.sh',shell=True)
    elif 'chmod' in binary:
        subprocess.call('bash root-binaries/suid_chmod.sh',shell=True)
    elif 'chroot' in binary:
        subprocess.call('bash root-binaries/suid_chroot.sh',shell=True)
    elif 'chown' in binary:
        subprocess.call('bash root-binaries/suid_chown.sh',shell=True)
    elif 'cpulimit' in binary:
        subprocess.call('bash root-binaries/suid_cpulimit.sh',shell=True)
    elif 'bsd-csh' in binary:
        subprocess.call('bash root-binaries/suid_csh.sh',shell=True)
    elif 'dmsetup' in binary:
        subprocess.call('bash root-binaries/suid_dmsetup.sh',shell=True)
    elif 'docker' in binary:
        subprocess.call('bash root-binaries/suid_docker.sh',shell=True)
    elif 'emacs' in binary:
        subprocess.call('bash root-binaries/suid_emacs.sh',shell=True)
    elif 'env' in binary:
        subprocess.call('bash root-binaries/suid_env.sh',shell=True)
    elif 'expect' in binary:
        subprocess.call('bash root-binaries/suid_expect.sh',shell=True)
    elif 'find' in binary:
        subprocess.call('bash root-binaries/suid_find.sh',shell=True)
    elif 'flock' in binary:
        subprocess.call('bash root-binaries/suid_flock.sh',shell=True)
    elif 'gdb' in binary:
        subprocess.call('bash root-binaries/suid_gdb.sh',shell=True)
    elif 'gimp-' in binary:
        subprocess.call('bash root-binaries/suid_gimp.sh',shell=True)
    elif 'gtester' in binary:
        subprocess.call('bash root-binaries/suid_gtester.sh',shell=True)
    elif 'ionice' in binary:
        subprocess.call('bash root-binaries/suid_ionice.sh',shell=True)
    elif 'ip' in binary:
        subprocess.call('bash root-binaries/suid_ip.sh',shell=True)
    elif 'jjs' in binary:
        subprocess.call('bash root-binaries/suid_jjs.sh',shell=True)
    elif 'jrunscript' in binary:
        subprocess.call('bash root-binaries/suid_jrunscript.sh',shell=True)
    elif 'ksh' in binary:
        subprocess.call('bash root-binaries/suid_ksh.sh',shell=True)
    elif 'ld-2.30.so' in binary:
        subprocess.call('bash root-binaries/suid_ld-2.30.so.sh',shell=True)
    elif 'logsave' in binary:
        subprocess.call('bash root-binaries/suid_logsave.sh',shell=True)
    elif 'make' in binary:
        subprocess.call('bash root-binaries/suid_make.sh',shell=True)
    elif 'nice' in binary:
        subprocess.call('bash root-binaries/suid_nice.sh',shell=True)
    elif 'node' in binary:
        subprocess.call('bash root-binaries/suid_node.sh',shell=True)
    elif 'nohup' in binary:
        subprocess.call('bash root-binaries/suid_nohup.sh',shell=True)
    elif 'openvpn' in binary:
        subprocess.call('bash root-binaries/suid_openvpn.sh',shell=True)
    elif 'perl' in binary:
        subprocess.call('bash root-binaries/suid_perl.sh',shell=True)
    elif 'php7' in binary:
        subprocess.call('bash root-binaries/suid_php.sh',shell=True)
    elif 'rlwrap' in binary:
        subprocess.call('bash root-binaries/suid_rlwrap.sh',shell=True)
    elif 'rsync' in binary:
        subprocess.call('bash root-binaries/suid_rsync.sh',shell=True)
    elif 'run-parts' in binary:
        subprocess.call('bash root-binaries/suid_run-parts.sh',shell=True)
    elif 'rview' in binary:
        subprocess.call('bash root-binaries/suid_rview.sh',shell=True)
    elif 'vim.' in binary:
        subprocess.call('bash root-binaries/suid_rvim.sh',shell=True)
    elif 'setarch' in binary:
        subprocess.call('bash root-binaries/suid_setarch.sh',shell=True)
    elif 'start-stop-daemon' in binary:
        subprocess.call('bash root-binaries/suid_setarch.sh',shell=True)
    elif 'stdbuf' in binary:
        subprocess.call('bash root-binaries/suid_stdbuf.sh',shell=True)
    elif 'strace' in binary:
        subprocess.call('bash root-binaries/suid_strace.sh',shell=True)
    elif 'taskset' in binary:
        subprocess.call('bash root-binaries/suid_taskset.sh',shell=True)
    elif 'tclsh8' in binary:
        subprocess.call('bash root-binaries/suid_tclsh.sh',shell=True)
    elif 'time' in binary:
        subprocess.call('bash root-binaries/suid_time.sh',shell=True)
    elif 'timeout' in binary:
        subprocess.call('bash root-binaries/suid_timeout.sh',shell=True)
    elif 'unshare' in binary:
        subprocess.call('bash root-binaries/suid_unshare.sh',shell=True)
    elif 'xargs' in binary:
        subprocess.call('bash root-binaries/suid_xargs.sh',shell=True)
    elif 'zsh' in binary:
        subprocess.call('bash root-binaries/suid_zsh.sh',shell=True)
    else:
        print(colored('[!] No Exploit file found for {}. Check root-binaries folder.'.format(binary),'red'))
        pass

def main():
    
    # Calling All Functions

    banner()
    time.sleep(2)
    perm_checker()
    
main()
