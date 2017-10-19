from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^classifier$', views.index, name='index'),
    url(r'^result$', views.result, name='result'),
]
