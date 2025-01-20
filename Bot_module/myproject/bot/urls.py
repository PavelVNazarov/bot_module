
# from django.urls import path, include
# from django.views.generic import RedirectView
#
# urlpatterns = [
#     path('dashboard/', include('bot.urls')),
#     path('', RedirectView.as_view(url='/dashboard/', permanent=False)),
# ]
from django.urls import path
from .views import admin_dashboard, logout_view

urlpatterns = [
    path('admin/', admin_dashboard, name='admin_dashboard'),
    path('logout/', logout_view, name='logout'),  # Убедитесь, что этот маршрут существует
]