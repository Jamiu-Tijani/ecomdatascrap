from django.conf.urls import url 
from . import views 
urlpatterns = [ url(r'^$', views.datalist.as_view()), url(r'^home/' ,views.index),
                   url(r'^action/' ,views.action) ]