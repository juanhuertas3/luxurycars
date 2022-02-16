from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/gestionventas/', permanent=True)),
    path('gestionventas/', include('gestionventas.urls')),
]

#Avatares
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)