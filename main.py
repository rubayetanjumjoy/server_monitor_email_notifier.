import time
import requests
import smtplib
import os
from email.mime.text import MIMEText
from fastapi import FastAPI
app = FastAPI()
email_host = "smtp.gmail.com"  # Your SMTP server
email_port = 587  # SMTP port (587 for TLS, 465 for SSL)
email_sender = "acibd785@gmail.com"  # Your email address
email_password = "kiruogcbjbwdvoqi"  # Your email password
email_recipient = ["rubayetanjumjoy@gmail.com","vladimirmakarov1616@gmail.com"]  # Recipient's email address
def send_email(subject, message):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = email_sender

    try:
        server = smtplib.SMTP(email_host, email_port)
        server.starttls()
        server.login(email_sender, email_password)

        for recipient in email_recipient:
            msg["To"] = recipient  # Set "To" for each recipient
            server.sendmail(email_sender, recipient, msg.as_string())  # Send email to each recipient

        server.quit()
        print("Email notification sent successfully.")
    except Exception as e:
        print(f"Failed to send email notification: {str(e)}")
   
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
while True:
    try:
        response = requests.get("http://maps.codemaven.net")  # Adjust URL as needed
       

        response2=requests.get('http://maps.codemaven.net/geocode/reverse/details/?lat=23.5508717&lng=90.53532709999999', headers = {'x-api-key': '9a786703565fd4c88ed8d989cc718107f5f56f6e'})
        print(response2.status_code)
        if response.status_code or response2.status_code == 200:
            print("Server is not responding. Sending email notification.")
            send_email("Server Down Notification", "Your server is not responding.")
    except Exception as e:
        print(f"Error checking server status: {str(e)}")

    time.sleep(600)  # Check every 10 minutes 


