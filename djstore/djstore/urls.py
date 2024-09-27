from django.contrib import admin
from django.conf import settings
from django.conf.urls import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('product.urls')),

] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#TODO:https://www.youtube.com/watch?v=Yg5zkd9nm6w&list=PLhf0_VlTw9T23viD9PDRxWfucKMpxEqU9
#TODO: minute 1hour 28minutes
