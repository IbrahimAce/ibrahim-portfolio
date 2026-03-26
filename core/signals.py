from django.dispatch import receiver
from axes.signals import user_locked_out
from django.core.mail import send_mail
import os


@receiver(user_locked_out)
def send_lockout_email(sender, request, username, ip_address, **kwargs):
    send_mail(
        subject='🚨 Failed Login Attempt on Your Portfolio!',
        message=f'Someone was locked out!\n\nUsername tried: {username}\nIP Address: {ip_address}\n\nThis happened on your Django portfolio admin.',
        from_email=os.environ.get('EMAIL_USER'),
        recipient_list=['karanjaibrahim141@gmail.com'],
        fail_silently=True,
    )
