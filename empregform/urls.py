from django.urls import path
from . import views

urlpatterns = [
    path('empregform', views.index1, name='index1'),
    path('getdata1', views.getdata1, name='getdata1'),
    path('display_data',views.display_data,name='display_data'),
    path('delete_form/<int:usn>/', views.delete_form, name='delete_form'),

]
