from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class User2(AbstractUser):
    """Кастомная модель пользователя."""
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    ]
    email = models.EmailField(unique=True)
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль',
        max_length=20,
        choices=ROLE_CHOICES,
        default=USER
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='users_user_unique_relationships',
                fields=('email', 'username'),
            ),
        ]
        ordering = ['id']

    @property
    def is_user(self):
        return self.role == User2.USER

    @property
    def is_moderator(self):
        return self.role == User2.MODERATOR

    @property
    def is_admin(self):
        return self.role == User2.ADMIN


@receiver(pre_save, sender=User2)
def auto_is_staff(sender, instance, *args, **kwargs):
    """Авто присвоение флага is_staff пользователям с ролью 'admin'."""
    if instance.role == User2.ADMIN:
        instance.is_staff = True
    elif instance.role == User2.USER or User2.MODERATOR:
        instance.is_staff = False


@receiver(pre_save, sender=User2)
def auto_admin_for_superuser(sender, instance, *args, **kwargs):
    """Авто присвоение роли 'admin' суперюзерам."""
    if instance.is_superuser:
        instance.role = User2.ADMIN
        instance.is_staff = True
