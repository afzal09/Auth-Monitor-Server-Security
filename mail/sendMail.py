"""A Mail class that is responsible to send mail to desired user using sendgrid api
"""

import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv


class sendMail():
  def mail(sender, user, host, ip_address):
      """Formats and logs the user login information in the specified format."""
      #load env variables
      load_dotenv()

      # email structure
      html_content = f'''
  <!doctype html>
  <html>
  <head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1">
    <script async src="https://cdn.ampproject.org/v0.js"></script>
    <style>
      body {{
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f5f5f5;
      }}
      .container {{
        max-width: 600px;
        margin: 0 auto;
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      }}
      .card {{
      background-color: #fcfcfc;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      padding: 20px;
    }}
      .header {{
        text-align: center;
        padding-bottom: 20px;
      }}
      .header img {{
        max-width: 100px;
      }}
      .content {{
        disply:flex;
        justify-content:center;
        font-size: 16px;
        line-height: 1.5;
        color: #333333;
      }}
      .footer {{
        text-align: center;
        font-size: 14px;
        color: #888888;
        padding-top: 20px;
        border-top: 1px solid #dddddd;
      }}
    </style>
  </head>
  <body>
    <div class="container">
    <div class="card">
      <div class="header">
        <img src="https://lh3.googleusercontent.com/d/1ScGR73IseiuqtFpruj1FyPweJ2ZReYlt"></img>
      </div>
      <div class="content">
        <h2>A new SSH login to {host} server</h2>
        <p>Auth-Monitor Notification System</p>
        <p>A new sign-in to your server {host} for User {user} from {ip_address} was detected. If this was you, you don’t need to do anything.</p>
        <p>If you did not initiate this action or if anything seems suspicious, please immediately contact your System Administrator. Do not proceed until your identity and the request have been verified.</p>
      </div>
      <div class="footer">
        <p>You received this email to let you know about important changes to your {host} and services.</p>
        <p>This is a system generated email do not reply to this email.</p>
        <p>© Auth-Monitor Notification System generated notification, India</p>
      </div>
    </div>
    </div>
  </body>
  </html>
      '''

      #email message
      from_email = Email('remote.ubuntu.server@gmail.com')
      to_email = To(sender)
      subject = "Server Security Notification"
      content = Content("text/html",html_content)
      mail = Mail(from_email, to_email, subject, content)

      # Send the email
      try:
          sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
          mail_json = mail.get()
          response = sg.client.mail.send.post(request_body=mail_json)
          print(f"mail sent to {sender} with code {response.status_code} - success\n")
      except Exception as e:
          print("Some error occured mail not sent",e)

# Test Mail
if __name__ == '__main__':
    sendMail.mail("afzalmomin2003@gmail.com","afzal","ubuntu","127.0.0.1")
