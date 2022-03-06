Emaileasily is a python package that simplifies the process of sending emails.

Installation
------------
```
pip install emaileasily
```

Usage
=====
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
Add email bcc and cc
----------------
```pycon
>>> from emaileasily import email_bcc, email_cc

# Accepts more than one email address.
>>> email_bcc('example2@gmail.com')
>>> email_cc('example3@gmail.com')
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

Attach Documents
------------------
```pycon
>>> from emaileasily import email_attach_document

# Call the function after email_content
# The functions gives you the option to select documents for attachment.
>>> email_attach_document()
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
Subject:  Read Inbox Emails
From:  nzulaerastus@gmail.com

Hello,

You can simply read emails using emaileasily's read_emails function and pass the arguments
email address, password, the number of emails to read, label, host, port.

Kind regards,
Erastus Nzula.

# To read sent emails replace the default label with '"[Gmail]/Sent Mail"'
>>> read_emails(email_address,email_password, number_of_emails, label='"[Gmail]/Sent Mail"')
```
