"""Functions to send emails.
"""

from potato.config import *

from email.utils import getaddresses, parseaddr, make_msgid
from email.mime.text import MIMEText

import smtplib

def send_email(to, body, subject):
    """Sends email.

    :to: Email address of the person.
    :body: A HTML body of the email.
    :subject: Subject!

    Returns nothing.
    """

    recipients = [to] 

    msg = MIMEText(body, 'html')
    msg['Subject'] = subject 
    msg["Message-ID"] = make_msgid()
    msg["To"] = ", ".join(recipients)
    msg["From"] = EMAIL_FROM

    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.ehlo()
    s.starttls()
    s.login(EMAIL_USER, EMAIL_PASSWORD)
    s.sendmail(EMAIL_FROM, recipients, msg.as_string())
    s.quit()

if __name__ == '__main__':
    body = """
    This is a test email! With <b>bold</b> text!
    """

    send_email("elizdet@mit.edu", body, "[Ignore] Test Email!")