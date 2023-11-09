from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from stusers import views as user_views
from django.contrib.auth import views as authentication_views
from stusers.views import RegisterView


urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='stusers/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='stusers/logout.html'), name='logout'),
    path('profile/', user_views.profilepage, name='profile'),

]


urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




