from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('register/', views.register, name="SignUp"),
    path('', views.register, name="SignUp"),
    path('userList', views.user_list, name='Users'),
    path('requestList/', views.request_list, name='Pending Requests'),
    path('login/', views.login, name='Login | Welcome'),
    path('invalid/', views.invalid, name='Errrr | You encountered error!!'),
]
