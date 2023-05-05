from email.message import EmailMessage # imports file to send email
import ssl #python module, provides encryption "secure sockets layer", creating secure connection between client and server
import smtplib # simple email library created by python to send simple emails

email_sender = 'wellspaul554@gmail.com'
email_password = "ljbimkdlkuchlhac" # generated an app password for google that allows python access to gmail, to send the email
email_receiver = 'gofota3408@irebah.com' # temp-mail.org generated

subject = "Dont forget to subscribe"
body = """
When you watch a video, please hit subscribe
"""

em = EmailMessage() # has number of functionalities, just filling in the from / to etc with our variables
em['From'] = email_sender
em['To'] = email_receiver
em[' subject'] = subject
em.set_content(body) # sets the content of the email, after filling in the above required headings

context = ssl.create_default_context() # creating a default connection using SSL

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp: # creates an SMPT object that can be used to send mail, using (host, port, local hostname)
    smtp.login(email_sender, email_password) # with the above process, log in and send (below)
    smtp.sendmail(email_sender, email_receiver, em.as_string()) # sends the email, converts the em into a string for subject and body