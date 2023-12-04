from . import views
from django.urls import path

app_name = 'microservicio2'

urlpatterns = [
   path('', views.index, name='index')

]