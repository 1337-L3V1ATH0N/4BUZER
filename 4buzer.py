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


###### Normal Binaries which are always running and not Mis-Configured to current version. You can add your system normal binaries here.

normal = ['exim4','mount.nfs','pppd','mount.cifs','pkexec',
        'bwrap','chsh','passwd','kismet_cap_linux_bluetooth',
        'kismet_cap_ti_cc_2540','kismet_cap_ti_cc_2531','kismet_cap_nrf_51822','kismet_cap_nxp_kw41z','fusermount3',
        'chfn','gpasswd','mount','newgrp','sudo','su','ntfs-3g',
        'kismet_cap_linux_wifi','kismet_cap_nrf_mousejack','umount','ssh-keysign','Xorg.wrap']

###### Vulnerable Binaries which are Vulnerable and Suspicious. You can add new Vulnerable Binaries here.

ld_2 = '' # Searching for ld-2 binaries in lib folder the version may vary on different system. This logic works for every system ld-2 binary.
for ld in os.listdir('/lib/x86_64-linux-gnu/'):
    if 'ld-2.3' in ld:
        ld_2 = ld

vuln = ['ash','bash','capsh','chmod','chroot',
        'chown','cpulimit','bsd-csh','dash','dmsetup',
        'docker','emacs-gtk','env','expect','find',
        'flock','gdb','gimp-2.10','gtester','hping3',
        'ionice','ip','jjs','jrunscript','ksh93',
        ld_2,'logsave','make','nice','node',
        'nohup','openvpn','perl','php7.4','python',
        'rlwrap','rsync','run-parts','rview','vim.gtk3','setarch','start-stop-daemon',
        'stdbuf','strace','systemctl','taskset','tclsh8.6','time',
        'timeout','unshare','view','xargs','zsh','busybox','python2.7','python3.7','python3.8','python3.9']

###### Locations for searching Mis-Configured Binaries. If You are 'root' and want to search SUID binaries in system then you can add more / folders here. 

locations = ['/bin','/dev','/lib/x86_64-linux-gnu/','/lib64',
        '/libx32','/mnt','/opt','/sbin','/usr/bin','/usr/sbin']

###### This Binaries are set to be SUID BIT and Mis-Configured to 'read/write/download/upload' .

rwud_vuln = ['ar','arp','atobm','awk','gawk','base32','base64','basenc','busybox','bridge','cat',
        'column','comm','cp','cpio','ksshell','less','look','lua','lwp-download','csplit',
        'cupsfilter','curl','cut','date','dd','dialog','diff','dig','docker','ed',
        'eqn','expand','file','fmt','fold','grep','gzip','hd','head','hexdump','highlight','iconv',
        'ip','join','jq','mawk','more','nawk','nl','nmap','od','openssl','paste','pg','pr','readelf',
        'restic','rev','sed','shuf','soelim','sort','sqlite3','ss','ssh-keyscan','ssh-keygen',
        'strings','sysctl','tac','tail','tbl','tee','tftp','troff','ul','unexpand','uniq',
        'update-alternatives','uudecode','uuencode','vim','vimdiff','rvim','rview','vpiw','vigr','wget','xmodmap','xxd','xz','zsoelim']

def help():

    print(colored('\nrootex\t - -4buzes the SUID binary which provides R00T Shell .','red',attrs=['reverse']))
    print(colored('rwexp\t - -4buZes the SUID binary which provides to read/write files.','magenta'))
    print('help\t - Prints this message.')
    print(colored('exit\t - Exits the program after scanning.','cyan'))
    print(colored('save\t - Saves the output in current directory.','green'))
    print(colored('clear\t -Clears the screen softly. You can scroll up to see output.','blue'))
    print(colored('author\t -Prints the author name.','white'))
    print(colored('lifesaver-Prints the name of a site which helped to save my life :)','red'))
    print(colored('chbin\t -Changes the file permission (Only if you have permission or escalated to r00t ;)','yellow'))
    
def banner():
	try:
            subprocess.call('./banner.py',shell=True)
            print(colored('\n\t\t\t\t[R00T]    = -4buZer will provide root shell.','red'))
            print(colored('\t\t\t\t[R-W-U-D] = -4buZer will give privileges to Read, Write, Upload, Download.','magenta'))
            print(colored('\t\t\t\t[Exploit] = -4buZer is available for binary.','yellow'))
            print(colored('\t\t\t\t[Normal]  = Binaries are normal not 4buZing.','green'))
            time.sleep(5)
            print()
	except FileNotFoundError:
		print(colored("[!] The Banner for 4buzer can't be found ! :( ",'red'))
		exit(1)

