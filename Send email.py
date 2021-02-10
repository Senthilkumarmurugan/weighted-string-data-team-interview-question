import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(receiver_email: str,message: str) -> dict:
    """ Function to send an email to the created Users in Orange Hrm"""

    Email=config['Email']
    port = Email['port']
    smtp_server = Email['smtp_server']
    sender_email = Email['sender_email']
    _password = Email['password']
    
    msg = MIMEMultipart()
    
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Orange Hrm credentials"
    # msg["cc"]=""
    msg.attach(MIMEText(message,'plain'))
    
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, _password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            return {"Success":"Mail sent successfully"}
    except Exception as e:
        return {"Error Exception as ":e}
