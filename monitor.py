""" A monitoring system that monitors sudoers for a system
"""

import tailer
from datetime import datetime
import smtplib

log_file = '/var/log/auth.log'

def sudo(data):
    text = data.split()
    month = text[0]
    date = text[1]
    time_obj = datetime.strptime(text[2],"%H:%M:%S")
    time = time_obj.strftime("%I:%M:%S %p")
    host = text[3]
    command = text[4].split(":")[0]
    if command.startswith("sudo"):
        if text[-1] == "failure":
            auth_failure = " ".join(text[-2:])
            print(f"month:{month}\n date:{date}\n time:{time}\n host:{host}\n command:{command}\n what_happened:{auth_failure}\n")
        elif " ".join(text[-4:]) == "3 incorrect password attempts":
            incorrect_attempts = " ".join(text[-4:])
            print(f"month:{month}\n date:{date}\n time:{time}\n host:{host}\n command:{command}\n what_happened:{incorrect_attempts}\n")

def ssh(log):
    fields = log.split()
    if len(fields) < 5:
        return
    month, date, time_str, host = fields[:4]
    time_obj = datetime.strptime(time_str, "%H:%M:%S")
    time_formatted = time_obj.strftime("%I:%M:%S %p")

    if "Accepted password" in log:
        user = fields[8]
        ip_address = fields[-4]
        print(
            f"Accepted publickey user loggedin:\nMonth: {month}\nDate: {date}\nTime: {time_formatted}\nHost: {host}\nUser: {user}\nIP Address: {ip_address}\n"
        )

    elif "Failed password" in log:
        user = fields[8]
        ip_address = fields[-4]
        print(
            f"Authentication Failure:\nMonth: {month}\nDate: {date}\nTime: {time_formatted}\nHost: {host}\nUser: {user}\nIP Address: {ip_address}\n"
        )


def main():
        for log in tailer.follow(open(log_file)):
            if "sudo" in str(log):
                text = log.split(";",1)[0]
                sudo(text)
            else:
                ssh(log)






if __name__ == "__main__":
    main()
