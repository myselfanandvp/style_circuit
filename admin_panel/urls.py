from django.urls import path
from .views import AdminHomeView
urlpatterns=[
    path('home/',AdminHomeView.as_view(),name='admin_home_url'),
]