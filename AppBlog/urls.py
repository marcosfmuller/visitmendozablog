from django.urls import path
from AppBlog.views import * 

urlpatterns = [
    path('', home, name='index'),
    path('about/', about, name='about'),
    path('gastronomy/', gastronomy, name='gastronomy'),
    path('hotels/', hotels, name='hotels'),
    path('activities/', activities, name='activities'),
    path('newpost/', createPost.as_view(), name='newpost'),
    path('<slug:slug>/', detailpost, name='detailpost'),
    
]