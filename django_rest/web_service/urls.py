from django.conf.urls import url
from . import views

urlpatterns = [
url( r'^$', views.WS , name='web-service'),
]
