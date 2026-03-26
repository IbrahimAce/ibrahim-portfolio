from django.dispatch import receiver
from axes.signals import user_locked_out

@receiver(user_locked_out)
def send_lockout_email(sender, request, username, ip_address, **kwargs):
    # Render Free Tier blocks SMTP, so we just log it to the Render console instead
    print(f"🚨 SUCCESSFUL LOCKOUT: User '{username}' from IP {ip_address} has been locked out!")
