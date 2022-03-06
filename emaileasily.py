import email
import imaplib
import os
import smtplib
import socket
import webbrowser
from email.header import decode_header
from email.message import EmailMessage
from tkinter.filedialog import askopenfilenames

from art import tprint

tprint('EMAILEASILY', font='medium')
message = EmailMessage()
filenames = []
body = []
global subject


def email_to(*receivers_addresses):
    recipients = []
    for recipient in receivers_addresses:
        recipients.append(recipient)
    message['To'] = recipients
    return message['To']


def email_subject(subject_=None):
    message['Subject'] = subject_
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
    return message.set_content(f"""{content}""", subtype='html')


def email_send(sender_email, password, host="smtp.gmail.com", port=465):
    message['From'] = sender_email
    try:
        with smtplib.SMTP_SSL(host, port) as smtp:
            smtp.login(sender_email, password)
            print('Sending email...')
            smtp.send_message(message)
            print(f'Email successfully sent.')
    except socket.gaierror:
        print('Please ensure you have an internet connection.')


def name_folder(subject_email):
    return "".join(c if c.isalnum() else "_" for c in subject_email)


def read_emails(email_address, email_password, number_of_emails=3, label='INBOX', host='imap.gmail.com',
                port=993):
    global subject
    imap = imaplib.IMAP4_SSL(host, port)
    imap.login(email_address, email_password)
    print('Successfully logged in, fetching emails...')
    status, all_messages = imap.select(label)
    messages = int(all_messages[0])
    for i in range(messages, messages - number_of_emails, -1):
        _, email_messages = imap.fetch(str(i), "(RFC822)")
        for email_message in email_messages:
            if isinstance(email_message, tuple):
                msg = email.message_from_bytes(email_message[1])
                get_subject_and_from(msg)

                if msg.is_multipart():
                    get_multipart_email(msg)
                else:
                    get_non_multipart_emails(msg)

    imap.close()
    imap.logout()


def get_subject_and_from(msg):
    global subject
    subject, encoding = decode_header(msg['Subject'])[0]
    if isinstance(subject, bytes):
        try:
            subject = subject.decode(encoding)
        except TypeError:
            pass
    sender, encoding = decode_header(msg.get("From"))[0]
    if isinstance(sender, bytes):
        sender = sender.decode(encoding)
    date, encoding = decode_header(msg.get("Date"))[0]
    if isinstance(date, bytes):
        date = date.decode(encoding)
    print('==' * 50)
    print("Subject: ", subject)
    print("From: ", sender)
    print("Date: ", date)


def get_multipart_email(msg):
    global subject
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
        elif "attachment" in content_disposition:
            filename = part.get_filename()
            if filename:
                folder_name = name_folder(subject)
                if not os.path.isdir(folder_name):
                    os.mkdir(folder_name)
                file_path = os.path.join(folder_name, filename)
                open(file_path, "wb").write(part.get_payload(decode=True))


def get_non_multipart_emails(msg):
    content_type = msg.get_content_type()
    e_body = msg.get_payload(decode=True).decode()
    if content_type == 'text/plain':
        print(e_body)
    if content_type == "text/html":
        folder_name = name_folder(subject)
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        filename = subject + '.html'
        file_path = os.path.join(folder_name, filename)
        open(file_path, "w").write(e_body)
        print(e_body)
        webbrowser.open(file_path)
