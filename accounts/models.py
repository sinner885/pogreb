from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    '''пользовательськая модель'''
    # добавьте сюда дополнительные поля

    def __str__(self):
        return self.email