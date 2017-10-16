"""smart_cookbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from rest_framework.routers import DefaultRouter

from smart_cookbook import viewsets

router = DefaultRouter()
router.register('ingredients', viewsets.IngredientViewset)
router.register('recipes', viewsets.RecipeViewset)
router.register('ingredient-quantities', viewsets.IngredientQuantityViewset)

admin.autodiscover()

urlpatterns = [
    *router.get_urls(),
    url(rf'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$', serve, kwargs={'document_root': settings.STATIC_ROOT}),
    url(rf'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$', serve, kwargs={'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', admin.site.urls),
]


