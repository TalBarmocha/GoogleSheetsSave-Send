import os
import gspread
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

x = datetime.now()
date = x.strftime('%d-%m-%Y')

jasonFilePath = " " #created from the cloud program using google drive api
sheetKey=" " # extracted from the url
path = '~/Users/Downloads/' #the path to witch the file will be saved (dont forget to add the '/' at the end of the path)
filename = f"{date}.xlsx"
filepath = path+filename
email_from = "yourmail@gmail.com"
email_target = "targetmail@example.com"
pswd = " " # get this from the google account password

####Create the File ####
gc = gspread.service_account(filename=jasonFilePath)
sh = gc.open_by_key(sheetKey)
export_file = sh.export(format='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
with open(filepath, 'wb') as f:
    f.write(export_file)
print(f"The file:{filename} has created at {path}")

####Sending the File via Gmail####

subject = "subject"
body = " "
msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = email_target
msg['Subject'] = subject
msg.attach(MIMEText(body))
attachment= open(filepath, 'rb')
# Encode as base 64
attachment_package = MIMEBase('application', 'octet-stream')
attachment_package.set_payload((attachment).read())
encoders.encode_base64(attachment_package)
attachment_package.add_header('Content-Disposition', f"attachment; filename= " + filename)
msg.attach(attachment_package)
text = msg.as_string()
print("Connectig to servers....")
TIE_server = smtplib.SMTP("smtp.gmail.com", 587)
TIE_server.starttls()
TIE_server.login(email_from, pswd)
TIE_server.sendmail(email_from, email_target, text)
print(f"The email sent to {email_target}")
TIE_server.quit()


#####Deleteing the file######


print("Deleting the file")
os.remove(filepath)
print("File deleted")
