from django.urls import path, include

from . import api, views

apipatterns = [
    path(r'', api.index, name='api.index'),
    path(r'phenotypes/<name>', api.phenotypes, name='api.phenotypes'),
]

urlpatterns = [
    path(r'', views.index, name='views.index'),
    path(r'api/', include(apipatterns))
]
