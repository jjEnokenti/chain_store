from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    """Employee model."""

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.username
