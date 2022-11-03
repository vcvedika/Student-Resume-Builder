from django.urls import path
from landingPage import views

urlpatterns = [
    path('',views.landing_page_view,name='landing-page'),
]
