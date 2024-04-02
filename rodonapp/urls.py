from .import views
from django.urls import path


urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('contact_submit', views.contact_submit, name='contact_submit'),
    path('adminlog',views.adminlog,name='adminlog'),
    path('properties',views.properties,name='properties'),
    path('delete_message/', views.delete_message, name='delete_message'),
    path('admin', views.admin, name='admin'),
    path('signin',views.signin,name='signin'),
    path('user_logout',views.user_logout,name='user_logout'),
]