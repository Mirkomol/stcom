from django.conf.urls.static import static
from django.urls import path
from steconomy import views as stecoviews
from django.conf import settings


urlpatterns = [
    path('steconomy/', stecoviews.index, name = 'steconomy'),
    path('steconomy/edit/<int:id>/', stecoviews.edit, name= 'edit'),
    path('steconomy/delete/<int:id>/', stecoviews.delete, name= 'ecodelete'),]


urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

