from django.db import models
from django.db.models.fields.related import ForeignKey
from django.urls import reverse_lazy

class Blog(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    context = models.TextField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('home')
        