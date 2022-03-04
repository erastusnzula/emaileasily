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
                   Date                 To              Cc             Bcc         Subject                                                        Content          Files
03-03-2022 Time: 21:30 receiver@gmail.com ccopy@gmail.com bcopy@gmail.com Python Articles \r\nHello,\r\n\r\nPython articles contribute largely to my ... ['cover.docx']
03-03-2022 Time: 21:30 receiver@gmail.com ccopy@gmail.com bcopy@gmail.com Python Articles \r\nHello,\r\n\r\nPython articles contribute largely to my ... ['cover.docx']
03-03-2022 Time: 21:30 receiver@gmail.com ccopy@gmail.com bcopy@gmail.com Python Articles \r\nHello,\r\n\r\nPython articles contribute largely to my ... ['cover.docx']
03-03-2022 Time: 21:31 receiver@gmail.com ccopy@gmail.com bcopy@gmail.com Python Articles \r\nHello,\r\n\r\nPython articles contribute largely to my ... ['cover.docx']
03-03-2022 Time: 21:31 receiver@gmail.com ccopy@gmail.com bcopy@gmail.com Python Articles \r\nHello,\r\n\r\nPython articles contribute largely to my ... ['cover.docx']

```

View the last sent email
------------------------
```pycon
>>> from emaileasily import get_last_sent_email
>>> get_last_sent_email()

                  Date                 To              Cc             Bcc         Subject                                                        Content          Files
03-03-2022 Time: 21:32 receiver@gmail.com ccopy@gmail.com bcopy@gmail.com Python Articles \r\nHello,\r\n\r\nPython articles contribute largely to my ... ['cover.docx']

```

View the last five sent emails
------------------------------
```pycon
>>> from emaileasily import get_last_five_sent_emails
>>> get_last_five_sent_emails()
```
