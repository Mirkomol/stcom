from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


app_name = 'stmain'

urlpatterns = [
    path('', views.PostList.as_view(), name='main'),
    path('/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('publishpost/', login_required(views.CreatePost.as_view()),  name='publish_post'),
    path('deleteblog/<int:id>/', views.delete_blog,  name='delete_blog')

]


