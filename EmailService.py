import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class EmailService:
    def sendEmailWithImage(subject, body, to, imagePath):
        user = "petrol.coding@gmail.com"
        password = "wtxizcciqtfvfitu"

        with open(imagePath, 'rb') as f:
            imgData = f.read() 

        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = user
        message['To'] = to

        text = MIMEText(body)
        message.attach(text)

        image = MIMEImage(imgData, name=os.path.basename(imagePath))
        message.attach(image)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, to, message.as_string())

        server.quit()