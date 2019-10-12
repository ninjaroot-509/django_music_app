from django.conf.urls import url,include
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^Albums-R/$', views.index, name='index'),
    url(r'^Acceuil/$', views.pageD, name='pageD'),
    url(r'^Albums/$', views.albums, name='albums'),
    url(r'^Playlistes/$', views.playlist, name='playlist'),
    url(r'^Actualites/$', views.post_list, name='blog'),
    url(r'^Contact/$', views.contact_us, name='contact'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$',views.post_detail,name='post_detail'),
    url(r'^Inscrire/$', views.register, name='register'),
    url(r'^Connecter/$', views.login_user, name='login_user'),
    url(r'^$', views.logout_user, name='logout_user'),
    url(r'^404/', views.error_404, name="404"),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<playlist_id>[0-9]+)/'r'playlistes/$', views.detailp, name="detailp"),
    
    # url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    # url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    # url(r'^songs/$', views.songs, name='songs'),
    # url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    
    # url(r'^create_album/$', views.create_album, name='create_album'),
    # url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    # url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    # url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
]

