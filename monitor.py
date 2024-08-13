""" A monitoring system that monitors sudoers for a system
"""

import tailer
from datetime import datetime
from sudo import sudo
from ssh import ssh



log_file = '/var/log/auth.log'
sys_admin = None
def main():
        print("Please provide the admin email address. Note emails will be sent to this email")
        sys_admin = str(input())
        for log in tailer.follow(open(log_file)):
            if "sudo" in str(log):
                text = log.split(";",1)[0]
                sudo(sys_admin,text)
            else:
                ssh(sys_admin,log)

if __name__ == "__main__":
    main()