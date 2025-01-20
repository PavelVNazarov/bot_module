# bot/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    chat_id = models.BigIntegerField(unique=True)

class Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    amount = models.FloatField()
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
