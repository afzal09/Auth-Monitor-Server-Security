from datetime import datetime
from mail.sendMail import sendMail


def ssh(sender,log):
    fields = log.split()
    if len(fields) < 5:
        return
    month, date, time_str, host = fields[:4]
    time_obj = datetime.strptime(time_str, "%H:%M:%S")
    time_formatted = time_obj.strftime("%I:%M:%S %p")

    if "Accepted publickey user logged in" in log:
        user = fields[8]
        ip_address = fields[-4]
        print(
            f"Accepted publickey:\nMonth: {month}\nDate: {date}\nTime: {time_formatted}\nHost: {host}\nUser: {user}\nIP Address: {ip_address}\n"
        )
        sendMail(sender,str(f"Accepted publickey user logged in: {user} into remote host: {host} from: {ip_address} on {month} {date} {time_formatted}"))

    elif "Failed password" in log:
        user = fields[8]
        ip_address = fields[-4]
        print(
            f"Authentication Failure:\nMonth: {month}\nDate: {date}\nTime: {time_formatted}\nHost: {host}\nUser: {user}\nIP Address: {ip_address}\n"
        )
        sendMail(sender,str(f"Authentication Failure for: {user} into remote host: {host} from: {ip_address} on {month} {date} {time_formatted}"))