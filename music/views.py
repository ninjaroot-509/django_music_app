from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .forms import AlbumForm, SongForm, UserForm, CommentForm
from .models import Acceuil, Acceuiluser, Album, Playlist, Post, Comment, Priere
from django import template
from django.template.loader import get_template 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

@login_required(login_url='/Connecter/')
def playlist(request):
    prieres = Priere.objects.all()
    playlists_list = Playlist.objects.all()
    paginator = Paginator(playlists_list, 7)
    page = request.GET.get('page')
    try:
        playlists = paginator.page(page)
    except PageNotAnInteger:
        playlists = paginator.page(1)
    except EmptyPage:
        playlists = paginator.page(paginator.num_pages)
    context = {
        'playlists': playlists,
        'paginate': True
        }
    return render(request, 'music/playlistM.html', {'playlists': playlists, 'prieres':prieres})

@login_required(login_url='/Connecter/')
def detailp(request, playlist_id):
    play = Playlist.objects.all()
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    return render(request, 'music/detailP.html', {'playlist': playlist, 'play': play})

def contact_us(request):
    if request.user.is_authenticated:
        form_class = ContactForm
            # new logic!
        if request.method == 'POST':
            form = form_class(data=request.POST)

            if form.is_valid():
                contact_name = request.POST.get(
                    'contact_name'
                , '')
                contact_email = request.POST.get(
                    'contact_email'
                , '')
                contact_subject = request.POST.get(
                    'contact_subject'
                , '')
                form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('music/contact_template.txt')
            
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_subject': contact_subject,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "Nouveaux Messages",
                content,
                "LevanjilPlay" +'',
                ['stanleycastin19@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('/Contact/')

        return render(request, 'music/contactU.html', {
            'form': form_class,
        })
    else:
        form_class = ContactForm
            # new logic!
        if request.method == 'POST':
            form = form_class(data=request.POST)

            if form.is_valid():
                contact_name = request.POST.get(
                    'contact_name'
                , '')
                contact_email = request.POST.get(
                    'contact_email'
                , '')
                contact_subject = request.POST.get(
                    'contact_subject'
                , '')
                form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('music/contact_template.txt')
            
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_subject': contact_subject,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "Nouveaux Messages",
                content,
                "LevanjilPlay" +'',
                ['stanleycastin19@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('/Contact/')

        return render(request, 'music/contact.html', {
            'form': form_class,
        })

def pageD(request):
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
        form_class = ContactForm
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
        return render(request, 'music/show.html', {'acceuils': acceuils,'albums': albums, 'prieres': prieres, 'playlists':playlists,'form': form_class})

def albums(request):
    if request.user.is_authenticated:
        form_class = ContactForm
        prieres = Priere.objects.all()
        playlists = Playlist.objects.all()
        albums_list = Album.objects.all()
        paginator = Paginator(albums_list, 12)
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
        return render(request, 'music/album2.html', {'albums': albums, 'form': form_class})
    else:
        form_class = ContactForm
        prieres = Priere.objects.all()
        playlists = Playlist.objects.all()
        albums_list = Album.objects.all()
        paginator = Paginator(albums_list, 12)
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
        return render(request, 'music/album1.html', {'albums': albums, 'form': form_class})


def index(request):
    if request.user.is_authenticated:
        form_class = ContactForm
        prieres = Priere.objects.all()
        playlists = Playlist.objects.all()
        albums_list = Album.objects.all()
        paginator = Paginator(albums_list, 9)
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
        return render(request, 'music/indexcon.html', {'albums': albums,'form': form_class})
    else:
        form_class = ContactForm
        prieres = Priere.objects.all()
        playlists = Playlist.objects.all()
        albums_list = Album.objects.all()
        paginator = Paginator(albums_list, 9)
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
        return render(request, 'music/index.html',{'albums':albums,'form': form_class})



def detail(request, album_id):
    if request.user.is_authenticated:
        form_class = ContactForm
        album = get_object_or_404(Album, pk=album_id)
        return render(request, 'music/detailU.html', {'album': album,'form': form_class})
    else:
        album = get_object_or_404(Album, pk=album_id)
        form_class = ContactForm
        return render(request, 'music/detail.html', {'album': album,'form': form_class})



def logout_user(request):
    logout(request)
    return redirect('/Acceuil/')

def login_user(request):
    if request.user.is_authenticated:
        return render(request, 'music/loginerror.html', {})
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/Acceuil/')
                else:
                    return render(request, 'music/login.html', {'error_message': "Votre compte n'est pas disponible"})
            else:
                return render(request, 'music/login.html', {'error_message': "Nom d'utilisateur ou mot de passe invalide"})
        return render(request, 'music/login.html', {})
        


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/Acceuil/')
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)



def error_404(request):
    return render(request, 'music/404.html', context={'errors': True})


def post_list(request):
    if request.user.is_authenticated:
        latest = Post.objects.order_by('-timestamp')[0:3]
        posts_list = Post.objects.all()
        form_class = ContactForm
        paginator = Paginator(posts_list, 3)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {
            'posts': posts,
            'paginate': True
        }
        return render(request, 'music/post_listU.html', {'posts': posts, 'form': form_class})
    else:
        latest = Post.objects.order_by('-timestamp')[0:3]
        form_class = ContactForm
        posts_list = Post.objects.all()
        paginator = Paginator(posts_list, 3)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {
            'posts': posts,
            'paginate': True
        }
        return render(request, 'music/post_list.html', {'posts': posts, 'form': form_class})

@login_required(login_url='/Connecter/')
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post)
    form_class = ContactForm
    comments = post.comments.filter(active=True)
    print (comments)  
        # for comment in comments:
        #   for reply in comment.replies.all():
        #       print reply.body
        #       # print reply.__dict__

        # rpy = Comment.objects.filter(active=True) 
        
    if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                # Assign the current post to the comment
                new_comment.post = post
                # Save the comment to the database
                new_comment.save()


                posts_list = Post.objects.all()
                paginator = Paginator(posts_list, 4)
                page = request.GET.get('page')
                try:
                    posts = paginator.page(page)
                except PageNotAnInteger:
                    posts = paginator.page(1)
                except EmptyPage:
                    posts = paginator.page(paginator.num_pages)
                context = {
                    'posts': posts,
                    'paginate': True
                }
    else:
        comment_form = CommentForm()
        posts_list = Post.objects.all()
        paginator = Paginator(posts_list, 4)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {
            'posts': posts,
            'paginate': True
        }
    return render(request,'music/post_detail.html',
        {'posts': posts,
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'form': form_class
        })  
    

