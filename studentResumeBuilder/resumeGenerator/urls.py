from django.urls import path
from . import views

urlpatterns = [
    path('', views.choose_template, name='choose-template'),
    path('form/', views.resume_form, name='resume-form')
]
