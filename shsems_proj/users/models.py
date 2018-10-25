from django.db import models

from django.contrib.auth.models import AbstractUser

class Participant(AbstractUser):
    contact_number = models.CharField("Contact Number",
       max_length = 50)

    def __str__(self):
        return self.username