from django.shortcuts import render, render_to_response
from django.template import RequestContext

def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

def handler403(request, exception, template_name="403.html"):
    response = render_to_response("403.html")
    response.status_code = 403
    return response

def handler500(request, exception, template_name="500.html"):
    response = render_to_response("500.html")
    response.status_code = 500
    return response




# def favorite_album(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         if album.is_favorite:
#             album.is_favorite = False
#         else:
#             album.is_favorite = True
#         album.save()
#     except (KeyError, Album.DoesNotExist):
#         return JsonResponse({'success': False})
#     else:
#         return JsonResponse({'success': True})

# def songs(request, filter_by):
#     albums = Album.objects.filter(request)
#     for song in album.song_set.all():
#         song_ids.append(song.pk)
#     admin_songs = Song.objects.filter(pk__in=song_ids)
#     if filter_by == 'favorites':
#         admin_songs = admin_songs.filter(is_favorite=True)
#     return render(request, 'music/songs.html', {
#         'song_list': admin_songs,
#         'filter_by': filter_by,
#     })

# def favorite(request, song_id):
#     song = get_object_or_404(Song, pk=song_id)
#     try:
#         if song.is_favorite:
#             song.is_favorite = False
#         else:
#             song.is_favorite = True
#         song.save()
#     except (KeyError, Song.DoesNotExist):
#         return JsonResponse({'success': False})
#     else:
#         return JsonResponse({'success': True})
        




