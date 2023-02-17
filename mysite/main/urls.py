from django.urls import path
from . import views

urlpatterns=[
    path('', views.HomeListView.as_view(), name='home'),
    path('contact-us/', views.ContactListView.as_view(), name='contact-us'),
]