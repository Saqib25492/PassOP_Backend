from djoser.email import ActivationEmail
from logging import Logger

class ActivateEmail(ActivationEmail):
    def send(self, to, *args, **kwargs):
        print(f"Sending activation mail to {to}")
        try:
            super().send(to, *args, **kwargs)
        except:
            Logger.exception(f"Couldn't send mail to {to}")
            raise
        print(f"Activation mail sent successfully to {to}")