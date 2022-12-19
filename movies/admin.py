from django.contrib import admin
from .models import Genre, Movie

class GengreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('title', 'number_in_stock', 'daily_rate')

admin.site.register(Genre, GengreAdmin)
admin.site.register(Movie, MovieAdmin)



