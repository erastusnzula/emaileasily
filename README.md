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

View all sent emails
-------------------
```pycon
>>> from emaileasily import emails_sent

# List all sent emails.
# The emails can be viewed manually by opening the directory file emails.csv.
>>> emails_sent() 

                  Date                 To              Cc             Bcc           Subject                                            Content                 Files
04-03-2022 Time: 17:58 receiver@gmail.com ccopy@gmail.com bcopy@gmail.com Read Inbox Emails Hello,You can simply read inbox emails using th...          ['blog.JPG']
04-03-2022 Time: 17:58 receiver@gmail.com ccopy@gmail.com bcopy@gmail.com Read Inbox Emails Hello,You can simply read inbox emails using th... ['assignment 1.docx']
04-03-2022 Time: 17:58 receiver@gmail.com ccopy@gmail.com bcopy@gmail.com Read Inbox Emails Hello,You can simply read inbox emails using th...                    []
04-03-2022 Time: 17:58 receiver@gmail.com ccopy@gmail.com bcopy@gmail.com Read Inbox Emails Hello,You can simply read inbox emails using th...                    []
04-03-2022 Time: 17:58 receiver@gmail.com ccopy@gmail.com bcopy@gmail.com Read Inbox Emails Hello,You can simply read inbox emails using th...                    []
04-03-2022 Time: 17:58 receiver@gmail.com ccopy@gmail.com bcopy@gmail.com Read Inbox Emails Hello,You can simply read inbox emails using th...                    []

```

View the last sent email
------------------------
```pycon
>>> from emaileasily import get_last_sent_email
>>> get_last_sent_email()

                  Date                 To              Cc             Bcc           Subject                                            Content Files
04-03-2022 Time: 17:59 receiver@gmail.com ccopy@gmail.com bcopy@gmail.com Read Inbox Emails Hello,You can simply read inbox emails using th...    []

```

View the last five sent emails
------------------------------
```pycon
>>> from emaileasily import get_last_five_sent_emails
>>> get_last_five_sent_emails()
```
Read Inbox Emails
-----------------
```pycon
>>> from emaileasily import read_inbox_emails
>>> read_inbox_emails(email_address, email_password, number_of_emails_to read)

 _____  __  __     _     ___  _      _____     _     ____   ___  _     __   __
| ____||  \/  |   / \   |_ _|| |    | ____|   / \   / ___| |_ _|| |    \ \ / /
|  _|  | |\/| |  / _ \   | | | |    |  _|    / _ \  \___ \  | | | |     \ V / 
| |___ | |  | | / ___ \  | | | |___ | |___  / ___ \  ___) | | | | |___   | |  
|_____||_|  |_|/_/   \_\|___||_____||_____|/_/   \_\|____/ |___||_____|  |_|  
                                                                              

Subject:  Read Inbox Emails
From:  nzulaerastus@gmail.com

Hello,

You can simply read inbox emails using the emaileasily function read_inbox_emails and pass the arguments
email address, password and the number of emails to read.

Kind regards,
Erastus Nzula.
    
    

______________________________________________________________________________________________________________________________________________________

```