from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    images = models.ImageField(upload_to='users_avatars', blank=True, null=True, verbose_name='Avatar')

    class Meta:
        db_table = 'User'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


