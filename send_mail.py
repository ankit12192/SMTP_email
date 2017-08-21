import smtplib
import imaplib
from email.mime.text import MIMEText as text
import time

class email_functions:

# Declaring class variables
    host = "imap.gmail.com"
    sender = ''
    password = ''
    reciver = ''
    body = ""
    m = text(body)
    m['Subject'] = 'Hello!'
    m['From'] = sender
    m['To'] = reciver


    def __init__(self):
        '''Constructure which performs login when the object is created '''

        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.sender, self.password)
        print "Performing login"



    def send_emails(self,count):
        """Takes 2 arguments
            count : total number emails that needs to be sent
            reciver : whom you want to send the email
        """

        start_time = time.time()
        try:
            for i in range(0, count):
                self.server.sendmail(self.sender, self.reciver,self.m.as_string())

                print "Successfully sent "+str(i+1)+" message"
            total_time = time.time() - start_time
            print "Total time taken "+str(total_time)
        except:
            print "Error: unable to send email"



    def create_folders(self):
        mail = imaplib.IMAP4_SSL(self.host)
        mail.login(self.sender, self.password)
        mail.create("BusinessEmails")



obj = email_functions()
obj.send_emails(10)

