from django.conf.urls import url
from . import views

app_name = "fileapp"

urlpatterns = [
    url(r'^$', views.BasicUploadView.as_view(), name='index'),
    url(r'^clear/$', views.clear_database, name='clear_database'),
]