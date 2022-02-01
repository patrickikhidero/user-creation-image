from django.core.mail import send_mail
import random
import base64
from decouple import config


class Util:

    @staticmethod
    def generate_password():
        letters = 'abcdefghijklmnopqrstuwxyz'
        password = ''
        for i in range(8):
            password += random.choice(letters)
        return password

    @staticmethod
    def generate_otp():
        otp_code = random.randrange(1000, 9999)
        return otp_code

    @staticmethod
    def send_email(data):
        email_subject = data['email_subject']
        message = data['email_body']
        email_from = config('EMAIL_HOST_USER', default='annony@gmail.com')
        email_to = data['to_email']
        html_format = data['email_body']
        try:
            send_mail(email_subject, message, email_from, email_to,
                      fail_silently=False, html_message=html_format)   
        except Exception as err:
            raise err

    @staticmethod
    def encode_password(password):
        if type(password) != str:
            password = str(password)
        encoded_password = base64.b64encode(password.encode())
        return encoded_password.decode()