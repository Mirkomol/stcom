from django.urls import path
from stcv import views as stcvviews

urlpatterns = [
    path('stcv/', stcvviews.accept, name = 'stcv'),
    path('stcv/<int:id>/', stcvviews.cv, name= 'cv'),
    path('stcv/list', stcvviews.list, name='list'),
    path('deletecv/<int:id>/', stcvviews.delete_cv, name='delete_cv')
]