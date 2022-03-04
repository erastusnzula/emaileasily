import csv
import datetime
import email
import imaplib
import os
import smtplib
import socket
import webbrowser
from email.header import decode_header
from email.message import EmailMessage
from tkinter.filedialog import askopenfilenames

import pandas
from art import tprint

tprint('EMAILEASILY')

message = EmailMessage()
filenames = []
body = []


def email_to(*receivers_addresses):
    recipients = []
    for recipient in receivers_addresses:
        recipients.append(recipient)
    message['To'] = recipients
    return message['To']


def email_subject(subject=None):
    message['Subject'] = subject
    return message['Subject']


def email_bcc(*bcc_addresses):
    recipients = []
    for recipient in bcc_addresses:
        recipients.append(recipient)
    message['Bcc'] = recipients
    return message['Bcc']


def email_cc(*cc_addresses):
    recipients = []
    for recipient in cc_addresses:
        recipients.append(recipient)
    message['Cc'] = recipients
    return message['Cc']


def email_attach_document():
    try:
        documents = askopenfilenames(title='Select files to attach')
        for document in documents:
            with open(document, "rb") as file:
                message.add_attachment(file.read(), maintype="application", subtype="octet-stream",
                                       filename=os.path.basename(file.name))
                filenames.append(os.path.basename(file.name))
                print(f'Document: {os.path.basename(file.name)} attached successfully.')
    except TypeError:
        print('Please call the function email_attach_document after email_content')


def email_content(content=None):
    body.append(content)
    return message.set_content(content)


def email_html(content=None):
    body.append(content)
    return message.set_content(content, subtype='html')


def email_copy_csv():
    try:
        date_sent = f"{datetime.datetime.now():%d-%m-%Y Time: %H:%M}"
        columns = ['Date', 'To', 'Cc', 'Bcc', 'Subject', 'Content', 'Files']
        body_ = '.'.join([x[:40] for x in body])
        rows = [date_sent, message['To'], message['Cc'], message['Bcc'], message['Subject'],
                body_ + '...', filenames]
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
            print('Sending email...')
            smtp.send_message(message)
            email_copy_csv()
            print(f'Email successfully sent.')
    except socket.gaierror:
        print('Please ensure you have an internet connection.')


def emails_sent():
    try:
        filename = 'emails.csv'
        df = pandas.read_csv(filename)
        df.replace(to_replace=["\\t|\\n|\\r", "\t|\n|\r"], value=['', ''], regex=True, inplace=True)
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
        df.replace(to_replace=["\\t|\\n|\\r", "\t|\n|\r"], value=['', ''], regex=True, inplace=True)
        pandas.set_option('display.max_columns', None)
        pandas.set_option('display.max_rows', None)
        return df.tail(1).to_string(index=False)
    except FileNotFoundError:
        print('You have no sent emails.')


def get_last_five_sent_emails():
    try:
        filename = 'emails.csv'
        df = pandas.read_csv(filename)
        df.replace(to_replace=["\\t|\\n|\\r", "\t|\n|\r"], value=['', ''], regex=True, inplace=True)
        pandas.set_option('display.max_columns', None)
        pandas.set_option('display.max_rows', None)
        return df.tail().to_string(index=False)
    except FileNotFoundError:
        print('You have no sent emails.')


def name_folder(subject):
    return "".join(c if c.isalnum() else "_" for c in subject)


def read_inbox_emails(email_address, email_password, number_of_emails=2, host='imap.gmail.com', port=993):
    imap = imaplib.IMAP4_SSL(host, port)
    imap.login(email_address, email_password)
    status, all_messages = imap.select("INBOX")
    # print(imap.list())
    messages = int(all_messages[0])
    for i in range(messages, messages - number_of_emails, -1):
        _, email_messages = imap.fetch(str(i), "(RFC822)")
        for email_message in email_messages:
            if isinstance(email_message, tuple):
                msg = email.message_from_bytes(email_message[1])
                subject, encoding = decode_header(msg['Subject'])[0]
                if isinstance(subject, bytes):
                    try:
                        subject = subject.decode(encoding)
                    except TypeError:
                        pass
                sender, encoding = decode_header(msg.get("From"))[0]
                if isinstance(sender, bytes):
                    sender = sender.decode(encoding)
                print("Subject: ", subject)
                print("From: ", sender)
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        e_body = None
                        try:
                            e_body = part.get_payload(decode=True).decode()
                        except (AttributeError, UnicodeDecodeError):
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            print(e_body)
                            print("_" * 150)
                        elif "attachment" in content_disposition:
                            filename = part.get_filename()
                            if filename:
                                folder_name = name_folder(subject)
                                if not os.path.isdir(folder_name):
                                    os.mkdir(folder_name)
                                file_path = os.path.join(folder_name, filename)
                                open(file_path, "wb").write(part.get_payload(decode=True))

                else:
                    content_type = msg.get_content_type()
                    e_body = msg.get_payload(decode=True).decode()
                    if content_type == 'text/plain':
                        print(e_body)
                        print("_" * 150)
                    if content_type == "text/html":
                        folder_name = name_folder(subject)
                        if not os.path.isdir(folder_name):
                            os.mkdir(folder_name)
                        filename = 'email_html_content.html'
                        file_path = os.path.join(folder_name, filename)
                        open(file_path, "w").write(e_body)
                        webbrowser.open(file_path)
    imap.close()
    imap.logout()
