from django.urls import path
from AppBlog.views import * 

urlpatterns = [
    path('', home, name='index'),
    path('about/', about, name='about'),
    path('gastronomy/', gastronomy, name='gastronomy'),
    path('hotels/', hotels, name='hotels'),
    path('activities/', activities, name='activities'),
    path('newpost/', createPost.as_view(), name='newpost'),
    path('postoptions/', PostListView.as_view(), name='postoptions'),
    path('post/edit/<pk>', updatePost.as_view(), name='postedit'),
    path('post/delete/<pk>', deletePost.as_view(), name='postdelete'),
    path('<slug:slug>/', detailpost, name='detailpost'),
    
]