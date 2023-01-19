from django.urls import path
from AppAccounts.views import * 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('panelctrl/', panelctrl, name='panelctrl'),
    path('profile/', editar_perfil, name='profile'),
   
    path('user/list/', UserListView.as_view(), name='userlist'),
    path('user/edit/<pk>', UserUpdateView.as_view(), name='useredit'),
    path('user/delete/<pk>', UserDeleteView.as_view(), name='userdelete'),


    path('register/', register, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
  
 
]