"""oreski_transliator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import render_index, zapolnit_iz_raspisania_na_nedelu, get_hash_igraet_seichas, \
    ostanovit_vosproizvedenie, prodolzit_vosproizvedenie
from oreski_transliator import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('zapolnit_iz_raspisania_na_nedelu/', zapolnit_iz_raspisania_na_nedelu, name='zapolnit_iz_raspisania_na_nedelu'),
    path('get_hash_igraet_seichas/', get_hash_igraet_seichas, name='get_hash_igraet_seichas'),
    path('ostanovit_vosproizvedenie/', ostanovit_vosproizvedenie, name='ostanovit_vosproizvedenie'),
    path('prodolzit_vosproizvedenie/', prodolzit_vosproizvedenie, name='prodolzit_vosproizvedenie'),
    path('', render_index),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
