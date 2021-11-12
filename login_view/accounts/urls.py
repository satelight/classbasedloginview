from django.urls import path
from .views import (
    RegisterUserView,HomeView,UserLoginView,UserLogoutView
)

app_name = "accounts"

urlpatterns =[
    path('home/',HomeView.as_view(),name='home'),
    path('regist/',RegisterUserView.as_view(),name='regist'),
    path('user_login/',UserLoginView.as_view(),name='user_login'),
    path('user_logout/', UserLogoutView.as_view(), name='user_logout'),

]
