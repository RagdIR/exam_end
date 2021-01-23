from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from api.views import AddViewSet, DellViewSet


app_name = 'api'


urlpatterns = [
    path('<int:pk>/add/', AddViewSet, name='add'),
    path('<int:pk>/remove/', DellViewSet, name='remove')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

