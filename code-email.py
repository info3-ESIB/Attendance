import smtplib

server=smtplib.SMTP_SSL('smtp.gmail.com',465)
sender_mail=input("please enter you mail here")
password=input("please enter your password here")

receiver_mail=input("Enter the mail of the person you are sending that mail to")
message=input("your message here")

server.login(sender_mail,password)
server.sendmail(sender_mail,receiver_mail,message)

server.quit()