from __future__ import unicode_literals
from django.db import models
from datetime import datetime, date

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        received_date = postData["release_date"]
        today = datetime.strftime(date.today(), '%Y-%m-%d')
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if received_date > today:
            errors["release_date"] = "Release date must be day in the past"
        if postData['description']:
            if len(postData['description']) < 10:
                errors["description"] = "Description should be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(default="generic description here")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

