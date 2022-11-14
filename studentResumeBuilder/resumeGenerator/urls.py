from django.urls import path
from . import views

urlpatterns = [
    path('', views.choose_template, name='choose-template'),
    path('form/', views.resume_form, name='resume-form'),
    path('resume1/', views.resume1, name='resume1'),
    path('view/', views.resume_view, name='resume-view'),
    path('resume2/', views.resume2, name='resume2'),
    path('resume3/', views.resume3, name='resume3'),
    path('switch/', views.switch_template, name='resume-switch'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
]
