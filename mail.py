import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import time
import streamlit as st

# setup details
sender_email = "Spassfabrik@hotmail.com"
#receiver_email = "xxx"
password = st.secrets["SIB_SMTP_PW"]

# Create secure connection with server and send email
smtp_server = "smtp-relay.sendinblue.com"
smtp_port = 587


def send_conf_mail(receiver_email: str):
    #context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, smtp_port) as server: # old: SMTP_SSL // context=context
        server.login(sender_email, password)

    
        message = MIMEMultipart("alternative")
        message["Subject"] = "LETFs Abenteuer | 200SMA-Reminder"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text (and HTML version) of your message
        text = f"""
        Du hast dich erfolgreich zum 200SMA-Reminder des SPY eingetragen.
        Bitte beachte, dass die E-Mails im Spam Ordner landen können. 
        Triff hier eigene Vorkehrung in deinem E-Mail Client, um keinen Reminder zu verpassen.
        Zum Beispiel kann der Absender als Kontakt hinzugefügt werden.

        Keine Interesse mehr?
        Aktuell ist nur möglich via Reddit PM an u/Spassfabrik sich aus dem Newsletter austragen zu lassen.

        Gruß 
        Spassfabrik & Finanzflunder - in Liebe zu ZahlGraf
                """

        part1 = MIMEText(text, "plain")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)

        # send mail
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Mail was sent!")
