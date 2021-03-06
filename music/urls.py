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
    url(r'^register/$', views.UserFormView.as_view() , name='register'),
    url(r'^login/$', views.LoginFormView.as_view() , name='login'),
    url(r'^logout/$', views.LogoutView.as_view() , name='logout'),
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),  
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
   
]
