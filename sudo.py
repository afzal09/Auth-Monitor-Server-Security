from datetime import datetime
from mail.sendMail import sendMail


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