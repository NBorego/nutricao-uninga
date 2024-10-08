from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogo.urls')),
    path('agendamento/', include('agendamento.urls')),
    path('login/', include('login.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
