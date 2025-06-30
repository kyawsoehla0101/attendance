from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files import File
from io import BytesIO
import qrcode
from django.contrib.auth.models import User

from django.utils.timezone import now
from django.utils import timezone



class PersonProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class QRData(models.Model):
    person = models.OneToOneField(PersonProfile, on_delete=models.CASCADE)
    qr_image = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    qr_string = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.qr_string = f"{self.person.id},{self.person.name}"
        qr = qrcode.make(self.qr_string)
        buffer = BytesIO()
        qr.save(buffer)
        self.qr_image.save(f"{self.person.name}_qr.png", File(buffer), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"QR for {self.person.name}"

class Attendance(models.Model):
    person = models.ForeignKey(PersonProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # timestamp = models.DateTimeField(auto_now_add=True)  # check-in/out time
    action = models.CharField(max_length=10, choices=[('in', 'Check-in'), ('out', 'Check-out')])

    def __str__(self):
        return f"{self.person.user.username} - {self.action} at {self.timestamp}"
