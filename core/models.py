from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE,
        related_name='profile'
    )

    region = models.CharField(max_length=1, choices=(
        ('1', 'Bishkek'),
        ('2', 'Osh'),
        ('3', 'Batken'),
        ('4', 'Djalal-Abad'),
        ('5', 'Naryn'),
        ('6', 'Talas'),
        ('7', 'Issyk-Kul'),
        ('8', 'Chuy'),
    ))

    photo = models.ImageField(
        upload_to='profile photo',
        null=True, blank=True
    )

    def __str__(self):
        return self.user.username
