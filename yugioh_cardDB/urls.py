"""yugioh_DB URL Configuration

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
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    path(r'', IndexView.as_view(), name="index"),
    path(r'pack_list', PackListView.as_view(), name="pack_list"),
    path(r'pack_detail/<int:pk>', PackDetailView.as_view(), name='pack_detail'),
    path(r'card_detail/<int:pk>', CardDetailView.as_view(), name='card_detail'),
    path(r'search', SearchView.as_view(), name='search'),
    path(r'search_result', SearchResultView.as_view(), name='search_result'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]