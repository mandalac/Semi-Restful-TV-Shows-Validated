from django.db import models

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title'])<2:
            errors['title'] = 'Title should have at least 2 characters'
        if len(postData['network'])<3:
            errors['network'] = 'Network should have at least 3 characters'
        if len(postData['description'])<10:
            errors['description'] = 'Description should have at leat 10 characters'
        return errors



class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
