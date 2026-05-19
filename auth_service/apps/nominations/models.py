from django.db import models
from python.django.microservice.auth_service.apps.users.models import User


class Nomination(models.Model):

    class Status(models.TextChoices):
        PENDING = 'PENDING'
        APPROVED = 'APPROVED'
        REJECTED = 'REJECTED'

    nominee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='nominee'
    )

    nominated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='nominator'
    )

    role = models.CharField(max_length=255)

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
    
    