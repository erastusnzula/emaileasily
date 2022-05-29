"""
Author: Erastus Nzula.
Licence: MIT.
Description: A simplified way to send and read emails.
Contribution status: open.
"""

import email
import imaplib
import os
import smtplib
import socket
import webbrowser
from email.header import decode_header
from email.message import EmailMessage
from tkinter.filedialog import askopenfilenames

message = EmailMessage()
# filenames = []
body = []
global subject


def email_to(*receivers_addresses):
    """
    :param receivers_addresses: The email main receivers' addresses.
    :return: email receivers' addresses.
    """
    to_recipients = []
    header = 'To'
    return loop_through_addresses(receivers_addresses, to_recipients, header)


def email_subject(subject_=None):
    """
    :param subject_: the email subject.
    :return: email subject.
    """
    try:
        message['Subject'] = subject_
        return message['Subject']
    except ValueError:
        for key in message.keys():
            del message[key]
        print('Re-enter email subject.')


def email_bcc(*bcc_addresses):
    """
    :param bcc_addresses: email bcc receivers' addresses.
    :return: bcc receivers' addresses.
    """
    bcc_recipients = []
    header = 'Bcc'
    return loop_through_addresses(bcc_addresses, bcc_recipients, header)


def email_cc(*cc_addresses):
    """
    :param cc_addresses: the email copy receivers' addresses
    :return: email address
    """
    cc_recipients = []
    header = 'Cc'
    return loop_through_addresses(cc_addresses, cc_recipients, header)


def loop_through_addresses(addresses, recipients, header):
    """
    Loop through all addresses.
    :param addresses: user address input.
    :param recipients: list to store all addresses.
    :param header: message label (To, Bcc or Cc)
    :return: email addresses.
    """
    try:
        for recipient in addresses:
            recipients.append(recipient)
        message[header] = recipients
        return message[header]
    except ValueError:
        for key in message.keys():
            del message[key]
        print('Re-enter email address.')


def email_attach_document():
    """
    Allows attachment of files from directory.
    :return: files to attach.
    """
    try:
        documents = askopenfilenames(title='Select files to attach')
        for document in documents:
            with open(document, "rb") as file:
                message.add_attachment(file.read(), maintype="application", subtype="octet-stream",
                                       filename=os.path.basename(file.name))
                # filenames.append(os.path.basename(file.name))
                print(f'Document: {os.path.basename(file.name)} attached successfully.')
    except TypeError:
        print('Please call the function email_attach_document after email_content')


def email_content(content=None):
    """
    Accepts plain email content.
    :param content: user plain content input.
    :return: email body.
    """
    body.append(content)
    return message.set_content(content)


def email_html(content=None):
    """
    Accepts html content input.
    :param content: html content.
    :return:email body in html format.
    """
    body.append(content)
    return message.set_content(f"""{content}""", subtype='html')


def email_send(sender_email, password, host="smtp.gmail.com", port=465):
    """
    Logs in users and sends emails.
    :param sender_email: sender email address.
    :param password: sender password.
    :param host: email provider host address.
    :param port: email provider port.
    :return: email send status.
    """
    message['From'] = sender_email
    try:
        with smtplib.SMTP_SSL(host, port) as smtp:
            smtp.login(sender_email, password)
            print('Sending email...')
            smtp.send_message(message)
            print(f'Email successfully sent.')
            smtp.quit()
            for key in message.keys():
                del message[key]

    except (smtplib.SMTPRecipientsRefused, socket.gaierror):
        for key in message.keys():
            del message[key]
        print('Failed to send email.')


def name_folder(subject_email):
    """
    Returns the snake case naming convention for emails' attachment folders and filenames.
    :param subject_email: email subject.
    :return: folder name
    """
    return "".join(c if c.isalnum() else "_" for c in subject_email)


def read_emails(email_address, email_password, number_of_emails=2, label='INBOX', host='imap.gmail.com',
                port=993):
    """
    Fetches emails and returns its content.
    :param email_address: sender email address.
    :param email_password: sender email password
    :param number_of_emails: the number of emails to view.
    :param label: the label to fetch emails from.
    :param host: the email provider host address.
    :param port: the email provider port
    :return: fetched emails.
    """
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

    close_imap(imap)


def close_imap(imap):
    """
    Closes the imaplib connection and logs out the user.
    :param imap: The imaplib connection.
    :return: 0
    """
    imap.close()
    imap.logout()


def get_subject_and_from(msg):
    """
    Gets the email subject, date and sender.
    Convert them to human-readable form.
    :param msg: email content
    :return: email subject, sender and date.
    """
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
    """
    Classifies multipart emails based on content type.
    Prints the body of emails without attachments.
    For emails with attachments it returns the get_attachments function.
    param msg: email content.
    :return: email_body.
    """
    global subject
    for part in msg.walk():
        content_type = part.get_content_type()
        content_disposition = str(part.get("Content-Disposition"))
        email_body = None
        try:
            email_body = part.get_payload(decode=True).decode()
        except (AttributeError, UnicodeDecodeError):
            pass
        if content_type == "text/plain" and "attachment" not in content_disposition:
            print(email_body)
        elif "attachment" in content_disposition:
            get_attachments(part)


def get_attachments(part):
    """
    Gets the attached files in a email.
    Creates a folder based on email subject.
    Stores the attached in the folder.
    :param part: The email attachment part
    :return: email attached files.
    """
    filename = part.get_filename()
    if filename:
        folder_name = name_folder(subject)
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        file_path = os.path.join(folder_name, filename)
        open(file_path, "wb").write(part.get_payload(decode=True))
        print('Attached files saved at: ' + file_path)


def get_non_multipart_emails(msg):
    """
    Fetches emails without attachments.
    If email content type is text/plain it prints out the email content(email body).
    If email content type is text/html it returns the get_html_emails function.
    :param msg: email message type
    :return: email_body
    """
    content_type = msg.get_content_type()
    email_body = msg.get_payload(decode=True).decode()
    if content_type == 'text/plain':
        print(email_body)
    if content_type == "text/html":
        get_html_emails(email_body)


def get_html_emails(email_body):
    """
    Creates a folder with name based on the email subject.
    Creates a html file inside the folder.
    Writes the email content in the file and opens it in a web browser.
    :param email_body: fetched email body.
    :return: email_body.
    """
    try:
        folder_name = name_folder(subject)
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        filename = subject + '.html'
        file_path = os.path.join(folder_name, filename)
        open(file_path, "w").write(email_body)
        print(email_body)
        webbrowser.open(file_path)
    except UnicodeEncodeError:
        pass
