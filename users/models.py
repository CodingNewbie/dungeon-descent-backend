from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser (AbstractUser):
    states = models.JSONField(default=dict)

