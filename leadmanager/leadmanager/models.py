from django.db import models

class Lead(modles.Model):
    name = model.CharField(max_length=100)
    email = modles.EmailField(max_length=100, unique=True)
    message = models.CharFiels(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
