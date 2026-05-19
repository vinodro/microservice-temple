from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        SUPER_ADMIN = 'SUPER_ADMIN'
        TEMPLE_ADMIN = 'TEMPLE_ADMIN'
        REPRESENTATIVE = 'REPRESENTATIVE'
        PUSARI = 'PUSARI'
        FUND_COLLECTOR = 'FUND_COLLECTOR'
        DEVOTEE = 'DEVOTEE'

    phone = models.CharField(max_length=20, unique=True)

    role = models.CharField(
        max_length=30,
        choices=Role.choices,
        default=Role.DEVOTEE
    )

    temple_name = models.CharField(max_length=255, blank=True)

    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username