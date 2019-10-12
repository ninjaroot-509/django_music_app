from django import forms
from django.contrib.auth.models import User

from .models import Album, Playlist, Song, Post, Comment, Songp


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']

class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = ['playlist_title',]


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']

class SongpForm(forms.ModelForm):

    class Meta:
        model = Songp
        fields = ['songp_title', 'audio_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_subject = forms.CharField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Votre nom:"
        self.fields['contact_email'].label = "Votre email:"
        self.fields['contact_subject'].label = "Subject:"
        self.fields['content'].label = "Ecrivez Ici:"
