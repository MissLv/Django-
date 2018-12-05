"""myfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^", include("Adm_Sr_Mod.urls")),
    url(r'^search/', include('haystack.urls')),
    url(r"^FreshOrder/",include("FreshOrder.urls")),
    url(r"^GoodsShow/",include("GoodsShow.urls")),
    url(r"^usermode/",include("usermode.urls")),
    url(r"^usermode/",include("usermode.urls")),
    url(r"^shopping_cart/",include("shopping_cart.urls")),
    url(r'^tinymce/', include('tinymce.urls')),
]
