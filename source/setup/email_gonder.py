import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, to_email):
    from_email = 'buraya gönderen email adresi girin'
    password = 'password'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('mail.burayasmtpserveradinigirin.com', 587)  # Update with your SMTP server details
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

# Kullanım
email_subject = 'Konu Başlığı'
email_message = 'E-posta içeriği...'
recipient_email = 'buraya gönderen email adresi girin'
send_email(email_subject, email_message, recipient_email)
