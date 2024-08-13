import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv,dotenv_values


def sendMail(reciver,msg):
    load_dotenv()
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("remote.ubuntu.server@gmail.com")  # Change to your verified sender
    to_email = To(reciver)  # Change to your recipient
    subject = "Server Security Notification"
    content = Content("text/plain", msg)
    mail = Mail(from_email, to_email, subject, content)

        # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

        # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
        
    print(response.status_code)
    print(response.headers)
