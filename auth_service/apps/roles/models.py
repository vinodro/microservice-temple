from django.db import models
from python.django.microservice.auth_service.apps.users.models import User


class Responsibility(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='responsibilities'
    )

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title