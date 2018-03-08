from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^classifier1$', views.index1, name='index1'),
    url(r'^classifier$', views.index, name='index'),
    url(r'^result$', views.result, name='result'),
]
