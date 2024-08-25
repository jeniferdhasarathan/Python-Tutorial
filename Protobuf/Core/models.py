from django.db import models


class SampleModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    data = models.BinaryField(null=True)  





from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    # Override the groups and user_permissions fields to avoid the clash
    groups = models.ManyToManyField(
        Group,
        related_name='core_user_set',  # Updated related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='core_user_set',  # Updated related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    is_default = models.BooleanField(default=False)  # Indicates if this is the default project

    def save(self, *args, **kwargs):
        if self.is_default:
            # Set other projects of the same owner to non-default
            Project.objects.filter(owner=self.owner, is_default=True).update(is_default=False)
        super().save(*args, **kwargs)

class AdminAccess(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_access', limit_choices_to={'is_admin': True})
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='admin_access')

    class Meta:
        unique_together = ('admin', 'project')
