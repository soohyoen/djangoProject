from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subcription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subcription',null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subcription',null=False)

    class Meta:
        unique_together = ['user', 'project']
