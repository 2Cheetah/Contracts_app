from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user_role_choices = [
        ('PJM', 'Project Manager'),
        ('CUS', 'Customer Interface'),
        ('BUS', 'Business Case Accountable'),
        ('LOG', 'Logistics Accountable'),
        ('PRO', 'Production Accountable'),
        ('QUA', 'Quality Accoutable'),
        ('GEN', 'General Manager'),
        ('PUR', 'Purchasing Accountable'),
        ('ACC', 'Accounting')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_role = models.CharField(max_length=3, choices=user_role_choices, default='goods')
    image = models.ImageField(default='default.jpg', blank=True, null=True, upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
