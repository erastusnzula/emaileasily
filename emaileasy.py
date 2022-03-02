import datetime
import os
import smtplib
import socket
from email.message import EmailMessage
from tkinter.filedialog import askopenfilenames

message = EmailMessage()
filenames = []


def email_to(*args):
    recipients = []
    for recipient in args:
        recipients.append(recipient)
    message['To'] = recipients
    return message['To']


def email_subject(subject=None):
    message['Subject'] = subject
    return message['Subject']


def email_attach_document():
    documents = askopenfilenames(title='Select files to attach')
    for document in documents:
        with open(document, "rb") as file:
            message.add_attachment(file.read(), maintype="application", subtype="octet-stream",
                                   filename=os.path.basename(file.name))
            filenames.append(os.path.basename(file.name))


def email_content(content=None):
    message['Body'] = content
    return message.set_content(content)


def email_html(content):
    return message.set_content(
        f"""
        {content}
        """, subtype='html')


def email_bcc(*args):
    recipients = []
    for recipient in args:
        recipients.append(recipient)
    message['Bcc'] = recipients
    return message['Bcc']


def email_cc(*args):
    recipients = []
    for recipient in args:
        recipients.append(recipient)
    message['Cc'] = recipients
    return message['Cc']


def store_data_copy():
    date_sent = f"{datetime.datetime.now():%d-%m-%Y Time: %H:%M}"
    with open('messages.txt', 'a') as f:
        f.write(
            f"Date: {date_sent}\nTo: {message['To']}\nCc: {message['Cc']}"
            f"\nBcc: {message['Bcc']}\nSubject: {message['Subject']}"
            f"\nContent: {message['Body']}\nAttached Files: {filenames}\n\n")


def email_send(sender_email, password, host="smtp.gmail.com", port=465):
    message['From'] = sender_email
    try:
        with smtplib.SMTP_SSL(host, port) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(message)
            store_data_copy()
            print(f'Email successfully sent.')
    except socket.gaierror:
        print('Please ensure you have an internet connection.')


def emails_sent():
    with open('messages.txt', 'r') as f:
        file = f.read()
        return file
