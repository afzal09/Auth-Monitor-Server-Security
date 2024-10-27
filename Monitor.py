""" A monitoring system that monitors Real-time sudo events and SSH Logins events for a Server
"""

import tailer
from datetime import datetime
from mail.sendMail import sendMail


class Monitor():
    def __init__(self,log_file,mail):
         self.log_file = log_file
         self.email = mail
         self.watch_email = tailer.head(open(mail),1)

    def sudo(self,data:str)-> None:
        """ Method for monitoring sudo events takes log file input data and parse it  
        """
        text = data.split()
        month = text[0]
        date = text[1]
        time_obj = datetime.strptime(text[2],"%H:%M:%S") #Takes UTC time object and converts it to IST
        time = time_obj.strftime("%I:%M:%S %p") #Format the Time object
        host = text[3]
        command = text[4].split(":")[0]
        if command.startswith("sudo"):
            if text[-1] == "failure":
                auth_failure = " ".join(text[-2:])
                print(f"Authentication Failure\n month:{month}\n date:{date}\n time:{time}\n host:{host}\n command:{command}\n reason:{auth_failure}\n")
            elif " ".join(text[-4:]) == "3 incorrect password attempts":
                incorrect_attempts = " ".join(text[-4:])
                print(f"Authentication Failure \nmonth:{month}\n date:{date}\n time:{time}\n host:{host}\n command:{command}\n resaon:{incorrect_attempts}\n")

    def ssh(self,sender:str,log:str) -> None:
        """Method for monitoring SSH events takes sender email sends it to desired recipient using Sendgrid mail api through sendMAil and log file input data and parse it
        """
        fields = log.split()
        if len(fields) < 5:
            return
        month, date, time_str, host = fields[:4]
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        time_formatted = time_obj.strftime("%I:%M:%S %p")
        if "Accepted password" in log:
            user = fields[8]
            ip_address = fields[-4]
            msg = 'Authentication success'
            print(
                f"{msg}:\nMonth: {month}\nDate: {date}\nTime: {time_formatted}\nHost: {host}\nUser: {user}\nIP Address: {ip_address}\n"
            )
            sendMail.mail(sender,user, host, ip_address)
        elif "Failed password" in log:
            user = fields[8]
            ip_address = fields[-4]
            msg = 'Authentication Failure'
            print(
                f"{msg}:\nMonth: {month}\nDate: {date}\nTime: {time_formatted}\nHost: {host}\nUser: {user}\nIP Address: {ip_address}\n"
            )

    def main(self):    
        """Main function where program executes
        """        
        if not self.watch_email:
            print("Please provide the admin email address. Note emails will be sent to this email")
            mail = str(input())
            print(f'auth emails will be sent to {mail}')
            print('program continuing ...\n')
            with open(self.email, 'w') as file:
                    file.write('')
            with open(self.email, 'a') as file:
                file.write(mail + '\n')
        else:
            print(f"Do you want to continue with previous email {self.watch_email[0]}")
            print("Type yes to Continue or no to edit...")
            res = str(input()).lower()
            if 'yes' in res:
                mail = self.watch_email[0]
                print(f'auth emails will be sent to {mail}')
                print('program continuing ...\n')
            elif 'no' in res:
                print("Please provide the admin email address. Note emails will be sent to this email")
                mail = str(input())
                print(f'auth emails will be sent to {mail}')
                print('program continuing ...\n')
                with open(self.email, 'w') as file:
                        file.write('')
                with open(self.email, 'a') as file:
                    file.write(mail + '\n')
            else:
                raise AttributeError("inavlid input ")
        for log in tailer.follow(open(self.log_file)):
            if "sudo" in str(log):
                text = log.split(";",1)[0]
                self.sudo(text)
            else:
                self.ssh(mail,log)

# Test
if __name__ == '__main__':
    monitor = Monitor('/var/log/auth.log','email.txt')
    monitor.main()