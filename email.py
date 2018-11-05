# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

msg = MIMEText('This is message')

# me == the sender's email address
me = 'jiayi.lu2@cn.bosch.com'
you = 'jiayi.lu2@cn.bosch.com'

msg['Subject'] = 'The contents of is .....'
msg['From'] = me
msg['To'] = you
# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('')
s.sendmail(me, [you], msg.as_string())
s.quit()
