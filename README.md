Emaileasily is a python package that simplifies the process of sending and reading emails.

Content
-------
1. [Installation](#Installation)
2. [Send Email](#Send-Email)
3. [Send an email with bcc and cc](#Send-an-email-with-bcc-and-cc)
4. [Send an email with attached document](#Send-an-email-with-attached-document)
5. [Send html email](#Send-html-email)
6. [Read Emails](#Read-Emails)

Installation
------------
```
pip install emaileasily
```
Modify your email settings:
 - Go to Manage google account -> Security -> Apps passwords ->select app
 - Choose other (Custom name) and enter a name of your choice then click generate.
 - Use the generated password to send and read emails using emaileasily.

If you don't have two-step verification just enable allow less secure apps and use your usual password.

Send Email
----------

```pycon
>>> from emaileasily import email_to, email_subject, email_content, email_send

# Accepts more than one email address eg email_to('example.gmail.com', 'example5@gmail.com').
>>> email_to('example.gmail.com')
'example.gmail.com'
>>> email_subject('Python Email')
'Python Email'
>>> email_content('This is an example of sending emails with emaileasily')
# email_send() takes sender address and password as key arguments.
# The functions also takes email host and port as optional arguments.
# Default host="smtp.gmail.com" and port=465
>>> email_send('sender@gmail.com', 'password')
Email successfully sent.
```
Send an email with bcc and cc
----------------

```pycon
>>> from emaileasily import email_to, email_subject, email_content, email_send, email_bcc, email_cc

# Accepts more than one email address.
>>> email_to('example.gmail.com')
'example.gmail.com'
>>> email_bcc('example2@gmail.com')
>>> email_cc('example3@gmail.com')
>>> email_subject('Python Email')
'Python Email'
>>> email_content('This is an example of sending emails with emaileasily')
# email_send() takes sender address and password as key arguments.
# The functions also takes email host and port as optional arguments.
# Default host="smtp.gmail.com" and port=465
>>> email_send('sender@gmail.com', 'password')
Email successfully sent.
```

Send an email with attached document
------------------

```pycon
>>> from emaileasily import email_to, email_subject, email_content, email_send,email_attach_document
>>> email_to('example.gmail.com')
'example.gmail.com'
>>> email_subject('Python Email')
'Python Email'
>>> email_content('This is an example of sending emails with emaileasily')
# Always call the function after email_content
# The functions gives you the option to select documents for attachment.
>>> email_attach_document()
# email_send() takes sender address and password as key arguments.
# The functions also takes email host and port as optional arguments.
# Default host="smtp.gmail.com" and port=465
>>> email_send('sender@gmail.com', 'password')
Email successfully sent.

```

Send html email
-------------------------

```pycon
>>> from emaileasily import email_html
>>> email_html(
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
    <h3>Message</h3>
    <p> Hello this is a html send message.</p>
    <a href='#'>Click here</a>
    </body>
    </html>
    """
    )
```


Read Emails
-----------------

```pycon
>>> from emaileasily import read_emails
"""
Required arguments:
    - email_address and password.
Optional arguments in order:
    -number of emails to read
        Default: 2
    -label
        Default: "INBOX"
    -host
        Default: 'imap.gmail.com'
    -port
        Default: 993
Change the default values according to preference and email account.
If the email has attachment it will be successfully saved in directory.
"""

# Read top inbox email
>>> read_emails(email_address, email_password, 1)

====================================================================================================
Subject:  Read Emails
From:  sender@gmail.com

Hello,

You can simply read emails using emaileasily read_emails function and pass the arguments
email address, password, the number of emails to read, label, host, port.

Kind regards,
Erastus Nzula.

```
Read sent emails by replacing the default label with `label='"[Gmail]/Sent Mail"'`
```pycon
>>> read_emails(email_address,email_password, number_of_emails, label='"[Gmail]/Sent Mail"')
```


