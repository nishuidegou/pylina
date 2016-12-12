from django.conf.urls import url
from . import views
from .views import ChatterView

urlpatterns = [
    # ex: /chatter/
    url(r'^$',views.index,name='index'),
    url(r'^chattering',ChatterView.as_view(),name='chatter'),
]