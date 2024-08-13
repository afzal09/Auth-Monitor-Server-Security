A system monitoring script
what this script will do
acces the log file and reports all the system logged into system
how to do this first acces the log file and analyze the log file its struture and then parse the log file into order 
then format the output

Date : Friday 09 August 

---
Notes
 
- [X] acces the /var/log/auth.log file
- [X] get last line of file
- [X] access data time elements
- [X]  sort the dat to get the service type for ssh and sudo 
- [X]  make function for ssh and sudo that will trigger actions when occured

---
Packages

- [X] Tailer
- [X] Datetime

example sudo log
Aug 11 21:54:49 Atherius sudo: pam_unix(sudo:auth): authentication failure; logname= uid=1000 euid=0 tty=/dev/pts/4 ruser=afzal rhost=  user=afzal
Aug 11 21:54:58 Atherius sudo:    afzal : 3 incorrect password attempts ; TTY=pts/4 ; PWD=/home/afzal/Desktop/project ; USER=root ; COMMAND=/bin/bash
Aug 11 21:56:11 Atherius sudo:    afzal : TTY=pts/4 ; PWD=/home/afzal/Desktop/project ; USER=root ; COMMAND=/usr/local/bin/apt update
Aug 11 12:02:29 Atherius sudo:    afzal : TTY=pts/2 ; PWD=/home/afzal/Desktop ; USER=root ; COMMAND=/usr/bin/rsync -id ubuntu-server/ afzal@192.168.122.2:



example results
['Aug', '12', '23:26:22', 'Atherius', 'sudo:', 'afzal', ':', 'TTY=pts/3']
month:Aug
 date:12
 time:11:26:22
 host:Atherius
 command:sudo
 what_happened:sudo: afzal : TTY=pts/3

['Aug', '12', '23:27:42', 'Atherius', 'sudo:', 'pam_unix(sudo:auth):', 'authentication', 'failure']
month:Aug
 date:12
 time:11:27:42
 host:Atherius
 command:sudo
 what_happened:authentication failure

['Aug', '12', '23:27:56', 'Atherius', 'sudo:', 'afzal', ':', '3', 'incorrect', 'password', 'attempts']
month:Aug
 date:12
 time:11:27:56
 host:Atherius
 command:sudo
 what_happened:3 incorrect password attempts



example ssh log
Aug 12 23:44:36 testserver sshd[933]: Server listening on :: port 22.
Aug 12 23:44:36 testserver sshd[935]: Accepted publickey for afzal from 192.168.122.1 port 53412 ssh2: RSA SHA256:gzoFPbMvLGXH+cKjdJ1eXh9PnyZ2FTvWkgJyjptzudw
Aug 12 23:44:36 testserver sshd[935]: pam_unix(sshd:session): session opened for user afzal(uid=1000) by afzal(uid=0)

Aug 12 23:48:00 testserver sshd[1111]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.122.1  user=afzal
Aug 12 23:48:02 testserver sshd[1111]: Failed password for afzal from 192.168.122.1 port 32893 ssh2