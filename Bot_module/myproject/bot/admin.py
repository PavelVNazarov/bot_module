# bot/admin.py
from django.contrib import admin
from .models import User, Trade

admin.site.register(User)
admin.site.register(Trade)
