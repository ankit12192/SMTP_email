from send_mail import email_functions


'''
Use this file to configure how the script should run

'''

email_functions.sender="Your email"
email_functions.password="your password"
TO = "Receiver Id here"

"""Total number of emails you want to send """
count = 2



obj = email_functions()
obj.send_emails(count,TO)



