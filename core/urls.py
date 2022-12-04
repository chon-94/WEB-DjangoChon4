from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('curriculum/', include('curriculum.urls',namespace='curriculum')),
    path('contacto/', include('contacto.urls',namespace='contacto')),
    path('about/', include('about.urls',namespace='about')),
    path('blog/', include('blog.urls',namespace='blog')),
    path('accounts/', include('allauth.urls')),
    ]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)