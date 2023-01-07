from django.urls import path
from AppBlog.views import * 

urlpatterns = [
    path('', home, name='index'),
]