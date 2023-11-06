import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pywhatkit as kit      # whatsappWEB için
import datetime
import logging
from kutuphane import fullzaman
import base64

def send_email(from_email, password, subject, message, to_email):
    #from_email = 'melih@fidanmail.com'
    #password = 'MT%39kf$8'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('mail.smtpserveri buraya yazın.com', 587)  # Update with your SMTP server details
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

# Kullanım
# email_subject = 'Konu Başlığı'
# email_message = 'E-posta içeriği...'
# recipient_email = 'melihfidan@gmail.com'
# send_email(email_subject, email_message, recipient_email)


def send_whatsapp_message(phone_number, message, hours, minutes):
    try:
        # Current time + specified time delay
        now = datetime.datetime.now()
        send_time = now.replace(hour=hours, minute=minutes) + datetime.timedelta(minutes=1)

        # Send the message
        kit.sendwhatmsg(phone_number, message, send_time.hour, send_time.minute)
    except Exception as e:
        logging.error(fullzaman + f'Hata: {e}')

# Kullanım
# phone_number = '+905322865115'  # Alıcı telefon numarası
# whatsapp_message = 'Merhaba, bu bir test mesajıdır.'
# message_hours = datetime.datetime.now().hour #   Gönderim saati (24 saat formatında)
# message_minutes = datetime.datetime.now().minute   # Gönderim dakikası

# send_whatsapp_message(phone_number, whatsapp_message, message_hours, message_minutes)
def encode_password(password):
    # Şifreyi base64 ile şifrele
    encoded_password = base64.b64encode(password.encode()).decode()
    return encoded_password

def decode_password(encoded_password):
    # Şifreyi base64 ile çöz
    decoded_password = base64.b64decode(encoded_password.encode()).decode()
    return decoded_password