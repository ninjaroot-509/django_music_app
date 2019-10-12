from django.contrib import admin
from .models import  Acceuil, Acceuiluser, Album, Song, Post, Comment, Playlist, Songp, Priere, Profile

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


admin.site.register(Album)
admin.site.register(Playlist)
admin.site.register(Priere)
admin.site.register(Acceuil)
admin.site.register(Acceuiluser)
admin.site.register(Songp)
admin.site.register(Song)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_location')
    list_select_related = ('profile', )

    def get_location(self, instance):
        return instance.profile.location
    get_location.short_description = 'Location'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author',
		'status')
	list_filter = ('status', 'created_on', 'author')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
	ordering = ['status', '-created_on']

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'post', 'created', 'active')
	list_filter = ('active', 'created', 'updated')
	search_fields = ('name', 'email', 'body')

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)

