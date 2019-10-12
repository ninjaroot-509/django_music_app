from django.shortcuts import render
from music.models import Album, Priere, Acceuil, Acceuiluser, Playlist
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def page(request):
    if request.user.is_authenticated:
        form_class = ContactForm
        prieres = Priere.objects.all()
        acceuilusers = Acceuiluser.objects.all()
        playlists = Playlist.objects.all()
        albums_list = Album.objects.all()
        paginator = Paginator(albums_list, 6)
        page = request.GET.get('page')
        try:
            albums = paginator.page(page)
        except PageNotAnInteger:
            albums = paginator.page(1)
        except EmptyPage:
            albums = paginator.page(paginator.num_pages)
        context = {
            'albums': albums,
            'paginate': True
        }
        return render(request, 'music/user.html', {'acceuilusers':acceuilusers, 'albums': albums, 'prieres': prieres, 'playlists':playlists,'form': form_class})
    else:
        # form_class = ContactForm
        prieres = Priere.objects.all()
        acceuils = Acceuil.objects.all()
        playlists = Playlist.objects.all()
        albums_list = Album.objects.all()
        paginator = Paginator(albums_list, 6)
        page = request.GET.get('page')
        try:
            albums = paginator.page(page)
        except PageNotAnInteger:
            albums = paginator.page(1)
        except EmptyPage:
            albums = paginator.page(paginator.num_pages)
        context = {
            'albums': albums,
            'paginate': True
        }
        return render(request, 'music/show.html', {'acceuils': acceuils,'albums': albums, 'prieres': prieres, 'playlists':playlists})
