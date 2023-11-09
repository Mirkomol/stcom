from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from stusers import views as user_views
from django.contrib.auth import views as authentication_views
from stusers.views import RegisterView





urlpatterns = [
    path('superuser/', admin.site.urls),
    path('', include('stfood.urls')),
    path('', include('stmain.urls')),
    path('', include('stcv.urls')),
    path('', include('steconomy.urls')),
    path('', include('stusers.urls')),
    path('', include('stdorm.urls')),

]

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)