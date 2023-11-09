from django.urls import path
from . import views

urlpatterns = [
    path('stdorm/create', views.post_create, name='stdormcreate'),
    path('stdorm/index', views.index, name='stdormpage'),

]
