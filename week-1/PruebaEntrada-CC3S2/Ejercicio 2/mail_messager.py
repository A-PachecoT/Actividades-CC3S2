# Credits: Brad Solomon, David Okwii https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
# TODO proper ensamblation of the codes
import smtplib


def send_email(user, pwd, recipient, subject, body):

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")

gmail_user = 'andre.pacheco.t@uni.pe'
gmail_pwd = '<PASSWORD>'

# SMTP_SSL Example
server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server_ssl.ehlo() # optional, called by login()
server_ssl.login(gmail_user, gmail_pwd)
# ssl server doesn't support or need tls, so don't call server_ssl.starttls()
server_ssl.sendmail(FROM, TO, message)
#server_ssl.quit()
server_ssl.close()
print 'successfully sent the mail'