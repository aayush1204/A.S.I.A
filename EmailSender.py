# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import pandas as pd

df = pd.read_csv('emails.csv')
email_list = df['Email']

for emails in email_list:
    
    emails = emails[1:-1].split(',')

    for email in emails:

        fromaddr = "halgekaraayush@gmail.com"
        toaddr = email[1:-1]
        print(toaddr)
        # instance of MIMEMultipart 
        msg = MIMEMultipart() 
        # storing the senders email address   
        msg['From'] = fromaddr 
        
        # storing the receivers email address  
        msg['To'] = toaddr 

        # storing the subject 
        msg['Subject'] = "Application for internship"

        # string to store the body of the mail 
        body = "Test run 1"

        # attach the body with the msg instance 
        msg.attach(MIMEText(body, 'plain')) 

        # open the file to be sent 
        filename = "resume.pdf"
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

        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 

        # start TLS for security 
        s.starttls() 

        # Authentication 
        s.login(fromaddr, "Aayush@12") 

        # Converts the Multipart msg into a string 
        text = msg.as_string() 

        # sending the mail 
        s.sendmail(fromaddr, toaddr, text) 

        # terminating the session 
        s.quit() 
