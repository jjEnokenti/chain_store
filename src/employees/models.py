from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    """Employee model."""

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    def __str__(self):
        return self.username
