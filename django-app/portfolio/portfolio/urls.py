"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView  # Импорт RedirectView
from django.templatetags.static import static as static_url  # Импорт для статического URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_port/', include('main_port.urls')),
    path('favicon.ico', RedirectView.as_view(url=static_url('favicon.ico'))),
]

# Если нужно добавить главную страницу
urlpatterns += [path('', include('main_port.urls'))]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