def perm_checker():
    
    date = time.ctime(time.time())
    host = os.uname()[1]
    vulnerable = 0
    suspicious = 0
    exploitroot = []
    root_save = []
    rwud_save = []

    for locate in locations:
            
            # Searching for SUID BITS inside all files and  folders.
        find_bin = "find "+locate+" -perm -4000 2>/dev/null"

        print(colored('[+] Searching in {}'.format(locate),'white'))
        permis = subprocess.check_output(find_bin,shell=True,text=True).split('\n')
        print('[+] Searched {}'.format(locate))      
         # For bin_name data to pass to function exploit.
        for perm in permis:

            bin_name = perm.split('/')

                # Taking the binary name and matching it with 'vuln' list. for eg:- /usr/bin/nice in bin_name[-1] is nice.

            if bin_name[-1] in vuln or 'python3' in vuln:
                root_save.append(perm)
                print(colored('\n[R00T] Found {} .'.format(perm),'red'))
                vulnerable += 1
                exploitroot.append(bin_name[-1])
                print(colored('[Hack] is available for {} .\n'.format(perm),'yellow',attrs=['reverse']))
                continue
                                    
                # Taking the binary name and matching it with 'normal' list. for eg:- /usr/bin/exim4 in bin_name[-1] is exim4.
                
            elif bin_name[-1] in normal:
                print(colored('[Normal] binary {}'.format(perm),'green'))
                
                # Taking the binary name and matching it with 'rwud_vuln' list. rwud is read/write/upload/download. Some SUID don't spawn root shell but are -4buzing to Read, Write, Upload, and Download.

            elif bin_name[-1] in rwud_vuln:
                rwud_save.append(perm)
                print(colored('\n[R-W-U-D] Found {}'.format(perm),'magenta'))
                suspicious += 1
                print(colored('[Hack] is available for {}\n'.format(perm),'yellow'))

    if vulnerable >= 1 or suspicious >= 1:
        print(colored('\n[FOUND-R00T] There is/are ( {} ) Mis-Configured Binary/ies.'.format(str(vulnerable)),'red'))
        print(colored('\n[FOUND-RWUD] There is/are ( {} ) Mis-Configured Binary/ies.'.format(str(suspicious)),'magenta'))

            # What to do with output.
        print('\n[TIP] Type "help" to check!')
        while True:
            print(colored('\n{}💀-4buZer > '.format(host),'red'),end='')
            response = input()
        
            if response == 'rootex':
                print(colored('Executing...','red'))
                time.sleep(1)
                print(colored('Executed R00T -4buZer for {}'.format(exploitroot[0]),'red',attrs=['blink']))
                print(colored('\nIn case no root shell then locate the binary exploit file in root-binaries folder and execute the command of that file manually on terminal.\n','white',attrs=['reverse']))
                exploit(exploitroot[0])
        
            elif response == 'rwexp':
                print(colored('Executing...','magenta'))
                time.sleep(1)
                print(colored('Executed R-W -4buZer for {}'.format())) ##### Add rwexp exploit below.

            elif response == 'help':
                help()
        
            elif response == 'exit':
                print(colored('\nExited Successfully... !','red'))
                exit(0)
        
            elif response == 'save':
                print(colored('\n[+] [FILE_NAME]@-4buZer > ','red'),end='')
                file_name = input()
                print(colored('Please Wait Saving',attrs=['blink']))
                time.sleep(2)
                for saved in root_save:     # Saving file path which is vulnerable to R00T shell in a file for later auditing.
                    with open(file_name,'a') as data:
                        data.write('Scanned On: ')
                        data.write(str(date))
                        data.write('\n[R00T Shell] --> ')
                        data.write(saved)
                for ruwd in rwud_save:      # Saving file path which is vulnerable to Read-Write-Upload-Download in a file.
                    with open(file_name,'a') as data:
                        data.write('\nScanned On: ')
                        data.write(str(date))
                        data.write('\n[Read-Write-Upload-Download] --> ')
                        data.write(ruwd)
                print(colored('\nDone with Saving data.','yellow'))

            elif response == 'lifesaver':
                print(colored('\nhttps://gtfobins.github.io/','cyan'))

            elif response == 'clear':
                os.system('clear -x')
                #Incase if you don't want banner after clearing screen you can comment this below line.
                os.system('./banner.py')

            elif response == 'Author' or response == 'author':
                print(colored('\nAuthor\t: Akash Pandey a.k.a L3V1ATH0N\n','white'))
                print(colored('HelpingHands : https://gtfobins.github.io/','white'))
            
            elif response == 'chbin':
                try:
                    print('\nThis command will only change the permission for SUID BIT and only if you are root.')
                    print(colored('\n[#] [File Perm]@-4buZer > ','yellow'),end=' ')
                    chbins = input(' File Path for permission change :- ')
                    subprocess.call('chmod -s '+chbins,shell=True)                
                except:
                    print(colored('\n[ERROR]','red',attrs=['blink']))
                    continue
            else:
                os.system('clear -x')
                help()

    elif vulnerable == 0:
        print(colored('[+] Nothing Suspicious Found.','blue'))
        print(colored('[+] Searched All Accessible Files/Folders.\n','blue'))
        
    #except:
        #print(colored('[-] OOps something went wrong !','red'))


# This function is just for r00t sh3ll.

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
    elif 'ld-2.' in binary:     
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
