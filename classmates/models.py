from django.db import models
from django.urls import reverse

class Classmate(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200, default='Unknown')  # Add the address field
    gender = models.CharField(max_length=10, default='Unknown')
    # Add the gender field

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('classmate_edit', kwargs={'pk': self.pk})

