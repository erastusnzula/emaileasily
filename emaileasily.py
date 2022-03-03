import csv
import datetime
import os
import smtplib
import socket
from email.message import EmailMessage
from tkinter.filedialog import askopenfilenames

import pandas

message = EmailMessage()
filenames = []
body = []


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
    body.append(content)
    return message.set_content(content)


def email_html(content=None):
    body.append(content)
    return message.set_content(content, subtype='html')


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


def email_copy_csv():
    try:
        date_sent = f"{datetime.datetime.now():%d-%m-%Y Time: %H:%M}"
        columns = ['Date', 'To', 'Cc', 'Bcc', 'Subject', 'Content', 'Files']
        body_ = '.'.join([x[:50] for x in body])
        rows = [date_sent, message['To'], message['Cc'], message['Bcc'], message['Subject'],
                body_, filenames]
        filename = 'emails.csv'
        new_file = not os.path.exists(filename)
        with open(filename, 'a') as f:
            writer = csv.writer(f, lineterminator="\n")
            if new_file:
                writer.writerow(columns)
            writer.writerow(rows)
    except TypeError:
        print('You have no sent emails.')


def email_send(sender_email, password, host="smtp.gmail.com", port=465):
    message['From'] = sender_email
    try:
        with smtplib.SMTP_SSL(host, port) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(message)
            email_copy_csv()
            print(f'Email successfully sent.')
    except socket.gaierror:
        print('Please ensure you have an internet connection.')


def emails_sent():
    try:
        filename = 'emails.csv'
        df = pandas.read_csv(filename)
        df = df.to_string(index=False)
        pandas.set_option('display.max_columns', None)
        pandas.set_option('display.max_rows', None)
        return df
    except FileNotFoundError:
        print('You have no sent emails.')


def get_last_sent_email():
    try:
        filename = 'emails.csv'
        df = pandas.read_csv(filename)
        pandas.set_option('display.max_columns', None)
        pandas.set_option('display.max_rows', None)
        return df.tail(1).to_string(index=False)
    except FileNotFoundError:
        print('You have no sent emails.')


def get_last_five_sent_emails():
    try:
        filename = 'emails.csv'
        df = pandas.read_csv(filename)
        pandas.set_option('display.max_columns', None)
        pandas.set_option('display.max_rows', None)
        return df.tail().to_string(index=False)
    except FileNotFoundError:
        print('You have no sent emails.')
