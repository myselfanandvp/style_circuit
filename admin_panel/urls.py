from django.urls import path
from .views import AdminHomeView,AdminListView
urlpatterns=[
    path('home/',AdminHomeView.as_view(),name='admin_home_url'),
    path("list/",AdminListView.as_view(),name="admin_list_url")
]