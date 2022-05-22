import ssl, smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formatdate
from email import encoders


port = 465

from_addr = "infotrois2022@gmail.com" 
password =  "Info32022"
to_addr = input("Enter the receiver's email address : ") 
subject = input("What is the subject of the email: ")
content = input("Type your email here: ")
FileName=input("Type your file here. Make sure to have the file in the same directory as this code and do not forget the extension:  ")
print("If the email does not appear in your inbox, please check your junk/spam")

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
msg['Date'] = formatdate(localtime = True)
body = MIMEText(content, 'plain')
msg.attach(body)

part = MIMEBase('application', "octet-stream")
part.set_payload(open(FileName, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename={FileName}')
msg.attach(part)

context = ssl.create_default_context()
with smtplib.SMTP_SSL ("smtp.gmail.com", port,context=context) as server:
    server.login(from_addr,password)
    server.send_message(msg,from_addr, to_addr)

