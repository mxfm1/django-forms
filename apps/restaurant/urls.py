from django.urls import path
from .views import get_user_info
urlpatterns = [
    path("user",get_user_info,name='get_user_info')
]