from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    def save(self, *args, **kwargs):
        if not self.pk:  # Only set is_active to False on creation
            self.is_active = False
        super().save(*args, **kwargs)
        
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
    
class Passwords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    site = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.site