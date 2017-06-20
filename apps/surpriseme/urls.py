from django.conf.urls import url
from . import views
app_name = 'surpriseme'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^surprise$', views.surprise, name='surprise'),
    url(r'^results$', views.results, name='results'),
]