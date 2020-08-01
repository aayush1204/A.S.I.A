# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import pandas as pd
import threading
# The necessary changes to be done in this file -
# initialize fromaddr with your email address and write the password of that account on line 27 in the parameters of the function
# Similarly Initialize the Body , Subject, the file to be attached in your mail (eg.resume) and its path.

class EmailThread(threading.Thread):
    def __init__(self,fromaddr, toaddr, text):
        threading.Thread.__init__(self)
        self.msg = text
        self.fromaddr = fromaddr
        self.toaddr = toaddr
        
    
    def run(self):
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.fromaddr, "Your_Password")
        server.sendmail(self.fromaddr,self.toaddr,self.msg)
        print(self.toaddr)
        server.quit() 
        
# This is your email address. The email id from which the mail will be sent      
fromaddr = "halgekaraayush@gmail.com"

msg = MIMEMultipart() 
# storing the senders email address   
msg['From'] = fromaddr 


# storing the subject 
msg['Subject'] = "Summer Engineering Internship Application"

# string to store the body of the mail  
body = "Dear Sir, \n \n I am Aayush Halgekar, a student at Dwarkadas J Sanghvi College of Engineering pursuing Bachelors in Computer Science Degree. I wanted to reach out to u to discuss the possibility of completing an internship with your company this summer. I know you are busy, but i would love to talk to you about the opprtunities that might be available at you organization. I have attached my resume in this email. Please do have a look. \n\n Thank you for your time in advance."

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 

# open the file to be sent 
# write the name of the file with extension here
filename = "resume.pdf"
# write the full path of that file here
attachment = open(r"C:\Users\aayus\OneDrive\Desktop\college\resume.pdf", "rb") 

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
p.set_payload((attachment).read()) 

# encode into base64 
encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# attach the instance 'p' to instance 'msg' 
msg.attach(p) 

df = pd.read_csv('emails.csv')
email_list = df['Email']

for emails in email_list:
    
    emails = emails[1:-1].split(',')
    
    for email in emails:
        toaddr = email[1:-1]

        msg['To'] = toaddr 
        
        EmailThread(fromaddr, toaddr, msg.as_string()).start()
        

