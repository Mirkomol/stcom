from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'stfood'

urlpatterns = [
    path('stfood/', views.IndexClassView.as_view(), name='stfood'),
    path('<int:pk>/',views.FoodDetail.as_view(), name='detail'),

    # add items
    # path('stfood/add', login_required(views.CreateItem.as_view()), name='create_item'),
    path('stfood/add', views.CreateFood, name='create_item'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    # delete
    path('delete/<int:id>/', views.delete_item, name='delete_item')
]


urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)