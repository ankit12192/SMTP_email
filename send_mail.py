# -*- coding: utf-8 -*-
# Author Ankit tiwari

"""

This code will perform email operations

send_email() will send multiple emails to a user

create_folder() will create folder in your gmail account

Note : Please do not edit any methods or class unless you need to make code changes
"""


import smtplib
import imaplib
import time
import random


class email_functions:

    ''' Class variables'''
    host = "imap.gmail.com"
    sender = ''
    password = ''
    file = open("message.txt", "r")
    msg = file.read()
    string_message = str(msg)
    folder_name =''

    def __init__(self):
        '''constructor which performs login
        when the object is created '''

        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.sender, self.password)
        print "Performing login"


    def get_random_number(self):
        '''Return a random number with current TS'''

        sub = random.randint(1,100000)+time.time()
        return sub


    def send_emails(self,count,receiver):

        """Takes 2 arguments
            count : total number emails that needs to be sent
            Receiver : whom you want to send the email
        """
        start_time = time.time()
        try:
            for i in range(0, count):
                Number = str(self.get_random_number())
                Subject = "Test Automation"+Number
                message = """From: """ +self.sender+""" \nTo: """+receiver+""" \nSubject: """+Subject+"""\n\n """+self.string_message+""""""
                self.server.sendmail(self.sender, str(receiver),message)
                print "Successfully sent "+str(i+1)+" message"
            total_time = time.time() - start_time
            print "Total time taken "+str(total_time)


        except:
            print "Error: unable to send email"
        finally:
            self.server.quit()

    def create_folders(self):
        '''Creates a single folder with a name'''
        mail = imaplib.IMAP4_SSL(self.host)
        mail.login(self.sender, self.password)
        mail.create(self.folder_name)