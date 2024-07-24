import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    """
    將密碼hash加密
    :param password:
    :return:
    """
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """
    驗證密碼
    :param plain_password:
    :param hashed_password:
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)


def send_email(to_address: str, username: str, content_data: str):
    from_address = "my_email_adress"
    password = "jdvxjaokltuhoshx"

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = "event_email"

    body = f"Hi {username},\n\nThis is an information for you.\n\n{content_data}\n\nBest regards,"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, password)
        text = msg.as_string()
        server.sendmail(from_address, to_address, text)
        server.quit()
        print(f"Email sent successfully to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}. Error: {str(e)}")




