"""
URL configuration for NewsStudyRostelecom project.

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import main.views as main_views
handler404 = main_views.custom_404
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('home/', include('home.urls')),
    path('users/', include('users.urls')),
             ##http://127.0.0.1:8000/
#] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug/__', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Панель администрирования Зеленых новостей"
admin.site.index_title = "Зеленые новости"
admin.site.index_template = 'main/custom_admin.html'
