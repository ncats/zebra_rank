from django.urls import path, include

from . import api, views

apipatterns = [
    path(r'', api.index, name='api.index'),
    path(r'sources', api.sources, name='api.sources'),
    path(r'phenotypes/<name>', api.phenotypes, name='api.phenotypes'),
    path(r'<source>/zrank', api.zebra_rank, name='api.zrank'),
]

urlpatterns = [
    path(r'', views.index, name='views.index'),
    path(r'api/', include(apipatterns)),
    path(r'<source>', views.data_source, name='view.data_source'),
]