# def songs(request, filter_by):
#     albums = Album.objects.filter(request)
#     for song in album.song_set.all():
#         song_ids.append(song.pk)
#     admin_songs = Song.objects.filter(pk__in=song_ids)
#     if filter_by == 'favorites':
#         admin_songs = admin_songs.filter(is_favorite=True)
#     return render(request, 'music/songs.html', {
#         'song_list': admin_songs,
#         'filter_by': filter_by,
#     })


# def create_album(request):
#     form = AlbumForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         album = form.save(commit=False)
#         album.user = request.user
#         album.album_logo = request.FILES['album_logo']
#         file_type = album.album_logo.url.split('.')[-1]
#         file_type = file_type.lower()
#         if file_type not in IMAGE_FILE_TYPES:
#             context = {
#                 'album': album,
#                 'form': form,
#                 'error_message': 'Image file must be PNG, JPG, or JPEG',
#             }
#             return render(request, 'music/create_album.html', context)
#         album.save()
#         return render(request, 'music/detail.html', {'album': album})
#     context = {
#         "form": form,
#     }
#     return render(request, 'music/create_album.html', context)


# def create_song(request, album_id):
#     form = SongForm(request.POST or None, request.FILES or None)
#     album = get_object_or_404(Album, pk=album_id)
#     if form.is_valid():
#         albums_songs = album.song_set.all()
#         for s in albums_songs:
#             if s.song_title == form.cleaned_data.get("song_title"):
#                 context = {
#                     'album': album,
#                     'form': form,
#                     'error_message': 'You already added that song',
#                 }
#                 return render(request, 'music/create_song.html', context)
#         song = form.save(commit=False)
#         song.album = album
#         song.audio_file = request.FILES['audio_file']
#         file_type = song.audio_file.url.split('.')[-1]
#         file_type = file_type.lower()
#         if file_type not in AUDIO_FILE_TYPES:
#             context = {
#                 'album': album,
#                 'form': form,
#                 'error_message': 'Audio file must be WAV, MP3, or OGG',
#             }
#             return render(request, 'music/create_song.html', context)

#         song.save()
#         return render(request, 'music/detail.html', {'album': album})
#     context = {
#         'album': album,
#         'form': form,
#     }
#     return render(request, 'music/create_song.html', context)


# def delete_album(request, album_id):
#     if not request.user.is_authenticated():
#         return render(request, 'music/login.html')
#     else:
#         album = Album.objects.get(pk=album_id)
#         album.delete()
#         albums = Album.objects.filter(user=request.user)
#     return render(request, 'music/index.html', {'albums': albums})


# def delete_song(request, album_id, song_id):
#     if not request.user.is_authenticated():
#         return render(request, 'music/login.html')
#     else:
#         album = get_object_or_404(Album, pk=album_id)
#         song = Song.objects.get(pk=song_id)
#         song.delete()
#     return render(request, 'music/detail.html', {'album': album})
# def favorite(request, song_id):
#     song = get_object_or_404(Song, pk=song_id)
#     try:
#         if song.is_favorite:
#             song.is_favorite = False
#         else:
#             song.is_favorite = True
#         song.save()
#     except (KeyError, Song.DoesNotExist):
#         return JsonResponse({'success': False})
#     else:
#         return JsonResponse({'success': True})


# def favorite_album(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         if album.is_favorite:
#             album.is_favorite = False
#         else:
#             album.is_favorite = True
#         album.save()
#     except (KeyError, Album.DoesNotExist):
#         return JsonResponse({'success': False})
#     else:
#         return JsonResponse({'success': True})
