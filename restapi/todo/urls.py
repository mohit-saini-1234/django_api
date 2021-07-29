from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('dummy', views.dummy, name='dummy'),
    path('hello', views.hello_world, name='hello_world'),
]
