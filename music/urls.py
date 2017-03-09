from django.conf.urls import url
from . import views


app_name = 'music'

# urlpatterns = [
#     url(r'^$', views.index , name='index'),
#     url(r'^add/$', views.add , name='add'),
#     url(r'^(?P<album_id>[0-9]+)$', views.detail, name='detail'),  
#     url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'), 
# ]


urlpatterns = [
    url(r'^$', views.IndexView.as_view() , name='index'),
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),  
   
]
