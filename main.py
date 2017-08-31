from send_mail import EmailFunctions
import argparse

'''
Enter your credentials below

'''

EmailFunctions.sender="Your Email id"
EmailFunctions.password="Your Password"


'''Dont Edit this code!!! '''
parser = argparse.ArgumentParser()
parser.add_argument('count', help='Enter Count',type=int)
parser.add_argument('To', help='Enter To Address',type=str)
args = parser.parse_args()
TOO = args.To
count = args.count
obj = EmailFunctions()
obj.send_emails(count=count,receiver=TOO)
