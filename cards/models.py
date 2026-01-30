from django.db import models
from django.contrib.auth.models import User

class ValentineCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=50)
    receiver_name = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
