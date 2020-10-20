from django.urls import path

from conline.base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
]
