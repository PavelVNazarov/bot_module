# bot/views.py
from django.shortcuts import render
from .models import User, Trade

def admin_dashboard(request):
    users = User.objects.all()
    trades = Trade.objects.all()
    return render(request, 'bot/admin_dashboard.html', {'users': users, 'trades': trades})
