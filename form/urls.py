from django.urls import path

from form import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getdata', views.getdata, name="getdata"),
    path('profile', views.profile, name="profile"),
    path('delete_contact/<int:usn>/', views.delete_contact, name='delete_contact'),
    path('update_contact/<int:usn>/', views.update_contact, name='update_contact'),

]
