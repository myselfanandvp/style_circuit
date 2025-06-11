from django.urls import path
from .views import AdminHomeView,AdminListView,AdminEditView,AdminDeleteView
urlpatterns=[
    path('home/',AdminHomeView.as_view(),name='admin_home_url'),
    path("list/",AdminListView.as_view(),name="admin_list_url"),
    path("edit/<uuid:userid>/",AdminEditView.as_view(),name="admin_edit_url"),
    path("delete/<uuid:userid>/",AdminDeleteView.as_view(),name="admin_delete_url"),
]