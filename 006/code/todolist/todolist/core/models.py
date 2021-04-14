from django.db import models


class TodoItems(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    done = models.BooleanField()
